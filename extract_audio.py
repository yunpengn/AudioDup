import glob
import os

from pydub import AudioSegment

# Standard output format for mp3 files.
AUDIO_FILE_FORMAT = "data/audios/%s.mp3"

# A list of all input video file names.
file_names = glob.glob("data/videos/*.mp4")

# Iterate through each video.
for video_file_name in file_names:
    # Read from mp4 file.
    print("Begins to read video with file name %s." % video_file_name)
    video = AudioSegment.from_file(video_file_name, "mp4")

    # Gets the new file name.
    actual_video_id = os.path.splitext(os.path.basename(video_file_name))[0]
    audio_file_name = AUDIO_FILE_FORMAT % actual_video_id

    # Exports the mp3 file.
    print("Begins to export audio to %s.\n" % audio_file_name)
    video.export(audio_file_name, format="mp3")

# Mark the process as completed.
print("Completed. We have extracted audios from %s video files." % len(file_names))
