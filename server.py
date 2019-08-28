import uuid

from flask import Flask, render_template, request

# Creates a Flask app.
app = Flask(__name__, template_folder='templates')


# Defines the health check endpoint.
@app.route('/')
def hello_world():
    return render_template('index.html')

# Defines the file upload endpoint.
@app.route('/upload', methods=['GET', 'POST'])
def upload_video():
    if request.method != 'POST':
        return render_template('upload.html')

    # Retrieves the uploaded file from request and saves.
    f = request.files['video_file']
    file_name = str(uuid.uuid4())
    f.save(file_name)
    return 'Hi!'


# Only runs the routing when the current file is being run.
if __name__ == '__main__':
    app.run()
