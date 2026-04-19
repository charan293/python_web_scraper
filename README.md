# Quotes Data Analyzer (Flask Web App)

## 🚀 Overview

This project is a full-stack Python application that scrapes quotes from **quotes.toscrape.com**, stores them in structured formats (CSV and SQLite), and provides an interactive web interface for searching, analyzing, and exporting data.

It demonstrates a complete data pipeline:
**Web Scraping → Data Storage → Database → Querying → Web Interface → Export**

---

## ✨ Features

* Scrapes quotes and authors from multiple pages (pagination)
* Stores data in CSV and SQLite database
* Search quotes by:

  * Author
  * Keyword
* Web-based interface using Flask
* Displays results in a clean table format
* Download filtered results as Excel (`output.xlsx`)
* Styled UI using HTML & CSS

---

## 🌐 Web Application

This project includes a Flask-based web app.

### Features:

* Search quotes directly from browser
* View results in a structured table
* Download results as Excel
* Simple and clean UI

---

## 📂 Project Structure

```
web_scraper_project/
│
├── app.py              # Flask web application
├── scraper.py          # Scrapes quotes from multiple pages
├── database.py         # Loads CSV into SQLite database
├── analysis.py         # CLI-based search and analysis
├── check_db.py         # Database check script
├── requirements.txt    # Dependencies
│
├── templates/          # HTML templates
│   ├── index.html
│   └── results.html
│
├── static/             # CSS styling
│   └── style.css
```

---

## 🛠️ Technologies Used

* Python
* Flask
* Requests
* BeautifulSoup
* Pandas
* SQLite
* Matplotlib
* OpenPyXL

---

## ⚙️ How to Run the Project

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the Scraper

```bash
python scraper.py
```

Creates `quotes.csv`

### 3. Store Data in Database

```bash
python database.py
```

Creates `data.db`

### 4. Run Web App

```bash
python app.py
```

Open in browser:

```
http://127.0.0.1:5000
```

---

## 📊 Output

* CSV file with scraped quotes
* SQLite database (`quotes` table)
* Web interface for searching data
* Excel file (`output.xlsx`) for exported results
* Tabular results displayed in browser

---

## 🧠 Description

Developed a full-stack data analysis application that integrates web scraping, database management, and web development. The project allows users to search and analyze quote data through an interactive web interface and export results for further use. It demonstrates practical skills in backend development, data processing, and UI integration.

---

## 📚 Learning Outcomes

* Web scraping using BeautifulSoup
* Working with CSV and SQLite databases
* Building web applications using Flask
* Handling user input via web forms
* Data querying with SQL and Pandas
* Exporting data to Excel
* Structuring full-stack projects

---

## 🔮 Future Improvements

* Deploy the application online for public access
* Add advanced filters (author + keyword together)
* Improve UI with modern frameworks (Bootstrap)
* Add authentication and user sessions
* Create dashboards for data visualization

---

## 📌 Note

Generated files such as `data.db`, `quotes.csv`, and `output.xlsx` are excluded using `.gitignore`.
