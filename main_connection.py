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
        
        if (choice == 1):
            create(connection, cursor)
        elif (choice == 2):
            read(connection, cursor)
        elif (choice == 3):
            update(connection, cursor)
        elif (choice == 4):
            delete(connection, cursor)
        else:
            quit()


def create(connection, cursor): # TECHNICALLY INSERT BY SQL STANDARDS
    print("\n**************************** For TABLE customers *************************")
    pk = input("\nEnter customer passkey: ")
    lastN = input("\nEnter customer's last name: ")
    firstN = input("\nEnter customer's first name: ")
    addres = input("\nEnter customer's address: ")
    cty = input("\nEnter customer's city: ")
    # For TABLE customers
    sql_customers = "\nINSERT INTO customers (passkey, lastname, firstname, address, city) VALUES (%s, %s, %s, %s, %s)"
    val = (pk, lastN, firstN, addres, cty)
    
    print("\n****************** For TABLE orders *********************************")
    prod = input("\nEnter the produce ordered: ")
    lbs = input("\nEnter number of lbs ordered: ")
    totPrice = input("\nEnter total value of transaction: ")
    order = input("\nEnter the ID of order: ")
    # For TABLE customers
    sql_customers = "\nINSERT INTO orders (produce, lbsOrdered, totalPrice, orderid) VALUES (%s, %f, %f, %d)"
    val = (prod, lbs, totPrice, order)

    print("\n****************** For TABLE orderHistory *********************************")
    date = input("\nEnter customer passkey: ")
    orderH = input("\nEnter customer's last name: ")
    pkH = input("\nEnter customer's first name: ")
    # For TABLE customers
    sql_customers = "\nINSERT INTO orders (purchase_date, orderid, passkey) VALUES (%d, %d, %s)"
    val = (prod, lbs, totPrice, order)





# call main
    if __name__ == "__main__":
        main()

