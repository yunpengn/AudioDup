from dejavu import Dejavu
from dejavu.recognize import MicrophoneRecognizer

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

# Reads 10 seconds from microphone and recognize.
song = djv.recognize(MicrophoneRecognizer, seconds=10)
print("Result: ", song)
