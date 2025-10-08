from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import hashlib

def encrypt_file(input_path, output_path, key):
    # Sinh IV
    iv = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CFB, iv)
    
    with open(input_path, 'rb') as f_in, open(output_path, 'wb') as f_out:
        f_out.write(iv)  # ghi IV đầu file
        data = f_in.read()
        ciphertext = cipher.encrypt(data)
        f_out.write(ciphertext)

def decrypt_file(input_path, output_path, key):
    with open(input_path, 'rb') as f_in:
        iv = f_in.read(16)
        cipher = AES.new(key, AES.MODE_CFB, iv)
        data = f_in.read()
        plaintext = cipher.decrypt(data)
    with open(output_path, 'wb') as f_out:
        f_out.write(plaintext)

def generate_key(password: str):
    # Dùng SHA256 để sinh khóa AES từ mật khẩu
    return hashlib.sha256(password.encode()).digest()
