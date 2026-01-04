import sqlite3

def inject_fake_history():
    # Connect to your database
    conn = sqlite3.connect('fitness_data.db')
    cursor = conn.cursor()

    # --- STEP 1: CLEAR OLD DATA ---
    # We wipe the table first so you don't have messy duplicates.
    # Your table will be clean and look perfect.
    cursor.execute("DELETE FROM expenses")
    print("🗑️  Old data wiped...")

    # --- STEP 2: THE FAKE DATA ---
    # We explicitly type the dates as STRINGS in the past (YYYY-MM-DD)
    # This simulates you using the app for the last 3 days.
    
    fake_meals = [
        # TODAY (Jan 04) - A good protein day
        ('2026-01-04 08:30:00', '3 Boiled Eggs', 21.0, 18.0),
        ('2026-01-04 13:15:00', 'Chicken Breast (200g)', 120.0, 60.0),
        ('2026-01-04 18:00:00', 'Whey Scoop', 90.0, 24.0),

        # YESTERDAY (Jan 03) - A decent day
        ('2026-01-03 09:00:00', 'Omelette (2 Eggs)', 30.0, 12.0),
        ('2026-01-03 14:00:00', 'Grilled Chicken Salad', 180.0, 40.0),
        ('2026-01-03 20:30:00', 'Soya Chunks Curry', 40.0, 25.0),

        # 2 DAYS AGO (Jan 02) - A lighter day
        ('2026-01-02 10:00:00', 'Paneer Sandwich', 45.0, 18.0),
        ('2026-01-02 21:00:00', 'Protein Shake', 90.0, 24.0),
    ]

    # --- STEP 3: INSERT IT ---
    cursor.executemany('''
        INSERT INTO expenses (date, item_name, price, protein_grams) 
        VALUES (?, ?, ?, ?)
    ''', fake_meals)

    conn.commit()
    conn.close()
    print("✅ Database successfully populated with 3 days of history!")

if __name__ == '__main__':
    inject_fake_history()