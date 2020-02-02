from dcs.config import config
import json, os

def write_metadata(data):
    with open(config['storage_directory'] + '/' "metadata.json", 'w') as outfile:
            json.dump(data, outfile)
            return True
    return False

def read_metadata():
    with open(os.path.join(config['storage_directory'], "metadata.json")) as infile:
            data = json.load(infile)
    return data