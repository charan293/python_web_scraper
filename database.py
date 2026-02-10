import sqlite3
import pandas as pd

df = pd.read_csv("quotes.csv")
conn = sqlite3.connect("data.db")
df.to_sql("quotes", conn, if_exists="replace", index=False)

conn.close()

print("Data stored successfully in SQLite database!")
