from flask_restful import Resource, reqparse

from queries.genre_names import get_genres

class Get_Genre_Names(Resource):
    def get(self):

        genres = get_genres()

        return genres
