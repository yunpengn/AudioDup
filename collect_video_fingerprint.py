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
        video_name = os.path.splitext(row[0])[0]
        frame_id = row[1]
        hash_type = row[2]
        hash_value = json.dumps(row[3])

        query = insert_query % (video_name, frame_id, hash_type, hash_value)
        queries.append(query)

# Writes the result to the given file.
with open('video_hash.sql', 'a') as file:
    for query in queries:
        file.write(query + "\n")
