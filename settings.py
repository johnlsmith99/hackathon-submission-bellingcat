SEARCH_KEY = ""
SEARCH_ID = ""
COUNTRY = "uk"  #this could be changed or redone with other countries
SEARCH_URL = "https://www.googleapis.com/customsearch/v1?key={key}&cx={cx}&q={query}&start={start}&num=10&gl=" + COUNTRY
RESULT_COUNT = 20   #this will mean that we technically only get 50 searches (as it is 10 per page standard)


import os
if os.path.exists("private.py"):
        from private import *
