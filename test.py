import glob
import os
import random

from dejavu import Dejavu
from dejavu.recognize import FileRecognizer
from pydub import AudioSegment
from pydub.generators import WhiteNoise


def recognize_from_file(input_file_name, original_name):
    # Attempts to recognize the song.
    recognize_result = djv.recognize(FileRecognizer, input_file_name)
    print("The result is %s" % recognize_result)

    # Removes the file.
    os.remove(input_file_name)
    print("The temporary file at %s has been removed." % input_file_name)

    # Checks the prediction result.
    if recognize_result is None:
        print("Unable to recognize the sound.")
        return False
    predicted_name = recognize_result['song_name'].decode()
    return original_name == predicted_name


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
noise_partition = 5

# A list of all input song file names.
file_names = glob.glob("data/audios/*.mp3")

for i in range(test_limit):
    # Randomly selects an input file.
    file_name = random.choice(file_names)
    original_song_name = os.path.splitext(os.path.basename(file_name))[0]
    print("Iteration %s: read file %s." % (i, file_name))

    # Reads the song.
    song = AudioSegment.from_mp3(file_name)
    if len(song) <= min_length:
        print("The given song is too short. Will skip.")
        continue

    # Selects a random piece from the given file.
    duration = random.randint(min_length, len(song))
    start_point = random.randint(0, len(song) - duration)
    end_point = start_point + duration
    print("Sliced song is from %s to %s." % (start_point, end_point))

    # Saves the sliced song to a file on disk.
    sliced_song = song[start_point:end_point]
    sliced_song.export("tmp1.mp3", format="mp3")
    print("The sliced song has been saved to tmp1.mp3 temporarily.")

    # Attempts to recognize.
    if recognize_from_file("tmp1.mp3", original_song_name):
        correct_count += 1

    # Creates a noise of at most a certain length.
    noise_duration = random.randint(0, duration // noise_partition)
    noise = WhiteNoise().to_audio_segment(noise_duration)

    # Adds noise to the sound.
    start_point = random.randint(0, duration - noise_duration)
    noise_song = sliced_song.overlay(noise, position=start_point)
    noise_song.export("tmp2.mp3", format="mp3")

    # Attempts to recognize.
    if recognize_from_file("tmp2.mp3", original_song_name):
        correct_count += 1
    print("====================================================\n")

print("Out of %s attempts, %s of them (%s%%) are correct."
      % (test_limit, correct_count, correct_count / test_limit * 2 * 100))
