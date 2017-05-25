import os

def readfile(path):
    with open(path, 'rb') as rh:
        return rh.read()
