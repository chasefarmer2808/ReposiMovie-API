from flask_restful import Resource, reqparse

from queries.movies_by_castcrew import get_movie_by_castcrew

class Search_Castcrew(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', action='append', default=[])
        parser.add_argument('limit', type=int)
        args = parser.parse_args()

        movies = get_movie_by_castcrew(args['name'], args['limit'])

        return movies
