import os
from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS

from app.routes import *

os.environ["NLS_LANG"] = ".AL32UTF8"

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
api = Api(app)

init_routes(api=api)

if __name__ == '__main__':
    app.run(debug=True)
