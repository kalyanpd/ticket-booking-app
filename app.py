from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Database setup
def init_db():
    conn = sqlite3.connect("tickets.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS bookings
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT,
                  event TEXT,
                  tickets INTEGER)''')
    conn.commit()
    conn.close()

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/book', methods=['GET', 'POST'])
def book():
    if request.method == "POST":
        name = request.form['name']
        event = request.form['event']
        tickets = request.form['tickets']

        conn = sqlite3.connect("tickets.db")
        c = conn.cursor()
        c.execute("INSERT INTO bookings (name, event, tickets) VALUES (?, ?, ?)",
                  (name, event, tickets))
        conn.commit()
        conn.close()
        return redirect(url_for('success'))
    return render_template("booking.html")

@app.route('/success')
def success():
    return render_template("success.html")

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=True)

