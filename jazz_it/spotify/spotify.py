from dataclasses import dataclass

import spotipy
from spotipy import SpotifyClientCredentials
from dotenv import load_dotenv
import os


load_dotenv()

auth_manager = SpotifyClientCredentials(
    client_id=os.environ['SPOTIPY_CLIENT_ID'],
    client_secret=os.environ['SPOTIPY_CLIENT_SECRET'],
)
sp = spotipy.Spotify(auth_manager=auth_manager)

search = sp.search(q="track%3ACrazy%2520Train%2520artist%3AOzzy%2520Osbourne", limit=1)


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


track = SpotifyTrack(
    name=search["tracks"]["items"][0]["name"],
    artist=SpotifyArtist(
        search["tracks"]["items"][0]["artists"][0]["name"],
        search["tracks"]["items"][0]["artists"][0]["id"],
    ),
    album=SpotifyAlbum(
        search["tracks"]["items"][0]["album"]["name"],
        search["tracks"]["items"][0]["album"]["id"],
        search["tracks"]["items"][0]["album"]["images"][1]["url"],
    ),
    id=search["tracks"]["items"][0]["id"],
    preview_url=search["tracks"]["items"][0]["preview_url"],
)
