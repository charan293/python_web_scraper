from flask import Flask, request, render_template, send_file
import sqlite3
import pandas as pd

app = Flask(__name__)

last_df = None

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/search", methods=["POST"])
def search():
    global last_df

    user_input = request.form["query"]

    conn = sqlite3.connect("data.db")

    query = """
    SELECT * FROM quotes
    WHERE author LIKE ? OR quote LIKE ?
    """

    df = pd.read_sql(query, conn, params=[f"%{user_input}%", f"%{user_input}%"])
    conn.close()

    last_df = df

    if df.empty:
        return "<h3>No results found</h3><a href='/'>Go Back</a>"

    return render_template("results.html", table=df.to_html(index=False))

@app.route("/download")
def download():
    global last_df

    if last_df is None or last_df.empty:
        return "No data to download"

    file_path = "output.xlsx"
    last_df.to_excel(file_path, index=False)

    return send_file(file_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)