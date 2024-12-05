import mysql.connector

mydb = mysql.connector.connect(
    host=""
    user=""
    password=""
)

mycursor = mydb.cursor()

mycursor.execute('''hiuoijpo''')

resultat = mycursor.fetchall()

return resultat

