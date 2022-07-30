import re
import logging

#### SET UP SQL CONNECTION HERE ##############################################################################################################################################
import mysql.connector
import sql_config as sc

def main():
    # Actually trying to enter into the sql server

    try:
        connection = mysql.connector.connect(user=sc.user, password = sc.password, host = sc.host, database = "grocermarket")
        
        cursor = connection.cursor()
    
    except mysql.connector.Error as mce:
        print(mce.msg)
        return
    
    logging.basicConfig(filename = "grocerLog.log", level = logging.DEBUG, format='%(asctime)s :: %(message)s')
