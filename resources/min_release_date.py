from flask_restful import Resource

from queries.get_min_release_date import get_min_release_date

class Min_Release_Date(Resource):
    def get(self):
        date = get_min_release_date()
        return date