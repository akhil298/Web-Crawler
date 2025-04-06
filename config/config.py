import os

#settings
SHOW_BROWSER = os.getenv('SHOW_BROWSER', "False") == 'True'
MAX_SCROLLS = int(os.getenv('MAX_SCROLLS', 500))
MAX_WORKERS = int(os.getenv('MAX_WORKERS',4))
SCROLL_PAUSE_TIME = float(os.getenv('SCROLL_PAUSE_TIME', 1.8))
WAIT_TIME = float(os.getenv('WAIT_TIME', 2))
