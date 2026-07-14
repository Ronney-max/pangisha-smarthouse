import os
import sys

ROOT_DIR = os.path.dirname(__file__)
SERVER_DIR = os.path.join(ROOT_DIR, "server")

if SERVER_DIR not in sys.path:
    sys.path.insert(0, SERVER_DIR)

from app import app

if __name__ == "__main__":
    app.run()