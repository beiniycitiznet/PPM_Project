import json

def load_json(filename):
    data = json.loads(filename.read())

    return data