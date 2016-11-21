from flask_restful import Resource

from queries.get_all_companies import get_all_companies

class Get_All_Companies(Resource):
    def get(self):
        companies = get_all_companies()
        return companies