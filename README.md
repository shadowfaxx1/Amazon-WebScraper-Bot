# Amazon Product Information Bot

Automates retrieval of Amazon product details (price, merchant, Amazon-recommended status) using ASIN IDs via Selenium, and saves results to Excel for tracking.

---

## Quick Start

```sh
git clone <repository_url>
pip install -r requirements.txt
```

Download [Chrome WebDriver](https://chromedriver.chromium.org/) matching your Chrome version and place it in the project directory. Then run the script with your list of ASIN links.

---

## How It Works

The bot is a Python class inheriting from `webdriver.Chrome`. For each ASIN it:

1. Searches the product page
2. Scrapes price, merchant info, and Amazon-recommended status
3. Checks ETrade Online price if available
4. Skips unavailable or unqualified listings

Results are printed as a table and saved to Excel.

---

## Notes

- Ensure you have write permissions for the Excel file and WebDriver directory
- XPath/CSS selectors may need updating if Amazon changes its page structure

---

## Stack
Python · Selenium · Chrome WebDriver · OpenPyXL
