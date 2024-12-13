from flask import Flask, render_template, request, redirect, session
import mysql.connector
import sys

app = Flask(__name__)
app.secret_key = "your_secret_key"

def get_db_connection():
        connection = mysql.connector.connect(
            host="10.2.4.30",
            user="herman",
            password="Bolla123.",
            database="cookieDB"
        )
        return connection

conn = get_db_connection()

cursor = conn.cursor()

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        mail = request.form['mail']
        password = request.form['passord']
        
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE mail = %s AND passord = %s", (mail, password))
        user = cursor.fetchone()
        conn.close()

        if user:
            session['user_id'] = user['id']
            session['user_name'] = user['navn']
            return redirect('/main')  # Send brukeren til hovedsiden
        else:
            return render_template('login.html', error="Invalid credentials")
    return render_template('login.html')

@app.route("/")
def index():
    return render_template ('index.html')

@app.route('/register')
def register():
    return render_template ('register.html')

@app.route('/registerRegister', methods=['POST'])
def registerRegister():
    try:
        input1 = request.form['navn']
        input2 = request.form['mail']
        input3 = request.form['passord']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (navn, mail, passord) VALUES (%s, %s, %s)", (input1, input2, input3))
        conn.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return "Database error occurred", 500
    finally:
        conn.close()
    return render_template('index.html')

@app.route('/tabels')
def tabels():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return "Error fetching data", 500
    finally:
        conn.close()
    return render_template('tabels.html', users=users)

@app.route('/login')
def login():
    return render_template('login.html')



@app.route("/main")
def main():
    return render_template('main.html')

if __name__ == "__main__":
    app.run(debug=True)