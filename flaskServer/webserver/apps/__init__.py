from flask import Flask
import os, glob
app = Flask(__name__, template_folder = 'template')
__all__ = [os.path.basename(f)[:-3] for f in glob.glob(os.path.dirname(__file__) + "/*.py")]