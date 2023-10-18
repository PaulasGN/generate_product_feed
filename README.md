# Generating an XML Product Feed from SQLite Database

This Python script generates an XML product feed from a provided SQLite database. The resulting XML file adheres to the Google Merchant product data specifications and can be used to sync a product catalog with external systems such as marketplaces.

## Prerequisites

Before running the script, ensure that you have the following in place:

1. **SQLite Database**: Set up an SQLite database containing the product catalog data. The database structure should include tables like `product`, `manufacturer`, `product_description`, and `product_image`. Update the database file path in the script accordingly.

2. **Python Environment**: Make sure you have Python installed on your system. This script was written in Python3.

3. **Required Python Modules**: You need the `sqlite3` and `xml.etree.ElementTree` modules, which are included in Python's standard library.

## Running the Script

Follow these steps to run the script:

1. **Update the Database Path**:

   Open the Python script (`product_feed.py`) in a code editor and update the database file path. Modify the following line to match your database file:

   ```python
   conn = sqlite3.connect('data.sqlite')


2. **Run the Script:**
   Open your terminal or command prompt, navigate to the directory containing the script, and run the following command:
     ```bash
      python product_feed.py

 This will execute the script, generate the XML product feed, and save it as feed.xml in the same directory.
