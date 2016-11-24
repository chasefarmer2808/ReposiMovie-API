from flask_restful import Resource, reqparse

from queries.movies_by_title import get_movie_by_title

class Search_Title(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('title', default="'%'")
        parser.add_argument('limit', type=int, default=0)
        args = parser.parse_args()

        movies = get_movie_by_title(args['title'], args['limit'])

        return movies