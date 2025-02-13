# (modified prob3-b)

import sqlite3

# Connect to the database
conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()

# Create the ADVENTURE_TRIP table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS ADVENTURE_TRIP (
        TRIP_ID INTEGER PRIMARY KEY,
        TRIP_NAME VARCHAR(100),
        START_LOCATION TEXT,
        STATE TEXT,
        DISTANCE NUMBER,
        MAX_GRP_SIZE NUMBER,
        SEASON TEXT,
        TRIP_GUIDE_ID INTEGER,
        FOREIGN KEY (TRIP_GUIDE_ID) REFERENCES GUIDE (GUIDE_ID)
    );
""")

# Commit the changes
conn.commit()

# Describe the layout and characteristics of the ADVENTURE_TRIP table
cursor.execute("PRAGMA table_info(ADVENTURE_TRIP);")
table_info = cursor.fetchall()

# Print the table information
print("Table format:")
for column in table_info:
    print(column)

# Check if the row already exists
cursor.execute("SELECT COUNT(*) FROM ADVENTURE_TRIP WHERE TRIP_ID = 45;")
if cursor.fetchone()[0] == 0:
    # Insert a row into the ADVENTURE_TRIP table
    cursor.execute("""
        INSERT INTO ADVENTURE_TRIP (TRIP_ID, TRIP_NAME, START_LOCATION, STATE, DISTANCE, MAX_GRP_SIZE, SEASON, TRIP_GUIDE_ID)
        VALUES (45, 'Jay Peak', 'Jay', 'VT', 8, 8, 'Summer', NULL);
    """)
    conn.commit()

# Display the contents of the ADVENTURE_TRIP table
cursor.execute("SELECT * FROM ADVENTURE_TRIP;")
rows = cursor.fetchall()

# Print the table contents
print("\nTable contents:")
for row in rows:
    print(row)

# Clear the ADVENTURE_TRIP table
cursor.execute("DELETE FROM ADVENTURE_TRIP;")
conn.commit()

# Display the contents of the ADVENTURE_TRIP table again
cursor.execute("SELECT * FROM ADVENTURE_TRIP;")
rows = cursor.fetchall()

# Print the table contents after deletion
print("\nTable contents after clearing:")
for row in rows:
    print(row)

# Close the connection
conn.close()
