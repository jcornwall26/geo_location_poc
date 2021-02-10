import csv
import functools
import geo

from logging import logger
from http import HTTPStatus
from typing import Callable, List
 
input_csv = './input.csv'
output_csv = './output.csv'

api_key = "d54234f9b3b1ddf124c70cf33484e139"

def log_response_type(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'{func.__name__} is returning a {type(result)}')
        return result
    return wrapper

@log_response_type
def geo_locate_stores():
    # get stores dict from input (in this case it's a CSV file)

    # for all the stores geo code them
    geo_code_results = perform_geo_coding(stores_to_geo_code())

    # send the stores to the output location (in this case it's a CSV file)
    put_stores_to_output(geo_code_results)

@log_response_type
def stores_to_geo_code():
    with open(input_csv, newline='') as csvfile:
        store_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        next(csvfile) # ignore header
        for r in store_reader:
            yield create_store_from_csv(r)

def create_store_from_csv(csv_row):
    return {
        "store": csv_row[0],
        "address": csv_row[1]
    }

@log_response_type
def perform_geo_coding(stores_to_geo_code):

    geo_code_results = [geo.create_geo_coded_store(store) for store in stores_to_geo_code]
    return geo_code_results

# def create_geo_coded_store(store):
#     address_query = store['address']
#     result = requests.get(f'http://api.positionstack.com/v1/forward?access_key={api_key}&query={address_query}')
#     if result.status_code == HTTPStatus.OK: #todo handle non-200s
#         data = result.json().get('data', None)
#         if data:
#             print(data[0])
#             return GeoStore(store['store'], data[0]) #todo handle more than one result

def put_stores_to_output(geo_code_results: List[geo.GeoStore]):
    for geo_store in geo_code_results:
        ...


if __name__ == "__main__":
    geo_locate_stores()