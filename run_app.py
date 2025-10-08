from flask import Flask, request, render_template, redirect, url_for, send_file
import os, hashlib
from Blockchain import Blockchain
from Block import Block
from encryption import encrypt_file, decrypt_file, generate_key
from ipfs_helper import upload_to_ipfs, download_from_ipfs

app = Flask(__name__, template_folder='app/templates')
blockchain = Blockchain()
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Trang chủ: hiển thị danh sách các block
@app.route('/')
def index():
    return render_template('index.html', blocks=blockchain.chain)

# Upload file, mã hóa, lưu IPFS và thêm vào blockchain
@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    password = request.form['password']
    username = request.form['username']
    key = generate_key(password)

    path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(path)

    encrypted_path = path + ".enc"
    encrypt_file(path, encrypted_path, key)

    file_hash = hashlib.sha256(open(encrypted_path, 'rb').read()).hexdigest()
    cid = upload_to_ipfs(encrypted_path)

    data = {
        "filename": file.filename,
        "CID": cid,
        "file_hash": file_hash,
        "username": username
    }
    blockchain.mine(data)
    return redirect(url_for('index'))

# Xác minh file bằng CID
@app.route('/verify/<cid>', methods=['GET'])
def verify(cid):
    encrypted_path = os.path.join(UPLOAD_FOLDER, cid + ".enc")
    download_from_ipfs(cid, encrypted_path)
    new_hash = hashlib.sha256(open(encrypted_path, 'rb').read()).hexdigest()

    for block in blockchain.chain:
        if isinstance(block.data, dict) and block.data.get("CID") == cid:
            original_hash = block.data.get("file_hash")
            valid = (original_hash == new_hash)
            return render_template('verify.html', cid=cid, valid=valid)

    return "CID not found!"

@app.route('/download/<cid>')
def download(cid):
    block = next((b for b in blockchain.chain if b.data.get("CID") == cid), None)
    filename = block.data["filename"] if block else f"{cid}.download"
    output_path = os.path.join(UPLOAD_FOLDER, f"{cid}.download")
    local_path = download_from_ipfs(cid, output_path)
    # Nếu là thư mục, lấy file bên trong
    if os.path.isdir(local_path):
        files = os.listdir(local_path)
        if files:
            local_path = os.path.join(local_path, files[0])
        else:
            return "Không tìm thấy file trong thư mục tải về.", 404
    if not os.path.exists(local_path):
        return "Không tìm thấy hoặc tải file từ IPFS thất bại.", 404
    return send_file(local_path, as_attachment=True, download_name=filename)

if __name__ == '__main__':
    app.run(host='localhost', port=9000, debug=True)