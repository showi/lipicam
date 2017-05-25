from os import path as P
import ConfigParser
import lipicam

conf_names = ['lipicam-base.cfg', 'lipicam.cfg']

path2replace = {name: ['%{}%'.format(name), getattr(lipicam, name)] for name in ['module_path']}

class Config(ConfigParser.ConfigParser):

    def __init__(self):
        ConfigParser.ConfigParser.__init__(self)
        paths = [P.join(lipicam.config_path, path) for path in conf_names]
        self.read(paths)
        userconf = P.join(self.getpath('config', 'user'), 'lipicam.cfg')
        self.read(userconf)

    def getpath(self, section, key):
        result = self.get(section, key)
        if result is None:
            return None
        for key, tup in path2replace.items():
            result = result.replace(*tup)
        return result

config = Config()
