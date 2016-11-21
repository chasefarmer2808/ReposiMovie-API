from resources.search_title import Search_Title
from resources.search_genre import Search_Genre
from resources.search_castcrew import Search_Castcrew
from resources.movie_id import Movie_Id
from resources.person_id import Person_Id
from resources.get_genre_names import Get_Genre_Names
from resources.top10 import Top10
from resources.min_release_date import Min_Release_Date
from resources.get_all_companies import Get_All_Companies
from resources.get_all_cast import Get_All_Cast

API_PREFIX = '/api/v1'
SEARCH_SUFFIX = '/search_title'
GENRE_SUFFIX = '/search_genre'
CAST_CREW_SUFFIX = '/search_castcrew'
MOVIE_ID_SUFFIX = '/movie'
PERSON_ID_SUFFIX = '/person'
Get_Genre_Names_SUFFIX = '/get_all_genres'
TOP10_SUFFIX = '/top10'
MIN_RELEASE_DATE_SUFFIX = '/get_min_release_date'
GET_ALL_COMPANIES_SUFFIX = '/get_all_companies'
GET_ALL_CAST_SUFFIX = '/get_all_cast'

def init_routes(api):
    api.add_resource(Search_Title, API_PREFIX + SEARCH_SUFFIX)
    api.add_resource(Search_Genre, API_PREFIX + GENRE_SUFFIX)
    api.add_resource(Search_Castcrew, API_PREFIX + CAST_CREW_SUFFIX)
    api.add_resource(Movie_Id, API_PREFIX + MOVIE_ID_SUFFIX)
    api.add_resource(Person_Id, API_PREFIX + PERSON_ID_SUFFIX)
    api.add_resource(Get_Genre_Names, API_PREFIX + Get_Genre_Names_SUFFIX)
    api.add_resource(Top10, API_PREFIX + TOP10_SUFFIX)
    api.add_resource(Min_Release_Date, API_PREFIX + MIN_RELEASE_DATE_SUFFIX)
    api.add_resource(Get_All_Companies, API_PREFIX + GET_ALL_COMPANIES_SUFFIX)
    api.add_resource(Get_All_Cast, API_PREFIX + GET_ALL_CAST_SUFFIX)