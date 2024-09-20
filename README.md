# Web Scraping Project

## Overview
This project scrapes headlines from a specified webpage and saves them to a CSV file.

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/Fatima0717/task_manager.git
    ```
2. **Navigate to the project directory:**
    ```bash
    cd yourrepository
    ```
3. **Set up a virtual environment:**
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    ```

4. **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the script:**
    ```bash
    python scrape_data.py
    ```

2. **Check the `scraped_data.csv` file for the output.**

## Dependencies

- `requests`
- `beautifulsoup4`
- `csv`
