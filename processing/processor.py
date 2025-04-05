from bs4 import BeautifulSoup
from utils.utils import is_likely_product_url, clean_url
from urllib.parse import urljoin, urlparse
import re

def extract_links(homepage_url, page_source):
    soup = BeautifulSoup(page_source, 'html.parser')
    links = set()
    domain = urlparse(homepage_url).netloc

    for link in soup.find_all('a', href=True):
        href = link['href']
        full_url = urljoin(homepage_url, href)
        cleaned_url = clean_url(full_url)
        if is_likely_product_url(cleaned_url) and urlparse(cleaned_url).netloc == domain:
            links.add(cleaned_url)

    print(f"Extracted {len(links)} links from page {homepage_url}.")
    return links

# def extract_product_links(endpoint_url, page_source):
#     soup = BeautifulSoup(page_source, 'html.parser')
#     links = set()
#     domain = urlparse(endpoint_url).netloc

#     for link in soup.find_all('a', href=True):
#         href = link['href']
#         full_url = urljoin(endpoint_url, href)
#         cleaned_url = clean_url(full_url)
#         if is_likely_product_url(cleaned_url) and urlparse(cleaned_url).netloc == domain:
#             links.add(cleaned_url)

#     print(f"Extracted {len(links)} product links from endpoint {endpoint_url}.")
#     return list(links)

def extract_product_links(endpoint_url, page_source):
    soup = BeautifulSoup(page_source, 'html.parser')
    links = set()
    domain = urlparse(endpoint_url).netloc

    # Extract links from <a> tags
    for link in soup.find_all('a', href=True):
        href = link['href']
        full_url = urljoin(endpoint_url, href)
        cleaned_url = clean_url(full_url)
        if is_likely_product_url(cleaned_url) and urlparse(cleaned_url).netloc == domain:
            links.add(cleaned_url)

    # Extract links from <script> tags
    script_pattern = re.compile(r'"url":"(https://[^"]+\/\d+)"')
    for script in soup.find_all('script', type='application/ld+json'):
        if script.string:
            matches = script_pattern.findall(script.string)
            for match in matches:
                cleaned_url = clean_url(match)
                if is_likely_product_url(cleaned_url) and urlparse(cleaned_url).netloc == domain:
                    links.add(cleaned_url)

    print(f"Extracted {len(links)} product links from endpoint {endpoint_url}.")
    return list(links)
