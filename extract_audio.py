import glob
import multiprocessing
import os
import sys
import traceback

from pydub import AudioSegment

# Standard output format for mp3 files.
AUDIO_FILE_FORMAT = "data/audios/%s.mp3"


# Extracts mp3 from an mp4 file.
def extract(video_file_name):
    # Read from mp4 file.
    print("Begins to read video with file name %s." % video_file_name)
    video = AudioSegment.from_file(video_file_name, "mp4")

    # Gets the new file name.
    actual_video_id = os.path.splitext(os.path.basename(video_file_name))[0]
    audio_file_name = AUDIO_FILE_FORMAT % actual_video_id

    # Exports the mp3 file.
    print("Begins to export audio to %s.\n" % audio_file_name)
    video.export(audio_file_name, format="mp3")


# A list of all input video file names.
file_names = glob.glob("data/videos/*.mp4")

# Gets the number of processes suitable for the current machine.
try:
    num_processes = multiprocessing.cpu_count()
except NotImplementedError:
    num_processes = 1
else:
    # There should be at least 1 process.
    num_processes = max(num_processes, 1)

# Creates a process pool and an iterator using this pool.
pool = multiprocessing.Pool(num_processes)
iterator = pool.imap_unordered(extract, file_names)

# Iterates through each input file.
while True:
    try:
        next(iterator)
    except multiprocessing.TimeoutError:
        continue
    except StopIteration:
        break
    except:
        traceback.print_exc(file=sys.stdout)

# Mark the process as completed and closes resources.
pool.close()
pool.join()
print("Completed. We have extracted audios from %s video files." % len(file_names))
