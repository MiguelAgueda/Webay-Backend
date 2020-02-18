"""
Source: https://docs.python.org/2/library/sqlite3.html
This is an example implementation of a database.
In this program, a database will be initialized and filled with data.
Then, the data will be printed to the console.

Any changes to the database structure need to be committed into a new
database file. The old file will not accept changes to the structure of 
data.
"""

import sqlite3


conn = sqlite3.connect("data_files/ex_database.db")

c = conn.cursor()

try:
    # Create table
    c.execute('''CREATE TABLE listings
              (sku INTEGER, title TEXT, price REAL)''')
except sqlite3.OperationalError:
    print("Skipping Creation of database file: Already Created.")

# # Never do this -- insecure!
# some_title = 'New Blue Shoes'
# c.execute("SELECT * FROM listings WHERE title = '%s'" % some_title)

# Do this instead
# t = ('RHAT',)
# c.execute('SELECT * FROM stocks WHERE symbol=?', t)
# print(c.fetchone())

# Larger example that inserts many records at a time
list_of_listings = [(1, 'Like-New Medium Blue Socks', 10.99),
                    (2, 'Used Small Lime Green Gloves', 11.99),
                    (3, 'New Medium Navy Blue Gloves', 12.99),
                    (4, 'Like-New Extra Large Brown Hat', 13.99),
                    ]
c.executemany('INSERT INTO listings VALUES (?,?,?)', list_of_listings)


conn.commit()  # Commit changes to database file.

for row in c.execute('SELECT * FROM listings ORDER BY price'):
    print(row)

conn.close()  # Close the connection to the database.
