import re
import logging # need logging of events

import mysql.connector
import sql_config as sc

############################ CREATE (AKA: INSERT) ###############################################################################################################################
def insert_customers(conn, cur):
    pk = input("ENTER PASSKEY OF CUSTOMER: ")
    lastN = input("ENTER LAST NAME OF CUSTOMER: ")
    firstN = input("ENTER FIRST NAME OF CUSTOMER: ")
    cty = input("ENTER THE CITY OF CUSTOMER: ")
    sql_customers = "INSERT INTO customers (passkey, lastName, firstName, city) VALUES (%s, %s, %s, %s)"
    val_customers = (pk, lastN, firstN, cty)
    print(cur.rowcount, "Record inserted into TABLE customers")
    cur.execute(sql_customers, val_customers)
    conn.commit()
    logging.info("Inserted new info into TABLE customers")

def insert_orders(conn, cur):
    pro = input("ENTER THE PRODUCE BEING BOUGHT: ")
    lbs = input("ENTER THE NUMBER OF POUNDS OF PRODUCE ORDERED: ")
    orID = input("ENTER THE ORDER ID OF THIS TRANSACTION: ")
    sql_orders = "INSERT INTO orders (produce, lbsOrdered, orderid) VALUES (%s, %s, %s)"
    val_orders = (pro, lbs, orID)
    print(cur.rowcount, "Record inserted into TABLE orders")
    cur.execute(sql_orders, val_orders)
    conn.commit()
    logging.info("Inserted new info into TABLE orders")

def insert_history(conn, cur):
    date = input("PLEASE ENTER THE DATE OF PRODUCT TRANSACTION (in YYYY-MM-DD format please): ")
    orID = input("ENTER THE ORDER ID OF THIS TRANSACTION: ")
    pk = input("ENTER PASSKEY OF TRANSACTION FROM CUSTOMER'S ORDER: ")
    sql_history = "INSERT INTO orderHistory (dt, orderid, passkey) VALUES (%s, %s, %s)"
    val_history = (date, orID, pk)
    print(cur.rowcount, "Record inserted into TABLE orderHistory")
    cur.execute(sql_history, val_history)
    conn.commit()
    logging.info("Inserted new info into TABLE ordersHistory")

############################################# READ (AKA: SELECT, aka show results) ##############################################################################################
def read_customers(cursor):
    cursor.execute("SELECT * FROM customers")
    fetch = cursor.fetchall()

    print("passkey      lastName        firstName       city")
    print("-------------------------------------------------")
    for item in fetch:
        print(str(item[0])+"    "+item[1]+"    "+item[2]+"     "+item[3])
    logging.info("SHOWED ALL AVAILABLE QUERIES WITHIN TABLE customers")

def read_orders(cursor):
    cursor.execute("SELECT * FROM orders")
    fetch = cursor.fetchall()

    print("produce      lbsOrdered        orderid")
    print("--------------------------------------")
    for item in fetch:
        print(str(item[0])+"    "+str(item[1])+"    "+str(item[2]))
    logging.info("SHOWED ALL AVAILABLE QUERIES WITHIN TABLE orders")


def read_history(cursor):
    cursor.execute("SELECT * FROM orderHistory")
    fetch = cursor.fetchall()

    print("dt      orderid        passkey")
    print("------------------------------")
    for item in fetch:
        print(str(item[0])+"    "+str(item[1])+"    "+str(item[2]))
    logging.info("SHOWED ALL AVAILABLE QUERIES WITHIN TABLE orderHistory")



################################################ UPDATE QUERIES ################################################################################################################
def update_customers(conn, cur):
    print("BE SURE TO INSERT MATCHING PASSKEY (to work) HERE")
    pk = input("ENTER PASSKEY OF CUSTOMER: ")
    lastN = input("ENTER LAST NAME OF CUSTOMER: ")
    firstN = input("ENTER FIRST NAME OF CUSTOMER: ")
    cty = input("ENTER THE CITY OF CUSTOMER: ")
    sql_customers = "UPDATE customers SET lastName= %s, firstName= %s, city= %s WHERE passkey = %s"
    val_customers = (lastN, firstN, cty, pk)

    cur.execute(sql_customers, val_customers)
    conn.commit()
    print(cur.rowcount, "UPDATED customers RECORD")
    logging.info("UPDATED customers TABLE")

