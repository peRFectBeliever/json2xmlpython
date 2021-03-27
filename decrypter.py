import json
import os
import sys
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random
from utils import get_key


def decrypt(key, file_name):
    chunk_size = 64 * 1024
    output_file = "/dest/" + entry.split("_")[0]

    with open(file_name, 'rb') as infile:
        file_size = int(infile.read(16))
        iv = infile.read(16)

        decrypter = AES.new(key, AES.MODE_CBC, iv)

        with open(output_file, 'wb') as outfile:
            while True:
                chunk = infile.read(chunk_size)

                if len(chunk) == 0:
                    break

                outfile.write(decrypter.decrypt(chunk))
            outfile.truncate(file_size)

entries = os.listdir('/dest')
password = "justapassword"
for entry in entries:
    encfile = "/dest/" + entry
    decrypt(get_key(password), encfile)
