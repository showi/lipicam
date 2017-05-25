from flask import Flask, Response, render_template
from lipicam.cam import Cam
from lipicam.config import config

cam = Cam()
app = Flask(__name__)

@app.route('/')
def main(name=None):
    return render_template('main.html')

@app.route('/cam/stream')
def route_cam_stream():
    return Response(cam.read(), mimetype='image/jpeg')


@app.route('/cam')
def route_cam():
    return render_template('cam.html')

def run():
    app.run(host=config.get('httpd', 'host'),
            port=config.getint('httpd', 'port'),
            debug=config.getboolean('main', 'debug'))

if __name__ == "__main__":
    run()
