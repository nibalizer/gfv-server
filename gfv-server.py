from flask import Flask
import subprocess
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/video/<path:video>')
def play_video(video):
    subprocess.call(['gfv', video])
    return "Playing Video {0}".format(video)

if __name__ == '__main__':
    app.run()
