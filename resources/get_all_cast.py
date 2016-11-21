from flask_restful import Resource

from queries.get_all_cast import get_all_cast

class Get_All_Cast(Resource):
    def get(self):
        cast = get_all_cast()
        return cast