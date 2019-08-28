import os
import uuid

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
confidence_threshold = 100
mp3_temp_file_format = "%s.mp3"

# Creates a new instance.
djv = Dejavu(config)


# Collects a new audio from a given MP4 file and inserts fingerprints into database.
def collect_mp4(file_name):
    # Extracts the audio.
    video = AudioSegment.from_file(file_name, "mp4")
    audio_file_name = mp3_temp_file_format % uuid.uuid4()
    video.export(audio_file_name, format="mp3")

    # Collects the audio.
    djv.fingerprint_file(audio_file_name)


# Returns true if a potential duplicate is found for the sound track of the given MP4 file.
def recognize_mp4(file_name):
    # Extracts audio.
    video = AudioSegment.from_file(file_name, "mp4")
    audio_file_name = mp3_temp_file_format % uuid.uuid4()
    video.export(audio_file_name, format="mp3")

    # Recognizes the audio.
    result = djv.recognize(FileRecognizer, audio_file_name)
    os.remove(audio_file_name)

    # Returns the result.
    return_val = []
    if result is not None and result['confidence'] > confidence_threshold:
        return_val.append([result['song_name'], result['confidence'] / result['fingerprint_count']])
    return return_val


# Returns true if a potential duplicate is found for the given MP3 file.
def recognize_mp3(file_name):
    song = djv.recognize(FileRecognizer, file_name)
    print("Recognition result is %s" % song)
    return song is None


def recognize_mp3_for_song(song_id, file_name):
    song = djv.recognize_for_song(FileRecognizer, song_id, file_name)
    print("Recognition result is %s" % song)
    return song is None
