from flask_restful import Resource

from queries.get_table_counts import get_table_counts

class Get_Table_Counts(Resource):
    def get(self):
        counts = get_table_counts()
        return counts