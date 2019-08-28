from flask import Flask

# Creates a Flask app.
app = Flask(__name__)


# Defines the health check endpoint.
@app.route('/')
def hello_world():
    return 'We love ByteDance!'


# Only runs the routing when the current file is being run.
if __name__ == '__main__':
    app.run()
