import ipfshttpclient

def upload_to_ipfs(filepath):
    client = ipfshttpclient.connect()  # localhost:5001
    res = client.add(filepath)
    return res['Hash']  # CID

def download_from_ipfs(cid, output_path):
    import ipfshttpclient
    client = ipfshttpclient.connect()
    try:
        client.get(cid, target=output_path)
        return output_path
    except Exception as e:
        print("Download error:", e)
        return None
