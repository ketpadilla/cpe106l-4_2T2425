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
for column in table_info:
    print(column)

# Close the connection
conn.close()
