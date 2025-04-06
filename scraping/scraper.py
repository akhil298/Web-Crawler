import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from config.config import SHOW_BROWSER, SCROLL_PAUSE_TIME, WAIT_TIME, MAX_SCROLLS

def scroll_page(driver, scroll_percentage=0.62, max_scrolls=5):
    for _ in range(max_scrolls):
        driver.execute_script(f"window.scrollBy(0, window.innerHeight * {scroll_percentage});")
        time.sleep(SCROLL_PAUSE_TIME)

def scrape_page(url, max_scrolls=5):
    chrome_options = Options()
    if not SHOW_BROWSER:
        chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.page_load_strategy = 'eager'
    service = Service()
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        print(f"Fetching page: {url}")
        driver.get(url)
        time.sleep(WAIT_TIME)
        scroll_page(driver, max_scrolls=max_scrolls)
        page_source = driver.page_source
        print(f"Page {url} fetched successfully.")
        return page_source
    except Exception as e:
        print(f"Error processing page {url}: {e}")
    finally:
        driver.quit()
