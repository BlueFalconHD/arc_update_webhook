import os
def get_token():
    with open(os.path.join(os.path.dirname(__file__), 'TOKEN'), 'r') as f:
        return f.read().strip()
