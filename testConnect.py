import re
import logging # need logging of events

import mysql.connector
import sql_config as sc

conn = mysql.connector.connect(
    host = sc.host,
    database = sc.database,
    user = sc.user,
    password = sc.password
)

cursor = conn.cursor()
cursor.execute("SELECT * FROM customers")

for row in cursor:
    print(row)