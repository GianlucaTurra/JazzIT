import os
from functools import cache

import spotipy
from dotenv import load_dotenv
from spotipy import SpotifyClientCredentials


def __check_environmental_variables():
    """Ensures environment variables are set correctly. TODO: is there a better way?"""
    try:
        var = os.environ['SPOTIFY_CLIENT_ID']
        var = os.environ['SPOTIFY_CLIENT_SECRET']
    except KeyError:
        load_dotenv()


@cache  # TODO: probably not the best
def get_spotify_client() -> spotipy.Spotify:
    __check_environmental_variables()
    auth_manager = SpotifyClientCredentials(
        client_id=os.environ['SPOTIFY_CLIENT_ID'],
        client_secret=os.environ['SPOTIFY_CLIENT_SECRET'],
    )
    return spotipy.Spotify(auth_manager=auth_manager)
