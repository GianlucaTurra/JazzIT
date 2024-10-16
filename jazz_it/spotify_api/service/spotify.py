from dataclasses import dataclass
from pprint import pprint
from typing import List
from urllib.parse import quote_plus, quote

from spotify_api.service.authentication import get_spotify_client


# search = sp.search(q="track%3ACrazy%2520Train%2520artist%3AOzzy%2520Osbourne", limit=1)

@dataclass
class SpotifyArtist:
    name: str
    id: str


@dataclass
class SpotifyAlbum:
    name: str
    id: str
    image_url: str


@dataclass
class SpotifyTrack:
    name: str
    artist: SpotifyArtist
    album: SpotifyAlbum
    id: str
    preview_url: str


def url_q_creation(track_name: str, artist_name: str = None, album_name: str = None) -> str:
    """Apparently spotify's API requires url spaces to be double encoded if the url is meant for the q param"""
    q = quote(f"track:{quote(track_name)}")
    if artist_name is not None:
        q += f"%2520{quote(f'artist:{quote(artist_name)}')}"
    if album_name is not None:
        q += f"%2520{quote(f'album:{quote(album_name)}')}"
    return q


def search_track(track_name: str, artist_name: str = None, album_name: str = None) -> List[SpotifyTrack]:
    search_query = url_q_creation(track_name, artist_name, album_name)
    sp = get_spotify_client()
    results = sp.search(q=quote_plus(search_query), type='track', limit=5)
    output = []
    for item in results['tracks']['items']:
        found_track = SpotifyTrack(
            name=item["name"],
            artist=SpotifyArtist(
                item["artists"][0]["name"],
                item["artists"][0]["id"],
            ),
            album=SpotifyAlbum(
                item["album"]["name"],
                item["album"]["id"],
                item["album"]["images"][1]["url"],
            ),
            id=item["id"],
            preview_url=item["preview_url"],
        )
        output.append(found_track)
    return output


pprint(search_track(track_name="trains", artist_name="porcupine tree", album_name="in absentia"))
