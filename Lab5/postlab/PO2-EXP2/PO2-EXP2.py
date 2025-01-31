import sqlite3
import os

DATABASE_FILE = os.path.join(os.path.dirname(__file__), "SolmarisCondo.db")

DROP_TABLES_SQL = os.path.join(os.path.dirname(__file__), "OracleDropSolmaris.sql")
CREATE_TABLES_SQL = os.path.join(os.path.dirname(__file__), "OracleSolmaris.sql")

def execute_sql_file(filename, connection):
    try:
        with open(filename, "r") as file:
            sql_script = file.read()
        print(f"Executing SQL from {filename}:")
        cursor = connection.cursor()
        cursor.executescript(sql_script)
        connection.commit()
    except Exception as e:
        print(f"Error executing {filename}: {e}")

def execute_query(connection, query, description):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        results = cursor.fetchall()

        print(f"\n{description}:")
        if results:
            for row in results:
                print(row)
        else:
            print("No results found.")
    except Exception as e:
        print(f"Error executing query: {e}")

def main():
    try:
        connection = sqlite3.connect(DATABASE_FILE)
        print(f"Connected to database: {DATABASE_FILE}")
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return

    try:
        print("Dropping tables...")
        execute_sql_file(DROP_TABLES_SQL, connection)

        print("Creating tables...")
        execute_sql_file(CREATE_TABLES_SQL, connection)

        queries = {
            "list_tables": {
                "query": "SELECT name FROM sqlite_master WHERE type='table';",
                "description": "List of tables"
            },
            "all_renters": {
                "query": "SELECT * FROM RENTERS;",
                "description": "All Renters"
            },
            "all_properties": {
                "query": "SELECT * FROM PROPERTIES;",
                "description": "All Properties"
            },
            "all_locations": {
                "query": "SELECT * FROM LOCATION;",
                "description": "All Locations"
            },
            "all_condo_units": {
                "query": "SELECT * FROM CONDO_UNIT;",
                "description": "All Condo Units"
            },
            "all_owners": {
                "query": "SELECT * FROM OWNER;",
                "description": "All Owners"
            },
            "all_service_categories": {
                "query": "SELECT * FROM SERVICE_CATEGORY;",
                "description": "All Service Categories"
            },
            "all_service_requests": {
                "query": "SELECT * FROM SERVICE_REQUEST;",
                "description": "All Service Requests"
            }
        }

        print("Executing queries...")
        for key in queries:
            execute_query(connection, queries[key]["query"], queries[key]["description"])

    except Exception as e:
        print("Error:", e)

    finally:
        connection.close()
        print("Connection closed.")

if __name__ == "__main__":
    main()