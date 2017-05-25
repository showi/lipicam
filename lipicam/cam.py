from os import path as P
import lipicam
from lipicam.config import config
from lipicam import util

mjpeg_dev = '/dev/shm/mjpeg/cam.jpg'
anim_path = P.join(lipicam.data_path, 'raspianim')

def generate_anim():
    data = [0, 10]
    def generate():
        if data[0] >= data[1]:
            data[0] = 0
        content = util.readfile(P.join(anim_path, '%03d.png' % data[0]))
        data[0] += 1
        yield content
    return generate

def generate():
    yield util.readfile(mjpeg_dev)

class Cam(object):

    def __init__(self, dev=mjpeg_dev):
        self.dev = dev
        self.path = mjpeg_dev
        self.generate = generate
        if config.getboolean('main', 'debug'):
            self.generate = generate_anim()

    def read(self):
        return self.generate()

if __name__ == '__main__':
    c = Cam()
    print('%s' % c.read())
