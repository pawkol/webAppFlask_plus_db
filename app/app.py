from flask import Flask, render_template, request, redirect
import mysql.connector
import os
import time

app = Flask(__name__)

# Funkcja nawiązywania połączenia z bazą danych
def get_db_connection():
    retries = 5
    while retries > 0:
        try:
            conn = mysql.connector.connect(
                host=os.getenv('DB_HOST', 'localhost'),
                user=os.getenv('DB_USER', 'root'),
                password=os.getenv('DB_PASSWORD', 'password'),
                database=os.getenv('DB_NAME', 'numbers_db')
            )
            return conn
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            retries -= 1
            time.sleep(5)
    raise Exception("Could not connect to the database.")

# Funkcja inicjalizująca bazę danych
def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS numbers (
            id INT AUTO_INCREMENT PRIMARY KEY,
            number INT NOT NULL
        )
    ''')
    conn.commit()
    cursor.close()
    conn.close()

@app.route('/', methods=['GET', 'POST'])
def index():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    if request.method == 'POST':
        number = request.form['number']
        cursor.execute('INSERT INTO numbers (number) VALUES (%s)', (number,))
        conn.commit()
        return redirect('/')
    
    cursor.execute('SELECT * FROM numbers')
    numbers = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', numbers=numbers)

if __name__ == '__main__':
    init_db()  # Inicjalizacja bazy danych przy starcie aplikacji
    app.run(host='0.0.0.0', port='8080', debug=True)

