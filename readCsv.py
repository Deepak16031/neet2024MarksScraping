import os
import csv
import psycopg2
from psycopg2 import sql

def create_connection():
    try:
        conn = psycopg2.connect(
            dbname="neetScam",
            user="deepak",
            password="deepak",
            host="localhost",
            port="5436"
        )
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None

def insert_data(conn, arr):
    try:
        cur = conn.cursor()
        insert_query = sql.SQL("""
            INSERT INTO neetscam (pdf, state, city, center, marks)
            VALUES (%s, %s, %s, %s, %s)
        """)
        cur.executemany(insert_query, arr)
        conn.commit()
        cur.close()
    except Exception as e:
        print(f"Error inserting data: {e}")

def main():
    conn = create_connection()
    if conn:
        folder_path = 'csv'
        read_csv_files_in_folder(folder_path, conn)
        conn.close()



def is_numeric(value):
    # Check if the value is numeric
    try:
        for i in value:
            if (i):
                float(i)
        return True
    except ValueError:
        return False

def read_csv_files_in_folder(folder_path, conn):
    # List all files in the given folder
    for filename in os.listdir(folder_path):
        print(filename)
        arr = []
        # Check if the file is a CSV file
        if filename.endswith('.csv'):
            file_path = os.path.join(folder_path, filename)
            # Open the CSV file
            with open(file_path, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                # Skip the header row
                next(reader, None)
                # Read each line in the CSV file
                for row in reader:
                    # Check if the first column is numeric
                    if len(row) > 0 and is_numeric(row):
                        state = int(filename[0:2])
                        city = int(filename[2:4])
                        center = int(filename[4:6])
                        file = int(filename.split('.')[0])
                        j = 1
                        while (j<len(row) and row[j] != ""):
                            try:
                                arr.append([file, state, city, center, row[j]])
                                #insert_data(conn, file, state, city, center, row[j])
                            except:
                                print(row)
                                return
                            j += 2

        insert_data(conn, arr)

main()
