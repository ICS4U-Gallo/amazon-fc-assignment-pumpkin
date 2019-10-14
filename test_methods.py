from methods import *
import pytest

def test_pull_product_from_json():
    test_input = {
        "00001": {
            "name": "Razor",
            "id": "00001",
            "dimensions": [5, 5, 10]}}

    excpected = test_input["00001"]

    assert pull_product_from_json("00001", test_input) = expected

def test_scan_product_into_shelf():
    shelf_obj = Shelf()
    test_input = {"name": "Razor",
            "id": "00001",
            "dimensions": [5, 5, 10]}

    scan_product_into_shelf(test_input, shelf_obj)

    assert  shelf_obj.items[0] == test_input

def test_remove_product_from_shelf():
    shelf_obj = Shelf()
    test_input = {"name": "Razor",
            "id": "00001",
            "dimensions": [5, 5, 10]}
    shelf_obj.append(test_input)

def test_
