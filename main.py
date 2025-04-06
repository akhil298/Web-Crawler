import json
from concurrent.futures import ThreadPoolExecutor, as_completed
from config.config import MAX_SCROLLS, MAX_WORKERS
from scraping.scraper import scrape_page
from processing.processor import extract_links, extract_product_links
from saving.saver import save_urls_to_json, save_page_to_html, save_status_to_csv
from urllib.parse import urlparse 

def process_homepage(url):
    page_source = scrape_page(url, max_scrolls=7)
    if page_source:
        endpoints = extract_links(url, page_source)
        return urlparse(url).netloc, list(endpoints)
    return urlparse(url).netloc, []

def process_endpoint(domain, endpoint):
    page_source = scrape_page(endpoint, max_scrolls=MAX_SCROLLS)
    if page_source:
        save_page_to_html(domain, endpoint, page_source)
        product_links = extract_product_links(endpoint, page_source)
        return endpoint, product_links
    return endpoint, []

def main(urls):
    domain_urls_map = {}
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        results = list(executor.map(process_homepage, urls))
        for domain, endpoints in results:
            domain_urls_map[domain] = endpoints

    save_urls_to_json(domain_urls_map, 'endpoint.json')
    save_status_to_csv([[domain, len(endpoints), 0, 0, len(endpoints)] for domain, endpoints in domain_urls_map.items()], 'initial_status_log.csv')

    product_links_map = {}
    status_log = []

    for domain, endpoints in domain_urls_map.items():
        status_log.append([domain, len(endpoints), 0, 0, len(endpoints)])
        with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
            futures = [executor.submit(process_endpoint, domain, endpoint) for endpoint in endpoints]
            for future in as_completed(futures):
                endpoint, product_links = future.result()
                if product_links:
                    if domain in product_links_map:
                        product_links_map[domain].extend(product_links)
                    else:
                        product_links_map[domain] = product_links
                    status_log[-1][2] += 1 
                else:
                    status_log[-1][3] += 1  
                status_log[-1][4] -= 1 

    save_status_to_csv(status_log, 'status_log.csv')
    with open('product_links.json', 'w', encoding='utf-8') as file:
        json.dump(product_links_map, file, indent=4)
    print("Product links saved to product_links.json.")

if __name__ == "__main__":
    urls = [
        "https://www.virgio.com/",
        "https://www.tatacliq.com/",
        "https://nykaafashion.com/",
        "https://www.westside.com/",
    ]
    main(urls)
