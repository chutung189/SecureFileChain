import ipfshttpclient

def upload_to_ipfs(filepath):
    client = ipfshttpclient.connect()  # localhost:5001
    res = client.add(filepath)
    return res['Hash']  # CID

def download_from_ipfs(cid, output_path):
    client = ipfshttpclient.connect()
    client.get(cid)
    # IPFS tải file về thư mục hiện tại theo tên CID
    import shutil
    shutil.move(cid, output_path)
