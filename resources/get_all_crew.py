from flask_restful import Resource

from queries.get_all_crew import get_all_crew

class Get_All_Crew(Resource):
    def get(self):
        crew = get_all_crew()
        return crew