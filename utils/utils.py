import re
from urllib.parse import urljoin, urlparse, urlunparse

def is_likely_product_url(url):
    product_patterns = [r'/c-', r'/product[s]?/', r'/item[s]?/', r'/p/', r'/shop/', r'/clothes?/', r'/collection[s]?/',
                        r'/men[s]?/?', r'/women[s]?/?', r'/hot/?', r'/trend[s]?/?', r'/fashion/?',
                        r'/wear/?', r'/store/?', r'/new-arrivals/?', r'/deals?/?']
    exclude_patterns = [r'(?i)/faq/?', r'(?i)/policy/?', r'(?i)/contact/?', r'(?i)/about/?', r'(?i)/account/?',
                        r'(?i)/cart/?', r'(?i)/login/?', r'(?i)/search', r'(?i)/help',
                        r'(?i)/privacy', r'(?i)/terms', r'(?i)/stores',r'/pages/?']

    if any(re.search(pattern, url) for pattern in product_patterns) and not any(re.search(pattern, url) for pattern in exclude_patterns):
        return True
    return False

def clean_url(url):
    parsed_url = urlparse(url)
    cleaned_url = urlunparse(parsed_url._replace(query='', fragment=''))
    return cleaned_url
