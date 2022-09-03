import pandas as pd
import requests

from requests.exceptions import RequestException
from storage import DBStorage
from urllib.parse import quote_plus

#from settings import *

def search_api(query, pages=int(RESULT_COUNT/10)):
  '''queries custom search API end point and returns search results'''
  result = []
  
  for i in range(0, pages):
    start = i * 10 + i  #rank of first record on page returned (1, 11,...)
    url = SEARCH_URL.format(
        key=SEARCH_KEY,
        cx=SEARCH_ID,
        query=quote_plus(query),  #ensures query is properly (URL) formatted
        start=start
    )
    
    reponse = requests.get(url)
    data = response.json()
    results += data["items"]  #returns list of dicts
  
  res_df = pd.DataFrame.from_dict(results)
  res_df["rank"] = list(range(1, res_df.shape[0] + 1))   #indicates rank (1-11)
  res_df = res_df[["link", "rank", "snippet", "title"]]   #removed a few fields
  return res_df