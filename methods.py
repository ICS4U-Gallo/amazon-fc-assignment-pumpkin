from typing import List
import random


class Shelf:

    def __init__(self):

        items = []


def init_shelfs(shelf_list, batch_size):

    for _ in range(batch_size):
        shellf_list.append(Shelf())

def pull_product_from_json(id: str, file: dict):
    """From a local json read a single product information key, and return it's information.

    Args:
        file, a file object of format json
        id, the key of the desired product

    Returns:
        a dict of: product_id, product_name, product_dimensions; key value pairs
        """

    pass

def scan_product_into_shelf(product_dictionary: dict, shelf_obj: object) -> None: # Joe
    """Adds a product dictionary to a shelf_obj
    Args:
        product_dictionary, a dictionary in the form of the dict created in create_product_dict
        shelf_obj, the shelf class-object add to the list of items via shelf_obj.items.append(______)
    Returns:
        None
        """

    pass

def manage_shelf_at_employee(target_id: str, shelf_obj: object) -> dict:
    """Search through the queue of customer orders, and compare it against the current availble shelf (shelf_obj.items)
    Args:
        target_id, a string that corosponds to a product dictionary key (ie: product_dictionary["Product_id"])
        shelf_obj, the shelf object that contains the item list for the current shelf at the employee station
    Returns:
        product_dict, the current employee target product that should be taken out
        """

    pass

def display_product_compartment(target_product: dict, shelf_obj: object) -> int:
    """Notifiy the employee what compartment the target item is contained within
    Args:
        target_product, the dictionary that will be used to search, and ultimetly notifiy the employee of the appropriate location
        shelf_obj, the object that contains the shelf_obj.items list that will be searched
    
    Returns:
        The appropriate index of the shelf_obj.items list that the employee should take the product from.
        """

    pass

def remove_product_from_shelf(target_product:dict, shelf_obj: object) -> None:
    """After an employee is told to take a product out of a shelf, it has to be removed from the list as it is no longer physically there
    Args:
        target_product, a dictionary that corroponds to the item that should be removed.
        shelf_obj, the class-object that contains the shelf_obj.items list that needs to be removed from.
    Returns:
        None
        """

    pass

def send_to_packaging(product_dict: dict, order_info: dict) -> None:
    """After a product is removed from the shelf it needs to be packaged and shipped.
    Args:
        product_dict, a dictionary that contains the information about the product
        order_info, a dictionary that contains the information about the order
    
    Returns:
        None
        """
    
    pass

orders = []
shelf_obj_list = []

init_shelfs(10)

shelf_loading_stations = 5
shelf_unloading_stations = 5

order_packaging_stations = 5

while True:
   break
