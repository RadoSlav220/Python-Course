from functools import reduce
from source.media import Media

def convertMediaToCSV(media: Media) -> str:
    return media.title + "," + media.popularity.__str__() 

def my_concatenate(s1: str, s2: str) -> str:
  return s1 + "\n" + s2

def convertMediaListToCSV(mediaCollection: list[Media]) -> str:
  return reduce(my_concatenate, [convertMediaToCSV(media) for media in mediaCollection], '')