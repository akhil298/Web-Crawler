
# E-commerce Product URL Crawler

The E-commerce Product URL Crawler is a web scraping tool designed to discover and list all product URLs across multiple e-commerce websites. This tool is built to handle variations in URL structures and can scale to process hundreds of domains efficiently.

## Features

- **URL Discovery:** Intelligently identifies product pages using regex patterns.
- **Scalability:** Modular design and parallel processing for handling large websites.
- **Performance:** Optimized for efficient scraping with configurable settings.
- **Robustness:** Handles edge cases and variations in URL structures.

## Requirements

- Python 3.x
- Selenium
- BeautifulSoup
- ChromeDriver

## Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/akhil298/Web-Crawler.git
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   
## Configuration

Configure the crawler settings in `config/config.py`:

- `SHOW_BROWSER`: Set to `True` to show the browser during scraping.
- `MAX_SCROLLS`: Maximum number of scrolls per page.
- `MAX_WORKERS`: Number of parallel workers for scraping.
- `SCROLL_PAUSE_TIME`: Time to wait between scrolls.
- `WAIT_TIME`: Initial wait time after loading a page.

## Usage

Run the crawler with the following command:

```bash
python main.py
```

The crawler will process the specified domains and save the discovered product URLs to JSON files.

## Project Structure

- `config/`: Configuration settings.
- `utils/`: Utility functions for URL processing.
- `scraping/`: Web scraping logic using Selenium.
- `processing/`: Functions for extracting and processing URLs.
- `saving/`: Functions for saving data to files.
- `requirements.txt`: List of Python dependencies.
- `README.md`: Project documentation.

## Approach to Finding Product URLs

The crawler uses a combination of regex patterns and URL cleaning to identify product URLs. The process involves the following steps:

1. **Homepage Scraping:** The crawler first scrapes the homepage of each domain to extract potential product URLs.
2. **URL Filtering:** The extracted URLs are filtered using regex patterns to identify those that are likely product pages.
3. **Endpoint Processing:** Each filtered URL is then processed to extract product links. The crawler scrolls through the page to load dynamically loaded content.
4. **Data Saving:** The discovered product URLs are saved to JSON files, and the status of each domain's processing is logged to a CSV file.


## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## Contact

For any questions or suggestions, please contact [akhilakhi298@gmai.com](mailto:akhilakhi298@gmai.com).
