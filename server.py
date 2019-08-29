import uuid
import os

from flask import Flask, render_template, request

# Creates a Flask app.
app = Flask(__name__, static_folder='templates', template_folder='templates')

# Defines the upload folder.
upload_folder = "upload/"


# Defines the health check endpoint.
@app.route('/')
def hello_world():
    return render_template('index.html')

# Defines the file upload endpoint.
@app.route('/upload', methods=['GET', 'POST'])
def upload_video():
    if request.method != 'POST' or 'video_file' not in request.files:
        return render_template('upload.html')

    # Retrieves the uploaded file from request and saves.
    f = request.files['video_file']
    uuid_val = str(uuid.uuid4())
    file_name = os.path.join(app.root_path, upload_folder, uuid_val)
    f.save(file_name)

    # Returns the result.
    result = check_duplicate(file_name)
    overall_video = result[0][0][0] if len(result[0]) > 0 else ''
    overall_score = result[0][0][1] if len(result[0]) > 0 else ''
    video_video = result[1][0][0] if len(result[1]) > 0 else ''
    video_score = result[1][0][1] if len(result[1]) > 0 else ''
    audio_video = result[2][0][0] if len(result[2]) > 0 else ''
    audio_score = result[2][0][1] if len(result[2]) > 0 else ''
    return render_template('result.html', origin_video = uuid_val,
                           overall_video=overall_video, overall_score=overall_score,
                           video_video=video_video, video_score=video_score,
                           audio_video=audio_video, audio_score=audio_score)


# Calls other functions to check whether there exists
def check_duplicate(file_name):
    pass


# Only runs the routing when the current file is being run.
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
