import re
import logging # need logging of events

import mysql.connector
import sql_config as sc

############################ INSERT ###############################################################################################################################
def insert(conn, cur):
    pk = input("ENTER PASSKEY OF CUSTOMER: ")
    lastN = input("ENTER LAST NAME OF CUSTOMER: ")
    firstN = input("ENTER FIRST NAME OF CUSTOMER: ")
    cty = input("ENTER THE CITY OF CUSTOMER: ")
    sql_customers = "INSERT INTO customers (passkey, lastName, firstName, city) VALUES (%s, %s, %s, %s)"
    val_customers = (pk, lastN, firstN, cty)
   # cur.execute(sql_customers, val_customers)
    print(cur.rowcount, "Record inserted into TABLE customers")

    pro = input("ENTER THE PRODUCE BEING BOUGHT: ")
    lbs = input("ENTER THE NUMBER OF POUNDS OF PRODUCE ORDERED: ")
    orID = input("ENTER THE ORDER ID OF THIS TRANSACTION: ")
    sql_orders = "INSERT INTO orders (produce, lbsOrdered, orderid) VALUES (%s, %f, %d)"
    val_orders = (pro, lbs, orID)
    #cur.execute(sql_orders, val_orders)
    print(cur.rowcount, "Record inserted into TABLE orders")

    cur.execute(sql_customers, val_customers, sql_orders, val_orders)
    conn.commit()


def main():

    conn = mysql.connector.connect(
        host = sc.host,
        database = sc.database,
        user = sc.user,
        password = sc.password
    )
    logging.info("Logging into the database, set pre-requisites by config file")

    cursor = conn.cursor()
    choice = 0

    while (choice <= 4):

        print("1. INSERT")
        print("2. READ")
        print("3. UPDATE")
        print("4. DELETE")
        print("5. EXIT")

        choice = int(input("Enter your choice: "))
        if (choice == 1):
            insert(conn, cursor)
        elif (choice == 2):
            read(cursor)
        elif (choice == 3):
            update(conn, cursor)
        elif (choice == 4):
            delete(conn, cursor)
        else:
            exit()

    
main()