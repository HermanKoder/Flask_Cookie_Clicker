from flask import Flask, render_template, request, redirect, session
import mysql.connector

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
            return redirect('/main')
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
    input1 = request.form['navn']
    input2 = request.form['mail']
    input3 = request.form['passord']
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (navn, mail, passord) VALUES (%s, %s, %s)", (input1, input2, input3))
    conn.commit()
    conn.close()
    return render_template('index.html')

@app.route('/tabels')
def tabels():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    conn.close()
    return render_template('tabels.html', users=users)

@app.route('/main')
def main():
    if 'user_id' not in session:
        return redirect('/login')

    user_id = session['user_id']
    user_name = session['user_name']

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM cookieScore WHERE user_id = %s", (user_id,))
    score = cursor.fetchone()

    if not score:
        cursor.execute("INSERT INTO cookieScore (cookies, user_id) VALUES (%s, %s)", (0, user_id))
        conn.commit()
        score = {'cookies': 0}

    conn.close()
    return render_template('main.html', user_name=user_name, cookies=score['cookies'])



if __name__ == "__main__":
    app.run(debug=True)