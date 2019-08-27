import hashlib
import MySQLdb

check_query = "SELECT * FROM md5 WHERE md5_val = '%s'"


# Checks whether there exists a file with the same MD5 value.
def check_md5_exists(file_name):
    # Calculates the MD5.
    hash_md5 = hashlib.md5()
    with open(file_name, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    new_md5 = hash_md5.hexdigest()

    # Opens the database connection.
    db = MySQLdb.connect("localhost", "dejavu", "dejavu", "dejavu", charset='utf8')
    cursor = db.cursor()
    query = check_query % new_md5

    # Queries the database.
    cursor.execute(query)
    results = cursor.fetchall()

    # Returns true if there exists an file with the same MD5 value.
    return len(results) != 0
