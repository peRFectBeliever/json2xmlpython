from Crypto.Hash import SHA256

def get_key(passwd):
    hashes = SHA256.new(passwd.encode('utf-8'))
    return hashes.digest()