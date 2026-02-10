# Quotes Web Scraper & Analysis

## Overview


This mini project scrapes quotes from **quotes.toscrape.com**, stores the data in a CSV file and a SQLite database, and performs basic analysis to visualize the top authors by number of quotes.

It demonstrates a simple end-to-end data pipeline:
**Web Scraping → Data Storage → Database → Analysis & Visualization**

---

## Features

* Scrapes quotes and author names using **BeautifulSoup**
* Saves scraped data to **quotes.csv**
* Loads CSV data into a **SQLite database (data.db)**
* Analyzes data using **Pandas**
* Visualizes results with **Matplotlib** (Top 5 Authors)

---

## Project Structure

```
web_scraper_project/
│
├── scraper.py        # Scrapes quotes from website
├── quotes.csv        # Stored scraped data
├── database.py       # Loads CSV into SQLite database
├── data.db           # SQLite database (generated file)
├── analysis.py       # Data analysis and visualization
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

This creates **quotes.csv**

### 3. Store Data in Database

```bash
python database.py
```

This creates **data.db**

### 4. Analyze and Visualize Data

```bash
python analysis.py
```

A bar chart of the top 5 authors will be displayed.

---

## Sample Output

* CSV file containing quotes and authors
* SQLite database table named `quotes`
* Bar chart showing most frequent authors

---

## Learning Outcomes

* Basic web scraping techniques
* Working with CSV and SQLite databases
* Using Pandas for analysis
* Creating visualizations with Matplotlib
* Building a simple data pipeline project

---

## Future Improvements

* Scrape multiple pages (pagination)
* Add filters (e.g., quotes by specific author)
* Export analysis results to Excel
* Automate the entire pipeline with a single script
