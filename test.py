import glob
import os
import random

from dejavu import Dejavu
from dejavu.recognize import FileRecognizer
from pydub import AudioSegment


# Database connection config.
config = {
    "database": {
        "host": "localhost",
        "user": "dejavu",
        "passwd": "dejavu",
        "db": "dejavu",
    },
    "database_type": "mysql",
}

# Creates a new instance.
djv = Dejavu(config)

# The number of iterations in the test.
correct_count = 0
test_limit = 50
min_length = 1000

# A list of all input song file names.
file_names = glob.glob("data/audios/*.mp3")

for i in range(test_limit):
    # Randomly selects an input file.
    file_name = random.choice(file_names)
    print("Iteration %s: read file %s." % (i, file_name))

    # Reads the song.
    song = AudioSegment.from_mp3(file_name)
    if len(song) <= min_length:
        print("The given song is too short. Will skip.")
        continue

    # Selects a random piece from the given file.
    duration = random.randint(1000, len(song))
    start_point = random.randint(0, len(song) - duration)
    end_point = start_point + duration
    print("Sliced song is from %s to %s." % (start_point, end_point))

    # Saves the sliced song to a file on disk.
    sliced_song = song[start_point:end_point]
    sliced_song.export("tmp.mp3", format="mp3")
    print("The sliced song has been saved to tmp.mp3 temporarily.")

    # Attempts to recognize the song.
    result = djv.recognize(FileRecognizer, "tmp.mp3")
    print("The result is %s" % result)

    # Checks the prediction result.
    original_song_name = os.path.splitext(os.path.basename(file_name))[0]
    predicted_song_name = result['song_name'].decode()
    if original_song_name == predicted_song_name:
        correct_count += 1

    # Removes the file.
    os.remove("tmp.mp3")
    print("The temporary file at tmp.mp3 has been removed.")
    print("====================================================\n")

print("Out of %s attempts, %s of them (%s%%) are correct." % (test_limit, correct_count, correct_count / test_limit * 100))
