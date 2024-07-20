import psycopg2
from psycopg2 import sql

def create_connection():
    try:
        conn = psycopg2.connect(
            dbname="your_database_name",
            user="your_username",
            password="your_password",
            host="localhost",
            port="5432"
        )
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None

def insert_data(conn, pdf, state, city, center, marks):
    try:
        cur = conn.cursor()
        insert_query = sql.SQL("""
            INSERT INTO neetscam (pdf, state, city, center, marks)
            VALUES (%s, %s, %s, %s, %s)
        """)
        cur.execute(insert_query, (pdf, state, city, center, marks))
        conn.commit()
        cur.close()
    except Exception as e:
        print(f"Error inserting data: {e}")

def main():
    conn = create_connection()
    if conn:
        insert_data(conn, 1, 2, 3, 4, 5)
        conn.close()
