import re
import logging # need logging of events

import mysql.connector
import sql_config as sc

############################ INSERT ###############################################################################################################################
def insert(conn, cur):
    
























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