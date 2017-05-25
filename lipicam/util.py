import os

def readfile(path):
    with open(path, 'rb') as rh:
        return rh.read()

def gen_secret():
    return os.urandom(24)
