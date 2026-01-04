from flask import Flask, render_template, request
import sqlite3
from datetime import datetime
import scraper  # <--- Imports your new honest bot

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('fitness_data.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    conn.execute('''CREATE TABLE IF NOT EXISTS expenses 
                   (id INTEGER PRIMARY KEY, date TEXT, item_name TEXT, price REAL, protein_grams REAL)''')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def home():
    conn = get_db_connection()
    
    # 1. LEFT TABLE: Daily Totals (Aggregation)
    cursor = conn.execute('''
        SELECT substr(date, 1, 10) as day, SUM(protein_grams) as total_protein 
        FROM expenses 
        GROUP BY day 
        ORDER BY day DESC 
        LIMIT 10
    ''')
    daily_stats = cursor.fetchall()
    
    # 2. RIGHT TABLE: Recent Logs
    cursor = conn.execute("SELECT * FROM expenses ORDER BY date DESC LIMIT 5")
    recent_data = cursor.fetchall()
    conn.close()
    
    # 3. GET PRICES & STATUS (The New Logic)
    # We unpack the tuple: price goes to variable 1, status goes to variable 2
    egg_price, egg_live = scraper.get_market_price("egg")
    chicken_price, chicken_live = scraper.get_market_price("chicken")
    
    # System Status is "Live" only if BOTH connections worked
    system_status = egg_live and chicken_live
    
    return render_template('index.html', 
                           daily_stats=daily_stats,
                           expenses=recent_data, 
                           egg_price=egg_price,
                           chicken_price=chicken_price,
                           is_live=system_status) # <--- Sending the truth to the UI

@app.route('/add', methods=['POST'])
def add_entry():
    try:
        item = request.form['item']
        price = float(request.form['price'])
        protein = float(request.form['protein'])
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        conn = get_db_connection()
        conn.execute("INSERT INTO expenses (date, item_name, price, protein_grams) VALUES (?, ?, ?, ?)", 
                     (date, item, price, protein))
        conn.commit()
        conn.close()
    except ValueError:
        pass
    return home()

if __name__ == '__main__':
    app.run(debug=True)