import pytest

from spotify_api.service.spotify import url_q_creation


def test_url_q_creation():
    assert url_q_creation("Crazy Train", "Ozzy Osbourne") == "track%3ACrazy%2520Train%2520artist%3AOzzy%2520Osbourne"
