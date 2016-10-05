from flask_restful import Resource, reqparse

class Search(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('title')
        args = parser.parse_args()

        return args