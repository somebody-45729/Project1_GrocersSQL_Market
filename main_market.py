import re
import logging

#### SET UP SQL CONNECTION HERE ##############################################################################################################################################
import mysql.connector
import sql_config as sc

def main():
    # Actually trying to connect the sql server

    try:
        connection = mysql.connector.connect(user=sc.user, password = sc.password, host = sc.host, database = sc.database)    
        cursor = connection.cursor()
    
    except mysql.connector.Error as mce:
        print(mce.msg)
        return
    
    except Exception as e:
        print("ERROR: Exiting program")
        return

    # Connection works (8/1/22 8:28 PM)
    
    logging.basicConfig(filename = "grocerLog.log", level = logging.DEBUG, format='%(asctime)s :: %(message)s')


    print("*** PRODUCE MARKET ***")

    csvName = "file.csv"

    lst_customers = load_customer_db(cursor)

    logging.info("Loading customer info into lst_cusotmers")

    lst_orders = load_order_db(cursor)

    logging.info("Loading order info into lst_orders")