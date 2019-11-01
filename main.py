from sessions import *
from methods import *
from sys import argv

def main(input):

    del input[0]
    session_obj = Session(input, "products.csv")
    
    if session_obj.type == "scan_in":
        user_obj = Scan_in(session_obj)

    elif session_obj.type == "scan_out":
        user_obj = Scan_out(session_obj)

    else:
        user_obj = Packager(session_obj)

    while True:
        user_obj.action()

def initialize_session(_type_):
    if _type_ == "scan_in":
        scan_in_session()

    if _type_ == "scan_out":
        scan_out_session()

    if _type_ == "packager":
        packager_session()

if "-h" in argv:
    print("""Positional arguments include
    Worker-Type (scan-in, scan-out, packager)
    Product-Flow (capped at 200)
    Order-Flow (capped at 200)
    Flow-Cap (off, to remove the natural limit of 200 simulated products and orders)
    
    Example: python3 main.py scan-in 50 50
    
    Example: python3 main.py scan-in 201 201 off""")

elif __name__ == "__main__":
    main(argv)
