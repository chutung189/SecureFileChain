from flask import Flask, request, render_template, redirect, url_for
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
        "file_hash": file_hash
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

if __name__ == '__main__':
    app.run(host='localhost', port=9000, debug=True)