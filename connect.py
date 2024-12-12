import mysql.connector as mariadb

mariadb_connection = mariadb.connect(user='test', password='password', host = 'localhost', port='3306')

create_cursor = mariadb_connection.cursor()

