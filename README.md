# Quotes Data Analyzer

## 🚀 Overview

This project is a Python-based data scraping and analysis application that extracts quotes and author information from the Quotes to Scrape website.

The application collects data from multiple pages, stores it in CSV and SQLite formats, allows users to search quotes by author or keyword, and exports search results to Excel.

It demonstrates a complete data pipeline:

**Web Scraping → Data Storage → Database → Querying → Export**

---

## ✨ Features

* Scrapes quotes and authors from multiple pages (pagination)
* Stores data in CSV format
* Imports data into an SQLite database
* Search quotes by:

  * Author
  * Keyword
* Export filtered results to Excel (`output.xlsx`)
* Command-line based interface

---

## 🛠️ Technologies Used

* Python
* Requests
* BeautifulSoup4
* Pandas
* SQLite3
* OpenPyXL

---

## 📂 Project Structure

```text
web_scraping_project/
│
├── scraper.py
├── database.py
├── analysis.py
├── check_db.py
│
├── quotes.csv
├── data.db
├── output.xlsx
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Workflow

### Step 1: Scrape Data

Run:

```bash
python scraper.py
```

This script:

* Sends HTTP requests to the website
* Extracts quotes and author names
* Handles pagination automatically
* Saves data into `quotes.csv`

---

### Step 2: Store Data in Database

Run:

```bash
python database.py
```

This script:

* Reads the CSV file
* Creates an SQLite database
* Stores records in the `quotes` table

---

### Step 3: Search Data

Run:

```bash
python analysis.py
```

Users can:

* Search quotes by author name
* Search quotes by keyword
* View matching records
* Export results to Excel

---

## 📊 Example Search

```text
Search Options:
1. Search by Author
2. Search by Keyword

Enter your choice: 1
Enter author name: Albert Einstein
```

Output:

```text
Matching quotes displayed in terminal
```

---

## 📤 Excel Export

After searching, users can choose to export results:

```text
Do you want to save results to Excel? (yes/no):
```

The filtered data will be saved as:

```text
output.xlsx
```

---

## 🎯 Learning Outcomes

Through this project, I learned:

* Web scraping using Requests and BeautifulSoup
* HTML parsing and data extraction
* Working with CSV files using Pandas
* Database management using SQLite
* SQL querying (SELECT, WHERE, LIKE)
* Data export to Excel
* Building end-to-end data processing pipelines

---

## 🔮 Future Improvements

* Remove duplicate records automatically
* Add data visualization and analytics
* Schedule automated scraping
* Support multiple websites
* Upgrade from SQLite to MySQL/PostgreSQL
* Add advanced filtering options

---

## 👨‍💻 Author

Charan
