Real Estate Data Scraper
This project is a web scraper designed to extract real estate listings from a specified website and save the extracted data into a CSV file. The scraper collects information such as prices, addresses, number of beds, baths, and lot sizes for properties listed in Rock Springs, WY.

Features
Web Scraping: Uses requests to fetch web pages and BeautifulSoup to parse HTML content.
Pagination Handling: Navigates through multiple pages to collect data.
Data Extraction: Extracts details including price, address, number of beds, full baths, half baths, area, and lot size.
CSV Output: Saves the scraped data into a CSV file for easy access and analysis.
How It Works
Send HTTP Requests: Fetches the initial page and determines the number of pages to scrape based on pagination information.
Parse HTML Content: Uses BeautifulSoup to parse the HTML content of each page.
Extract Data: Collects property details including price, address, number of beds, full baths, half baths, area, and lot size.
Handle Missing Data: Provides default values ("None") when certain data points are not available.
Save Data: Writes the collected data to Output.csv.
Installation
Make sure you have Python installed. Then, install the required packages using pip:

pip install requests pandas beautifulsoup4

Usage
Run the Script: Execute the script to start scraping data from the website.

python web_scraper.py

Check the Output: After the script completes, the scraped data will be saved in Output.csv in the same directory as the script.
Example Output
The Output.csv file will contain columns for:

Price: The listed price of the property.
Address: The property address.
Beds: Number of bedrooms.
Full Baths: Number of full bathrooms.
Area: The area of the property in square feet.
Half Baths: Number of half bathrooms.
Lot Size: The size of the lot.
Notes
The script assumes the website's structure and class names will remain consistent. If the website's layout changes, the script may need adjustments.
This script is intended for educational purposes and personal use. Ensure compliance with the website's robots.txt file and terms of service when scraping.
