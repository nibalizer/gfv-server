from flask import Flask
import subprocess
import os
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/video/<path:video>')
def play_video(video):
    print "python", video
#    try:
#        os.remove('/tmp/gfv')
#    except OSError:
#        pass
    #print ['~/get-flash-videos/get_flash_videos', '-f', '/tmp/gfv', '-p', '--player', '~/video.sh', str(video)]
#    subprocess.call(['~/get-flash-videos/get_flash_videos', '-f', '/tmp/gfv', '-p', '--player', '~/video.sh', video], shell=True)
#    subprocess.call(['/home/kiosk/sandbox/gfv-server/gfv-bin', video], shell=True)
    os.system("/home/kiosk/sandbox/gfv-server/gfv-bin {0}".format(video))
    return "Playing Video {0}".format(video)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
