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
mp3_temp_file_format = "%s.mp3"

# Creates a new instance.
djv = Dejavu(config)


# Returns true if a potential duplicate is found for the sound track of the given MP4 file.
def recognize_mp4(file_name):
    video = AudioSegment.from_file(file_name, "mp4")
    audio_file_name = mp3_temp_file_format % uuid.uuid4()
    video.export(audio_file_name, format="mp3")

    return recognize_mp3(audio_file_name)


# Returns true if a potential duplicate is found for the given MP3 file.
def recognize_mp3(file_name):
    song = djv.recognize(FileRecognizer, file_name)
    print("Recognition result is %s" % song)
    return song is None


def recognize_mp3_for_song(file_name, song_id):
    song = djv.recognize_for_song(FileRecognizer, file_name, song_id)
    print("Recognition result is %s" % song)
    return song is None
