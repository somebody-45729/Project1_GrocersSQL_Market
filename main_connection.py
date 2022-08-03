import re
import logging

#### SET UP SQL CONNECTION HERE ##############################################################################################################################################
import mysql.connector
import sql_config as sc

def main():
    # Actually trying to connect the sql server

    try:
        connection = mysql.connector.connect(user=sc.user, password = sc.password, host = sc.host, port = sc.port, database = sc.database)    
        cursor = connection.cursor()
    
    except mysql.connector.Error as mce:
        print(mce.msg)
        return
    
    except Exception as e:
        print("ERROR: Exiting program")
        return

    # Connection works (8/1/22 8:28 PM)
    
    logging.basicConfig(filename = "grocerLog.log", level = logging.DEBUG, format='%(asctime)s :: %(message)s')

    # MENU FOR SELECTION

    choice = 0

    while (choice <= 4): # NEED TO ADD IN A MENU SELECTION
        # MENU OPTIONS (CRUD)
        print ("\nSELECT FROM THE FOLLOWING OPTIONS:")
        print("\t1) CREATE")
        print("\t2) READ")
        print("\t3) UPDATE")
        print("\t4) DELETE")
        print("\t5) EXIT")

        try:
            choice = int(input("ENTER YOUR CHOICE (1 - 5): "))
        except ValueError:
            print("Not a valid integer, please try again!")
            logging.info("User has not entered integer, retrying again . . .")