def update_orders(conn, cur):
    print("BE SURE TO INSERT MATCHING ORDER_ID (to work) HERE")
    pro = input("ENTER PRODUCE TYPE: ")
    lbs = input("ENTER POUNDS OF PRODUCE: ")
    orID = input("ENTER ORDER_ID OF CUSTOMER: ")
    sql_orders = "UPDATE customers SET produce= %s, lbsOrdered= %s WHERE orderid = %s"
    val_orders = (pro, lbs, orID)

    cur.execute(sql_orders, val_orders)
    conn.commit()
    print(cur.rowcount, "UPDATED orders RECORD")
    logging.info("UPDATED orders TABLE")

def update_history(conn, cur):
    print("BE SURE TO INSERT MATCHING PASSKEY + ORDER_ID (to work) HERE")
    date = input("ENTER DATE (YYYY-MM-DD FORMAT): ")
    orID = input("ENTER ORDER_ID: ")
    pk = input("ENTER PASSKEY: ")
    sql_orders = "UPDATE orderHistory SET produce= %s, lbsOrdered= %s WHERE orderid = %s"
    val_orders = (date, orID, pk)

    cur.execute(sql_orders, val_orders)
    conn.commit()
    print(cur.rowcount, "UPDATED orderHistory RECORD")
    logging.info("UPDATED orderHistory TABLE")


###################################################### DELETE QUERIES FROM TABLES #############################################################################################
def delete_customers(conn, cur):
    pk = input("ENTER THE PASSKEY TO DELETE: ")

    sql_customer = "DELETE FROM customers WHERE passkey = '"+pk+"'"
    cur.execute(sql_customer)
    conn.commit()
    print(cur.rowcount, "DELETED RECORD ASSOCIATED WITH PASSKEY")
    logging.info("PASSKEY + ASSOCIATED ROW DELETED")

def delete_orders(conn, cur):
    orID = input("ENTER THE ORDER_ID TO DELETE: ")

    sql_order = "DELETE FROM orders WHERE passkey = '"+orID+"'"
    cur.execute(sql_order)
    conn.commit()
    print(cur.rowcount, "DELETED RECORD ASSOCIATED WITH ORDER_ID")
    logging.info("ORDER_ID + ASSOCIATED ROW DELETED")

def delete_history(conn, cur):
    pk = input("ENTER THE PASSKEY TO DELETE: ")
    orID = input("ENTER THE ORDER_ID TO DELETE: ")

    sql_history = "DELETE FROM orderHistory WHERE passkey = '"+pk+"' AND orderid = '"+orID+"'"
    cur.execute(sql_history)
    conn.commit()
    print(cur.rowcount, "DELETED RECORD ASSOCIATED WITH PASSKEY AND ORDER_ID")
    logging.info("PASSKEY AND ORDER_ID + ASSOCIATED ROW DELETED")


############################################# MAIN CONNECTION SECTION ##########################################################################################################
def main(): # Including login
    logging.basicConfig(filename="grocerLog.log", level=logging.DEBUG, format='%(asctime)s :: %(message)s')

    conn = mysql.connector.connect(
        host = sc.host,
        database = sc.database,
        user = sc.user,
        password = sc.password
    )
    logging.info("Logging into the database, set pre-requisites by config file")

    cursor = conn.cursor()


    choice = 0
    while (choice <= 12):

        print("1. INSERT INTO customers")
        print("2. INSERT INTO orders")
        print("3. INSERT INTO orderHistory")

        print("\n4. READ customers")
        print("5. READ orders")
        print("6. READ orderHistory")

        print("\n7. UPDATE customers")
        print("8. UPDATE orders")
        print("9. UPDATE orderHistory")

        print("\n10. DELETE from customers")
        print("11. DELETE from orders")
        print("12. DELETE from orderHistory")

        print("13. EXIT")

        choice = int(input("Enter your choice from the given numbers 1 - 13: "))

        if (choice == 1):
            insert_customers(conn, cursor)
        elif (choice == 2):
            insert_orders(conn, cursor)
        elif (choice == 3):
            insert_history(conn, cursor)
        elif (choice == 4):
            read_customers(cursor)
        elif (choice == 5):
            read_orders(cursor)
        elif (choice == 6):
            read_history(cursor)
        elif (choice == 7):
            update_customers(conn, cursor)
        elif (choice == 8):
            update_orders(conn, cursor)
        elif (choice == 9):
            update_history(conn, cursor)
        elif (choice == 10):
            delete_customers(conn, cursor)
        elif (choice == 11):
            delete_orders(conn, cursor)
        elif (choice == 12):
            delete_history(conn, cursor)
        else:
            exit()

if __name__ == "__main__":    
    main()