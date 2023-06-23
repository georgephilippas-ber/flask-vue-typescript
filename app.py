from os.path import join, dirname
from flask import Flask, send_from_directory

app = Flask(__name__)

frontend_path: str = join(dirname(__file__), "frontend-vue", "dist")


@app.route('/')
def index():
    return send_from_directory(frontend_path, "index.html")


@app.route("/<path:filename>")
def static_files(filename):
    return send_from_directory(frontend_path, filename)


# @app.route('/')
# def hello_world():  # put application's code here
#     return 'Hello World!'


if __name__ == '__main__':
    app.run()
