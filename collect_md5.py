import hashlib


# Generates the MD5 value (in hex string representation) of a file given its file name.
def md5(file_name):
    hash_md5 = hashlib.md5()

    # Reads the file in chunk of 4096 bytes.
    with open(file_name, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)

    # Converts it to hex string format.
    return hash_md5.hexdigest()
