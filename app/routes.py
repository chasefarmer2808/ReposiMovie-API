from resources.search_title import Search_Title
from resources.search_genre import Search_Genre
from resources.search_castcrew import Search_Castcrew
from resources.movie_id import Movie_Id
from resources.person_id import Person_Id
from resources.top10 import Top10

API_PREFIX = '/api/v1'
SEARCH_SUFFIX = '/search_title'
GENRE_SUFFIX = '/search_genre'
CAST_CREW_SUFFIX = '/search_castcrew'
MOVIE_ID_SUFFIX = '/movie'
PERSON_ID_SUFFIX = '/person'
TOP10_SUFFIX = '/top10'

def init_routes(api):
    api.add_resource(Search_Title, API_PREFIX + SEARCH_SUFFIX)
    api.add_resource(Search_Genre, API_PREFIX + GENRE_SUFFIX)
    api.add_resource(Search_Castcrew, API_PREFIX + CAST_CREW_SUFFIX)
    api.add_resource(Movie_Id, API_PREFIX + MOVIE_ID_SUFFIX)
    api.add_resource(Person_Id, API_PREFIX + PERSON_ID_SUFFIX)
    api.add_resource(Top10, API_PREFIX + TOP10_SUFFIX)
