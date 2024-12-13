from flask import Flask, render_template, request
import mysql.connector
import sys


app = Flask(__name__)

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host="10.2.4.30",
            user="herman",
            password="Bolla123.",
            database="cookieDB"
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        sys.exit(1)

    
conn = get_db_connection()

cursor = conn.cursor()

@app.route("/")
def index():
    return render_template ('index.html')

@app.route('/register', methods=['POST'])
def register():
    input1 = request.form['name']
    input2 = request.form['email']
    input3 = request.form['password']
 
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Brukere (username, email, password) VALUES (%s, %s, %s)", (input1, input2, input3)))
    conn.commit()
    conn.close()
   
    return render_template('register.html')

@app.route('/login')
def login():
    return render_template('login.html')



@app.route("/main")
def main():
    return render_template('main.html')

if __name__ == "__main__":
    app.run(debug=True)