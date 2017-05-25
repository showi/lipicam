from os import path as P
import logging
logging.basicConfig()
log = logging.getLogger('lipicam')
log.setLevel(logging.DEBUG)

base_path = P.abspath(P.join(P.dirname(__file__)))
module_path = P.abspath(P.join(base_path, P.pardir))
config_path = P.join(base_path, 'config')
data_path = P.join(base_path, '__data__')
