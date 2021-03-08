import csv
import os
import sys
import geo

from typing import List

input_csv = f'{os.path.dirname(__file__) or "./"}/input.csv'
#output_csv = f'{os.path.dirname(__file__)}/output.csv'
output_csv = '/mnt/ram/output.csv'

api_key = "d54234f9b3b1ddf124c70cf33484e139"

def log_response_type(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'{func.__name__} is returning a {type(result)}')
        return result
    return wrapper


@log_response_type
def geo_locate_stores():
    # for all the stores geo code them
    geo_code_results = perform_geo_coding(stores_to_geo_code())

    # send the stores to the output location (in this case it's a CSV file)
    put_stores_to_output(geo_code_results)


@log_response_type
def stores_to_geo_code():
    with open(input_csv, newline='') as csvfile:
        store_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        next(csvfile)  # ignore header
        for r in store_reader:
            yield create_store_from_csv(r)


def create_store_from_csv(csv_row):
    return {
        "store": csv_row[0],
        "address": csv_row[1]
    }


@log_response_type
def perform_geo_coding(stores_to_geo_code) -> List[geo.GeoStore]:
    geo_code_results = [geo.create_geo_coded_store(store) for store in stores_to_geo_code]
    return geo_code_results


def put_stores_to_output(geo_code_results: List[geo.GeoStore]):
    store = geo_code_results[0]
    ...


if __name__ == "__main__":
    print('Looking for modules in:')
    print('\n'.join(sys.path))
    geo_locate_stores()
