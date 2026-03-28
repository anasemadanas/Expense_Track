import sqlite3
import csv
from shared.constants import DB_PATH, DATA_SAMPLE_PATH
import os

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute("SELECT Transaction_ID, Name, Amount, Category, Date, Type FROM Transaction")
rows = cursor.fetchall()

os.makedirs(DATA_SAMPLE_PATH, exist_ok=True)

file_path = os.path.join(DATA_SAMPLE_PATH, "transactions.csv")

with open(file_path, mode='w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    
    writer.writerow(["ID", "Name", "Amount", "Category", "Date", "Type"])
    
    writer.writerows(rows)

print(f"Transactions exported to {file_path}")

conn.close()