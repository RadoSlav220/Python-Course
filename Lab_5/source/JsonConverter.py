from source.media import Media

def convertMediaToJSON(media: Media) -> dict[str, any]:
    return {'title': media.title, 'rating': media.popularity}

def convertMediaListToJSON(mediaCollection: list[Media]) -> list[dict[str, any]]:
  return [convertMediaToJSON(media) for media in mediaCollection]