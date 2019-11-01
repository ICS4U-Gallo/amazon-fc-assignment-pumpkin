from methods import *
import sys

class Session:

    def __init__(self, init_args, product_csv_filename):
        
        self.prod_filename = product_csv_filename

        self.appropriate_args = [
            ["scan-in","scan-out","packager"],
            [list(range(200))],
            [list(range(200))],
            ["off"]
        ]

        #Checking the given arguments for correctness
        
        if len(init_args) < 3:
            print("You have not entered the correct fields, type python3 main.py -h")
            sys.exit()

        if len(init_args) == 3:
            
            try:
                init_args[1] = int(init_args[1])
                init_args[2] = int(init_args[2])

            except:
                    print("You have not entered the correct fields, type python3 main.py -h")
                    sys.exit()

            for i in range(len(init_args)):
                if init_args[i] not in self.appropriate_args[i]:
                    print("You have not entered the correct fields, type python3 main.py -h")
                    sys.exit()
            
            else:
                self.type = init_args[0]
                
                if init_args[1] < 200:
                    self.products = init_args[1]
                else:
                    self.products = 200
                
                if init_args[2] < 200:
                    self.orders = init_args[2]
                else:
                    self.orders = 200

        if len(init_args) == 4:

            try:
                init_args[1] = int(init_args[1])
                init_args[2] = int(init_args[2])

            except:
                    print("You have not entered the correct fields, type python3 main.py -h")
                    sys.exit()

            for i in range(len(init_args)):
                if init_args[i] not in self.appropriate_args[i] and init_args[2]:
                    print("You have not entered the correct fields, type python3 main.py -h")
                    sys.exit()
            
            else:
                self.type = init_args[0]
                self.products = init_args[1]
                self.orders = init_args[2]

        if len(init_args) > 4:
            print("You have not enterd the correct fields, type python3 main.py -h")
            sys.exit()


class Scan_in:
    def __init__(self, session_obj):

        self.sess = session_obj

        self.inbound_shipments = []
        gererate_random_shipment(self.sess.products, self.inbound_shipments, self.sess.prod_filename)

        self.shelves = []
        generate_empty_shelves(100, self.shelves)

        self.interactions = 0

        self.thresh = 5

    def update(self):
        gererate_random_shipment(self.sess.products, self.inbound_shipments, self.sess.prod_filename)

    def action(self):
        self.interactions += 1

    def check_update_thresh(self):
        
        if len(self.inbound_shipments) <= self.thresh:
            return True
        
        else:
            return False

    def gen_exit_report(self):

        print(f"{self.interactions} items have been shelved.....")

class Scan_out:

    def __init__(self, session_obj):

        self.sess = session_obj

        self.to_be_packaged = []
        generate_random_order(self.to_be_packaged, 10, self.sess.prod_filename)

        self.shelves = []
        generate_empty_shelves(100, self.shelves)

        fill_shelves_randomly(self.shelves, self.sess.prod_filename,2)

    def update(self):
        fill_shelves_randomly(self.shelves,self.sess.prod_filename,1)

    def action(self):
        pass

    def check_update_thresh(self):
        pass

    def gen_exit_report(self):
        print(f"{len(self.to_be_packaged)} items have been proccesed for shipping.....")

class Packager:

    def __init__(self, session_obj):

        self.sess = session_obj

        self.completed_parcels = []

        self.inbound_trolley = []

        gererate_random_shipment(self.sess.products, self.inbound_trolley, self.sess.prod_filename)

    def update(self):

        generate_random_shipment(self.sess.products, self.inbound_trolley, self.ses.prod_filename)

    def action(self):
        pass

    def check_update_thresh(self):
        pass

    def gen_exit_report(self):
        print(f"{len(self.completed_parcels)} items were shipped out.....")
