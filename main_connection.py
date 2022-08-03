import re
import logging

#### SET UP SQL CONNECTION HERE ##############################################################################################################################################
import mysql.connector
import sql_config as sc

def main():
    # Actually trying to connect the sql server

    try:
        connection = mysql.connector.connect(user=sc.user, password = sc.password, host = sc.host, port = sc.port, database = sc.database)    
        cur = connection.cursor()
    
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
            create(connection, cur)
            logging.info("SELECTED CREATE/INSERT OPTION")
        elif (choice == 2):
            read(cur)
            logging.info("SELECTED READ OPTION")
        elif (choice == 3):
            update(connection, cur)
            logging.info("SELECTED UPDATE OPTION")
        elif (choice == 4):
            delete(connection, cur)
            logging.info("SELECTED DELETE OPTION")
        else:
            quit()


def create(connection, cur): # TECHNICALLY INSERT BY SQL STANDARDS ##########################################################################################################
    print("\n**************************** For TABLE customers *************************") # TABLE 1
    pk = input("\nEnter customer passkey: ")
    lastN = input("\nEnter customer's last name: ")
    firstN = input("\nEnter customer's first name: ")
    addres = input("\nEnter customer's address: ")
    cty = input("\nEnter customer's city: ")
    # For TABLE customers
    sql_customers = "\nINSERT INTO customers (passkey, lastname, firstname, address, city) VALUES (%s, %s, %s, %s, %s)"
    val_customers = (pk, lastN, firstN, addres, cty)
    
    print("\n****************** For TABLE orders *********************************") # TABLE 2
    prod = input("\nEnter the produce ordered: ")
    lbs = input("\nEnter number of lbs ordered: ")
    totPrice = input("\nEnter total value of transaction: ")
    order = input("\nEnter the ID of order: ")
    # For TABLE customers
    sql_orders = "\nINSERT INTO orders (produce, lbsOrdered, totalPrice, orderid) VALUES (%s, %f, %f, %d)"
    val_orders = (prod, lbs, totPrice, order)

    print("\n****************** For TABLE orderHistory *********************************") # TABLE 3
    date = input("\nEnter customer passkey: ")
    orderH = input("\nEnter customer's last name: ")
    pkH = input("\nEnter customer's first name: ")
    # For TABLE customers
    sql_history = "\nINSERT INTO orders (purchase_date, orderid, passkey) VALUES (%d, %d, %s)" # ASK ABOUT THIS SINCE THIS TABLE HAS FOREIGN KEYS
    val_history = (date, orderH, pkH)

    
    # EXECUTE THE QURIES
    cur.execute(sql_customers, val_customers)
    cur.execute(sql_orders, val_orders)
    cur.execute(sql_history, val_history)
    

    connection.commit()
    
    logging.info("INSERTED INTO ALL 3 TABLES, NEED A WAY TO FIND SEPEARTION.")





def read(cur): # SELECT: Seletct data from tables ##############################################################################################################
    cur.execute("SELECT * FROM customers")
    cur.execute("SELECT * FROM orders")
    cur.execute("SELECT * FROM orderHistory")    

    res = cur.fetchall()

    print("/n   passkey   lastname    firstname   address     city")
    for x in res:
        print(str(x[0])+"  "+x[1]+"  "+x[2]+"  "+x[5]+"  "+x[3]+"  "+x[4])
    print("/n   produce    lbsOrdered   totalPrice     orderid")
    print("/n   purchase_date    orderid    passkey")





def update(connect, cur):
    


# call main
    if __name__ == "__main__":
        main()

