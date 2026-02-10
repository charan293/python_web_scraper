import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect("data.db")
df = pd.read_sql("SELECT * FROM quotes", conn)
author_counts = df["author"].value_counts().head(5)
author_counts.plot(kind="bar")
plt.title("Top 5 Authors by Number of Quotes")
plt.xlabel("Author")
plt.ylabel("Number of Quotes")
plt.tight_layout()
plt.show()

conn.close()
