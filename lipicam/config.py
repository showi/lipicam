from os import path as P
import ConfigParser
import lipicam

conf_names = ['lipicam-base.cfg', 'lipicam.cfg']

class Config(ConfigParser.ConfigParser):

    def __init__(self):
        ConfigParser.ConfigParser.__init__(self)
        paths = [P.join(lipicam.config_path, path) for path in conf_names]
        lipicam.log.debug('path: {}'.format(paths))
        self.read(paths)


config = Config()
