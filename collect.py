from dejavu import Dejavu

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

# Collects all songs.
djv.fingerprint_directory("data/", [".mp3"])

print("We have collected %s fingerprints." % djv.db.get_num_fingerprints())
