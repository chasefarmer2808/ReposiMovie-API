from resources.search_title import Search_Title
from resources.search_genre import Search_Genre
from resources.search_castcrew import Search_Castcrew

API_PREFIX = '/api/v1'
SEARCH_SUFFIX = '/search_title'
GENRE_SUFFIX = '/search_genre'
CAST_CREW_SUFFIX = '/search_castcrew'

def init_routes(api):
    api.add_resource(Search_Title, API_PREFIX + SEARCH_SUFFIX)
    api.add_resource(Search_Genre, API_PREFIX + GENRE_SUFFIX)
    api.add_resource(Search_Castcrew, API_PREFIX + CAST_CREW_SUFFIX)
