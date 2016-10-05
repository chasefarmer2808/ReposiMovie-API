from flask_restful import Resource, reqparse
import json
import datetime

from queries.movies import get_movie

class Search(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('title', default='%')
        args = parser.parse_args()

        movies = get_movie(args['title'])

        return movies