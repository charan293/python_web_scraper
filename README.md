# Quotes Data Analyzer

## Overview

This project is a Python-based data pipeline that scrapes quotes from **quotes.toscrape.com**, stores them in structured formats (CSV and SQLite), and provides an interactive tool for searching, analyzing, and exporting data.

It demonstrates a complete workflow:
**Web Scraping → Data Storage → Database → Querying → Visualization → Export**

---

## Features

* Scrapes quotes and authors from multiple pages (pagination)
* Stores data in CSV and SQLite database
* Search quotes by author (user input)
* Search quotes by keyword
* Export filtered results to Excel (`output.xlsx`)
* Visualize top authors using Matplotlib
* Interactive command-line interface

---

## Project Structure

```
web_scraper_project/
│
├── scraper.py        # Scrapes quotes from multiple pages
├── quotes.csv        # Stored scraped data
├── database.py       # Loads CSV into SQLite database
├── data.db           # SQLite database (generated file)
├── analysis.py       # Search, analysis, and export functionality
├── check_db.py       # Quick database check script
├── requirements.txt  # Project dependencies
```

---

## Technologies Used

* Python
* Requests
* BeautifulSoup
* Pandas
* SQLite
* Matplotlib
* OpenPyXL (for Excel export)

---

## How to Run the Project

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the Scraper

```bash
python scraper.py
```

This creates **quotes.csv** with data from all pages.

### 3. Store Data in Database

```bash
python database.py
```

This creates **data.db** with a table named `quotes`.

### 4. Run Analysis Tool

```bash
python analysis.py
```

* Choose search option (author or keyword)
* View results in terminal
* Optionally export results to Excel

---

## Output

* CSV file containing quotes and authors
* SQLite database with structured data
* Interactive search results in terminal
* Excel file (`output.xlsx`) for filtered results
* Bar chart visualization of top authors

---

## Description

Developed a Python-based data pipeline that scrapes, processes, and analyzes quote data from a website. The project includes features like pagination scraping, database storage, user-driven search (author/keyword), and exporting results to Excel. It demonstrates practical skills in web scraping, data handling, SQL querying, and data visualization.

---

## Learning Outcomes

* Web scraping using BeautifulSoup
* Working with CSV and SQLite databases
* Writing SQL queries with Python (Pandas)
* Data visualization using Matplotlib
* Building an interactive CLI-based tool
* Handling real-world debugging and dependency issues

---

## Future Improvements

* Build a graphical user interface (GUI) for better user experience
* Convert the project into a web application using Flask
* Add advanced data visualizations and dashboards
* Automate data updates with scheduling
