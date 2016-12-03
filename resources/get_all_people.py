from flask_restful import Resource

from queries.get_all_people import get_all_people

class Get_All_People(Resource):
    def get(self):
        people = get_all_people()
        return people