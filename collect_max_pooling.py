import numpy as np
import os

insert_query = "INSERT INTO video_max_pooling (video_name, frame_id, max_pooling) VALUES ('%s', %s, '%s');"

# Reads from the csv file.
queries = []
npy_file = np.load("max_pooling.npy", allow_pickle=True)

# Reads line by line.
for row in npy_file:
    without_ext = os.path.splitext(row[0])[0].split("/")[1].split("\\")
    video_name = without_ext[0]
    frame_id = without_ext[1]

    max_pooling_value = row[1].tolist()[0]
    query = insert_query % (video_name, frame_id, max_pooling_value)
    queries.append(query)

# Writes the result to the given file.
with open('max_pooling.sql', 'a') as file:
    for query in queries:
        file.write(query + "\n")
