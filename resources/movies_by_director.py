from flask_restful import Resource, reqparse

from queries.movies_by_director import get_movies_by_director

class Movies_By_Director(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', default="'%'")
        args = parser.parse_args()

        movies = get_movies_by_director(args['name'])

        return movies