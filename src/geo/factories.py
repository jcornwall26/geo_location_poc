import requests
import geo.geo_store

from http import HTTPStatus

api_key = "d54234f9b3b1ddf124c70cf33484e139"

def create_geo_coded_store(store):
    address_query = store['address']
    result = requests.get(f'http://api.positionstack.com/v1/forward?access_key={api_key}&query={address_query}')
    if result.status_code == HTTPStatus.OK:  #todo handle non-200s
        data = result.json().get('data', None)
        if data:
            print(data[0])
            return geo.GeoStore(store['store'], data[0])  #todo handle more than one result
    return None
