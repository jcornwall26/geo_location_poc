from geo import GeoStore


def test_geo_store():
    store = GeoStore(None, None)
    assert store is not None
