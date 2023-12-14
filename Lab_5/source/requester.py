from ctypes import ArgumentError
import requests
from source.media import Media


def requestData(mediaType: str, period: str) -> list[Media]:
  url = "https://api.themoviedb.org/3/trending" + "/" + mediaType + "/" + period + "?language=en-US"
  headers = {
      "accept": "application/json",
      "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJhZDVhNDU4YzljZmMxODdjZThlMDdhM2ZiYTU1MjE0YyIsInN1YiI6IjY1NzRkNzA2ZTkzZTk1MDExZDRlMmM2MiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.MsO7CO9573rr8rTEczZJ4PW6dnVX9xuU2OUNOcaHEts"
  }
  response = requests.get(url, headers=headers)
  content = response.json()['results']
  
  if mediaType == 'movie':
    return [Media(rowMedia['title'], rowMedia['popularity']) for rowMedia in content]
  elif mediaType == 'tv':
    return [Media(rowMedia['name'], rowMedia['popularity']) for rowMedia in content]
  else:
    raise ArgumentError("Invalid media type")
 