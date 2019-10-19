from typing import List
import random
import json
import csv

class Shelf:
    def __init__(self):

        self.items = []

def generate_random_order(batch_size: int) -> list:
    """This function generates a random order

    Args:
        Batch size for order generation

    Returns:
        A list of ordered products 
        """
    
    first_names = ["Ryan","Sydney", "Joe", "Mehana", "Daniel", "John"]
    last_names = ["Smith", "Johnson", "Edwards", "Kim", "Low"]

    street_names = ["Leslie", "6th Avenue", "Finch", "Bayview", "College", "Major Mackenzie"]
    
    rtn_ar = []

    for _ in range(batch_size):
        rtn_dict = {"first_name": first_names[random.randint(len(first_names))],
                "last_name": last_names[random.randint(len(last_names))],
                "street": street_names[random.randint(len(street_names))],
                "street_number": random.randint(0,100)}
        
        rtn_ar.append(rtn_dict)

    return rtn_ar

def gererate_random_shippment(batch_size: int, product_json_name: str) -> list:
    """This function generates a random incoming shippment

    Args:
        Batch size for shippment generation
        produt_json_name, the file name with which all products are stored in json format

    Returns:
        A list of inbound products
        """
    
    inbound_products = []

    for _ in range(batch_size):

        with open(product_json_name) as _file:
        
            data = csv.reader(_file)

            inbound_product.append(data[random.randint(len(_file))])

    return inbound_products

def add_product_into_shelf(product_dictionary: dict, shelf_obj: object) -> None: # Joe
    """Adds a product dictionary to a shelf_obj
    Args:
        product_dictionary, a dictionary in the form of the dict created in create_product_dict
        shelf_obj, the shelf class-object add to the list of items via shelf_obj.items.append(______)
    Returns:
        None
        """

    pass

def compare_shelf_against_orders(target_id: str, shelf_obj: object, orders: list) -> dict:
    """Search through the list of customer orders, and compare it against the current availble shelf (shelf_obj.items)
    Args:
        target_id, a string that corosponds to a product dictionary key (ie: product_dictionary["Product_id"])
        shelf_obj, the shelf object that contains the item list for the current shelf at the employee station
        orders, a list of all available customer orders
    Returns:
        product_dict, the current employee target product that should be taken out
        """

    pass

def remove_product_from_shelf(target_index: int, shelf_obj: object) -> None:
    """After an employee is told to take a product out of a shelf, it has to be removed from the list as it is no longer physically there
    Args:
        target_index, representing the index of the product targeted for deletion within the shelf_obj.items list
        shelf_obj, the class-object that contains the shelf_obj.items list that needs to be removed from.
    Returns:
        None
        """

    pass

def send_to_packaging(product_dict: dict, order_info: dict) -> dict:
    """After a product is removed from the shelf it needs to be packaged and shipped.
    Args:
        product_dict, a dictionary that contains the information about the product
        order_info, a dictionary that contains the information about the order
    
    Returns:
        a dictionary containing, product dimensions, recipient information.
        """
    
    pass

def display_packaging_specs(packaging_info_dict: dict):
    """After the item is taken off the shelf, and a certain order is began the last steps are shipping and packaging
    The function recieves bundles info from the 'send_to_packing' function and then formats the info in a return statment
    for easy GUI implementation"""

    product_info = packaging_info_dict["dimensions"]
    order_info = packaging_info_dict["order_info"]

    pass
