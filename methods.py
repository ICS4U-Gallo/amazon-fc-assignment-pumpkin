from typing import List
import random
import csv

class Shelf:
    def __init__(self):

        # A shelf has 4 faces that can hold items
        # Each cubby is a 2-D list (think spreadsheets)
        # [Rows][columns] --> a list of items in that cubby slot

        self.cubby_face0 = [[[],[],[],[]], [[],[],[],[]], [[],[],[],[]], [[],[],[],[]]]
        self.cubby_face1 = [[[],[],[],[]], [[],[],[],[]], [[],[],[],[]], [[],[],[],[]]]
        self.cubby_face2 = [[[],[],[],[]], [[],[],[],[]], [[],[],[],[]], [[],[],[],[]]]
        self.cubby_face3 = [[[],[],[],[]], [[],[],[],[]], [[],[],[],[]], [[],[],[],[]]]

class Item:
    def __init__(self, id_, name, dimensions):

        self.id = id_
        self.name = name
        self.dimensions = dimensions

def generate_random_order(target_ar: list, batch_size: int, product_csv_name: str) -> list:
    """This function generates a random order list of length 'batch_size'
    Args:
        Batch size for order generation
        Product_csv_name, the name of the csv file.
    Returns:
        A list of ordered products 
        """
    
    first_names = ["Ryan","Sydney", "Joe", "Mehana", "Daniel", "John"]
    last_names = ["Smith", "Johnson", "Edwards", "Kim", "Low"]

    street_names = ["Leslie", "6th Avenue", "Finch", "Bayview", "College", "Major Mackenzie"]

    with open(product_csv_name) as _file:
        
        num_of_products = len(_file)

        for _ in range(batch_size):
            rtn_dict = {"first_name": first_names[random.randint(len(first_names))],
                    "last_name": last_names[random.randint(len(last_names))],
                    "street": street_names[random.randint(len(street_names))],
                    "street_number": random.randint(0,100),
                    "product_id": _file[random.randint(1, num_of_products)][1]}
        
        target_ar.append(rtn_dict)

def fill_shelves_randomly(shelves: List[object], product_csv_name: str, items_per_cubby: int) -> None:
    """For simulation purposes fill Shelve object with random products.

    Args:
        A list of empty Shelve objects.
        the name of the csv file with all possible products.
        items_per_cubby is the number of items added to the cubbies
    """

    for _ in range(items_per_cubby):
        with open(product_csv_name) as _file:

            data = csv.reader(_file)    

            for shelve in shelves:
            
                rand_row = data[random.randint(1, len(data))]

                name = rand_row[0]        
                id = rand_row[1]
                dim = [rand_row[2], rand_row[3], rand_row[4]]

                rand_prod = Item( id, name, dimensions)

                add_product_into_shelf(rand_prod, shelves)

def gererate_random_shipment(batch_size: int, target_ar: list, product_csv_name: str) -> list:
    """This function generates a random incoming shippment list of length 'batch_size'
    Args:
        Batch size for shippment generation
        produt_csv_name, the file name with which all products are stored in json format
    Returns:
        A list of inbound products
        """
    
    inbound_products = target_ar

    for _ in range(batch_size):

        with open(product_csv_name) as _file:
        
            data = csv.reader(_file)

            rand_row = data[random.randint(1, len(data))]

            item = Item(rand_row[1], rand_row[0], [rand_row[2], rand_row[3], rand_row[4]]) # id name dim 
            
            inbound_products.append(item)

    return inbound_products

def generate_empty_shelves(batch_size: int, target_ar: list) -> None:

    for i in range(batch_size):
        target_ar.append(Shelf())

def check_shelve_stock(shelves: List[object]) -> int:

    sum = 0

def add_product_into_shelf(product_obj: object, shelf_obj: object) -> None: # Joe
    """Adds a product dictionary to a shelf_obj at the least populated cubby.
    Args:
        product_obj, a object of form self.____ (id, name, dimensions) 
        shelf_obj, the shelf class-object add to the list of items via shelf_obj.cubby_face#[row][column].append(______)
    Returns:
        None
        """

    pass

def compare_shelf_against_orders(target_id: str, shelf_obj: object, orders: list) -> dict: # Henson
    """Search through the list of customer orders, and compare it against the current availble shelf (shelf_obj.items)
    Args:
        target_id, a string that corosponds to a product dictionary key (ie: product_dictionary["Product_id"])
        shelf_obj, the shelf object that contains the item list for the current shelf at the employee station
        orders, a list of all available customer orders
    Returns:
        product_dict, the current employee target product that should be taken out
        """

    pass

def remove_product_from_shelf(target_index: int, shelf_obj: object) -> None: # Mehana
    """After an employee is told to take a product out of a shelf, it has to be removed from the list as it is no longer physically there
    Args:
        target_index, representing the index of the product targeted for deletion within the shelf_obj.items list
        shelf_obj, the class-object that contains the shelf_obj.items list that needs to be removed from.
    Returns:
        None
        """

    pass

def send_to_packaging(product_obj: object, order_info: dict) -> dict: # Sydney
    """After a product is removed from the shelf it needs to be packaged and shipped.
    Args:
        product_obj, a object that contains all the product attributes
        order_info, a dictionary that contains the information about the order
    
    Returns:
        a dictionary containing, product pointer, and recipient information.
        """
    
    pass
