import json
import os
import sys
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random
from utils import get_key


def encrypt(key, filename):
    chunk_size = 64 * 1024
    o_file = filename + "_encrypted"
    file_size = str(os.path.getsize(filename)).zfill(16)
    iv = Random.new().read(16)

    encryptor = AES.new(key, AES.MODE_CBC, iv)

    with open(filename, 'rb') as infile:
        with open(o_file, 'wb') as outfile:
            outfile.write(file_size.encode('utf-8'))
            outfile.write(iv)

            while True:
                chunk = infile.read(chunk_size)

                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += b' ' * (16 - (len(chunk) % 16))

                outfile.write(encryptor.encrypt(chunk))


def json2xml_conversion(json_obj, line_padding=""):
    result_list = list()

    json_obj_type = type(json_obj)

    if json_obj_type is list:
        for sub_elem in json_obj:
            result_list.append(json2xml_conversion(sub_elem, line_padding))

        return "\n".join(result_list)

    if json_obj_type is dict:
        for tag_name in json_obj:
            sub_obj = json_obj[tag_name]
            result_list.append("%s<%s>" % (line_padding, tag_name))
            result_list.append(json2xml_conversion(sub_obj, "\t" + line_padding))
            result_list.append("%s</%s>" % (line_padding, tag_name))

        return "\n".join(result_list)

    return "%s%s" % (line_padding, json_obj)


# cleanup files in destination directory
entries = os.listdir('/dest')
for entry in entries:
    remove_file = "/dest/" + entry
    if os.path.exists(remove_file):
        os.remove(remove_file)

# Read, convert and encrypt files
entries = os.listdir('/src')
password = "justapassword"
for entry in entries:
    json_file = "/src/" + entry
    print("converting Json file"+json_file)
    with open(json_file, 'r') as f:
        json_content = f.read()
    j = json.loads(json_content)
    xmlString = json2xml_conversion(j)
    output_file = "/dest/" + entry.split(".")[0] + ".xml"

    with open(output_file, 'w') as f:
        f.write(xmlString)
    print("converted " + json_file + " to XML file" + output_file)
    encrypt(get_key(password), output_file)
    if os.path.exists(output_file):
        os.remove(output_file)
