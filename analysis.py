import sqlite3
import pandas as pd

conn = sqlite3.connect("data.db")

print("Search Options:")
print("1. Search by Author")
print("2. Search by Keyword")

choice = input("Enter your choice (1 or 2): ")

if choice == "1":
    author = input("Enter author name: ")
    query = "SELECT * FROM quotes WHERE author LIKE ?"
    df = pd.read_sql(query, conn, params=[f"%{author}%"])

elif choice == "2":
    keyword = input("Enter keyword: ")
    query = "SELECT * FROM quotes WHERE quote LIKE ?"
    df = pd.read_sql(query, conn, params=[f"%{keyword}%"])

else:
    print("Invalid choice")
    conn.close()
    exit()

if df.empty:
    print("No results found.")
else:
    print(df.to_string(index=False))

# Export option
save = input("Do you want to save results to Excel? (yes/no): ")

if save.lower() == "yes":
    df.to_excel("output.xlsx", index=False)
    print("Data saved to output.xlsx")

conn.close()
