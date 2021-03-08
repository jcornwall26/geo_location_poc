from geo import GeoStore
import os
import sys


def test_geo_store():
    print('Looking for modules in:')
    print('\n'.join(sys.path))
    ...
    #store = GeoStore(None, None)
    assert store is not None

if __name__ == "__main__":
    print('Looking for modules in:')
    print('\n'.join(sys.path))
    print(os.environ['TEST'])
    ...