import os
from flask import Flask, request
from flask_restful import Resource, Api

from app.routes import *

os.environ["NLS_LANG"] = ".AL32UTF8"

app = Flask(__name__)
api = Api(app)

init_routes(api=api)

if __name__ == '__main__':
    app.run(debug=True)