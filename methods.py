from typing import List
import random


class Shelf:

    def __init__(self):

        items = []


def init_shelfs(shelf_list, batch_size):

    for _ in range(batch_size):
        shellf_list.append(Shelf())

def create_product_dict(product_id: str, product_name: str, product_dimensions: list) -> dict: # Joe
    """Creates a dictionary to store a specific products information
    
    Args:
        Product_id, as a string ie: 0000193
        Product_name, as a string ie: Gillet Razor
        Product_dimensions, a list of form: [length, width, height]
        
    Returns:
        Dictonary
        """
    pass

def pull_product_from_csv(row: int, file: object):
    """From a local csv read a single product information row, and return it's information.

    Args:
        file, a file object of format csv
        row, the row of the desired product

    Returns:
        a batch return of....... product_id, product_name, product_dimensions
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

def generate_random_orders(products_filename, orders_list):

    with open(products_filename) as csv_file:

        id, name, dimensions = pull_product_from_csv(random.randint(0, len(csv_file)), csv_file) # Randomly select a product to order
        product_dict = create_product_dict(id, name, dimensions)

        orders_list.append(product_dict)

orders = []
shelf_obj_list = []

init_shelfs(10)

shelf_loading_stations = 5
shelf_unloading_stations = 5

order_packaging_stations = 5

while True:

    for _ in range(random.randint(0,5)): # 0-5 random products will be ordered
        generate_random_orders("products.csv", orders)

    
    for _ in range(shelf_loading_stations):
        scan_product_into_shelf(product_dict, shelf_obj_list[random.randint(0,len(shelf_obj_list))]) # Add the current product into a randomly selected shelf
