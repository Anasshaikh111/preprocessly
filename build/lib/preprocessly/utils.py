import json
import os
import re

BASE_PATH = os.path.dirname(__file__)

def load_json_dict(name):
    with open(os.path.join(BASE_PATH, name), "r") as f:
        return json.load(f)

def load_list(name):
    with open(os.path.join(BASE_PATH, name), "r") as f:
        return [w.strip() for w in f.readlines()]

def normalize_whitespace(text):
    return re.sub(r"\s+", " ", text).strip()
