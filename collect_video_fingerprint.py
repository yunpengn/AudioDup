import csv
import json
import os

insert_query = "INSERT INTO video_hash (video_name, frame_id, hash_type, hash_value) VALUES ('%s', %s, %s, '%s');"

# Reads from the csv file.
queries = []
with open('video_hash.csv') as file:
    csv_file = csv.reader(file, delimiter=',')

    # Reads line by line.
    for row in csv_file:
        without_ext = os.path.splitext(row[1])[0]
        video_name = without_ext.split("/")[1]
        frame_id = without_ext.split("/")[2]

        for i in range(3):
            hash_type = i
            hash_value = row[i + 2]
            query = insert_query % (video_name, frame_id, hash_type, hash_value)
            queries.append(query)

# Writes the result to the given file.
with open('video_hash.sql', 'a') as file:
    for query in queries:
        file.write(query + "\n")
