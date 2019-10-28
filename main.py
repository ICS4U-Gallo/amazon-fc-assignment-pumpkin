from sessions import *
from methods import *

def initialize_session(_type_):
    if _type_ == "scan_in":
        scan_in_session()

    if _type_ == "scan_out":
        scan_out_session()

    if _type_ == "packager":
        packager_session()