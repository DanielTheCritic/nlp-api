import json
import os
from itertools import islice 

def getCurrentVersion():
    with open(getFilePath("version.json"), "r") as versionString:
        obj = json.load(versionString)
    return ".".join([ str(obj["major"]), str(obj["minor"]), str(obj["patch"]) ])

def getFilePath(fileName):
    current = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current, fileName)