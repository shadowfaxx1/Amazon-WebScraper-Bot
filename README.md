# Amazon Product Information Bot

This project involves creating an Amazon Product Information Bot using Selenium to automate the process of retrieving various product details, including prices, merchant information, and seller status for specific products using their ASIN IDs. The bot saves this information for further analysis and tracking by the company.

## Overview

The Amazon Product Information Bot is a Python script that utilizes Selenium and Chrome WebDriver to interact with the Amazon website, search for specific products using their ASIN IDs, and scrape relevant information. The bot retrieves product prices, merchant details, and checks whether the product is recommended by Amazon. The collected data is then stored in an Excel spreadsheet for easy tracking and analysis.

## Requirements

To run the Amazon Product Information Bot, you need the following:

1. Python: Make sure you have Python installed on your system.
2. Selenium: Install the Selenium library for Python using pip.
3. Chrome WebDriver: Download the appropriate Chrome WebDriver compatible with your Chrome browser version.
4. Excel file: Create an Excel file to store the scraped product information.

## Installation

1. Clone the repository: `git clone <repository_url>`
2. Install required libraries: `pip install -r requirements.txt`
3. Download and place the Chrome WebDriver in the specified directory.

## How it Works

1. The bot is created as a Python class named `amazon`, which inherits from `webdriver.Chrome`.
2. The class is initialized with optional arguments for the driver path, teardown, and headless mode.
3. The `perform_search` method performs the search operation using the provided ASIN link. If the product is unavailable or not qualified, it returns 0; otherwise, it proceeds with scraping.
4. The `get_item_price` method fetches the product price. If the product price is not found, it returns 0.
5. The `is_present` method checks if the product is present and available for scraping.
6. The `get_merchant_info` method retrieves the merchant information for the product.
7. The `get_ETrade_price` method gets the price from ETrade Online if available.
8. The `search_url` method combines the previous methods to perform scraping for a single product.
9. The `search_items` method iterates through the provided ASIN links, performs scraping, and saves the data in a list.
10. The scraped data is then presented in a pretty table format.
11. The data is also saved to the Excel file.

## Usage

1. Create a list of ASIN links for the products you want to track.
2. Initialize the `amazon` class with the provided ASIN links.
3. Run the script to execute the scraping process and save the product information to the Excel file.

## Note

1. Make sure you have the required permissions to access the Excel file and the Chrome WebDriver.
2. The bot may not work correctly if the Amazon website structure changes. In such cases, you may need to update the XPath or CSS selector in the methods.

Use the Amazon Product Information Bot to efficiently retrieve and track product details for your company's products on Amazon!
