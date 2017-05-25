from os import path as P
import logging
logging.basicConfig()
log = logging.getLogger('lipicam')
log.setLevel(logging.DEBUG)

base_path = P.abspath(P.join(P.dirname(__file__)))
module_path = P.abspath(P.join(base_path, P.pardir))
log.debug('base_path: {}'.format(base_path))
config_path = P.join(base_path, 'config')
log.debug('config_path: {}'.format(config_path))
data_path = P.join(base_path, '__data__')
log.debug('config_path: {}'.format(config_path))
