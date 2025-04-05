import os

#settings
SHOW_BROWSER = os.getenv('SHOW_BROWSER', 'True') == 'True'
MAX_SCROLLS = int(os.getenv('MAX_SCROLLS', 90))
MAX_WORKERS = int(os.getenv('MAX_WORKERS',2))
SCROLL_PAUSE_TIME = float(os.getenv('SCROLL_PAUSE_TIME', 1.5))
WAIT_TIME = float(os.getenv('WAIT_TIME', 2))
