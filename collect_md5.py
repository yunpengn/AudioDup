import csv
import os

insert_query = "INSERT INTO md5 (video_name, md5_val) VALUES ('%s', '%s');"

# Reads from the csv file.
queries = []
with open('md5.csv') as file:
    csv_file = csv.reader(file, delimiter=',')

    # Reads line by line.
    for row in csv_file:
        video_name = os.path.splitext(row[0])[0]
        md5_val = row[1]
        query = insert_query % (video_name, md5_val)
        queries.append(query)

# Writes the result to the given file.
with open('md5.sql', 'a') as file:
    for query in queries:
        file.write(query + "\n")
