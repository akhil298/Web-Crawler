import os
import json
import csv
from urllib.parse import urljoin, urlparse, urlunparse

def save_urls_to_json(domain_urls_map, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(domain_urls_map, file, indent=4)
    print(f"URLs saved to {output_file}.")

def save_page_to_html(domain, endpoint, page_source):
    if not page_source:
        return

    os.makedirs(domain, exist_ok=True)
    parsed_url = urlparse(endpoint)
    path = parsed_url.path.strip('/')

    if path:
        filename = f"{path.replace('/', '_')}.html"
    else:
        filename = "index.html"

    filepath = os.path.join(domain, filename)

    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(page_source)
    print(f"Saved: {filepath}")

def save_status_to_csv(status_log, output_file):
    with open(output_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Domain", "Total URLs", "Completed", "Failed", "Pending"])
        writer.writerows(status_log)
    print(f"Status log saved to {output_file}.")
