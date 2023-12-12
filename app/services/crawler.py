import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from concurrent.futures import ThreadPoolExecutor
from ..utils import robots_parser, url_utils
from ..utils.logger import logger
import os
import threading
# from flask import flash

#media Dir
MEDIA_DIR = 'downloaded_media'
if not os.path.exists(MEDIA_DIR):
    os.makedirs(MEDIA_DIR)

class WebCrawler:
    """
    A class to perform web crawling tasks. It fetches web pages, parses their content, and extracts useful information such as links and media.

    Methods:
    crawl(url): Performs the crawling operation for a given URL.

    Attributes:
    url (str): The initial URL to start crawling from.
    max_depth (int): The maximum depth of crawling.
    max_pages (int): The maximum number of pages to crawl.
    delay (int): The delay between requests to respect the website's robots.txt rules.
    crawled_pages (set): A set of already crawled URLs to avoid duplication.
    executor (ThreadPoolExecutor): An executor for managing concurrent crawling tasks.
    lock (threading.Lock): A lock to control access to shared resources in a multithreaded environment.
    """

    def __init__(self, url, max_depth=5, max_pages=100, delay=2):
        self.url = url
        self.max_depth = max_depth
        self.max_pages = max_pages
        self.delay = delay
        self.crawled_pages = set()
        self.executor = ThreadPoolExecutor(max_workers=10)
        self.lock = threading.Lock()

    def extract_text(self, soup, tag, class_name=None):
        """ Extracts text from a specific tag and class name (optional). """
        elements = soup.find_all(tag, class_=class_name) if class_name else soup.find_all(tag)
        return ' '.join([elem.get_text(strip=True) for elem in elements])

    def crawl(self, url):
        """
        Performs the crawling operation for a given URL. This method fetches the page, checks for robots.txt compliance,
        and extracts and returns relevant data like title, content, links, etc.

        Args:
        url (str): The URL to crawl.

        Returns:
        A dictionary containing the crawled data, such as the URL, title, content, content type, file path for downloaded media, and extracted links.
        If an error occurs or the URL is invalid, an appropriate error message is returned.
        """
        # Validate URL
        if not url_utils.is_valid_url(url):
            # flash("Please enter a valid url", 'warning')
            logger.warning(f"url {url}, error Invalid URL")
            return {'url': url, 'error': 'Invalid URL'}
        
        with self.lock:
            if url in self.crawled_pages:
                return
            else:
                self.crawled_pages.add(url)
        file_name = None
        domain = urlparse(url).netloc
        robot_parser = robots_parser.RobotsParser(url)
        can_fetch = robot_parser.can_fetch(url)
        if can_fetch is None:  # Assuming can_fetch returns None if robots.txt is not found
            print(f"No robots.txt found for {url}, proceeding with crawling.")
        elif not can_fetch:
            # flash(f"Cannot fetch {url} due to site restrictions")
            print(f"Cannot fetch {url} due to robots.txt restriction.")
            logger.warning(f"Cannot fetch {url} due to robots.txt restriction.")
            return None
        
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()

            content_type = response.headers.get('Content-Type')
            print(content_type)
            # If the content type indicates an image or application/file
            if 'image' in content_type or 'application' in content_type:
                file_name = os.path.join(MEDIA_DIR, url.split('/')[-1])
                with open(file_name, 'wb') as file:
                    file.write(response.content)


            if response.status_code != 200:
                logger.warning(f"Failed to fetch {url} - Status Code: {response.status_code}")
                logger.info(f'Failed to fetch {url}')
                # flash(f"Failed to fetch {url}")
                return {'url': url, 'error': f"HTTP Error {response.status_code}"}

            soup = BeautifulSoup(response.content, 'html.parser')
            title = soup.title.string.strip() if soup.title else "No title"
            
            # Store the content and links in the database
            headers = self.extract_text(soup, 'h1') + ' ' + self.extract_text(soup, 'h2')
            paragraphs = self.extract_text(soup, 'p')
            content = headers + ' ' + paragraphs
            # content = response.text
            links = [link.get('href') for link in soup.find_all('a') if link.get('href')]
            internal_links = [urljoin(url, link) for link in links if url_utils.is_internal(link, domain) and link not in self.crawled_pages]
            image_links = [img.get('src') for img in soup.find_all('img') if img.get('src')]
            all_links = links + image_links + internal_links
            return {
                'url': url,
                'title': title, 
                'content': content,
                'content-type': content_type,
                'file_path': file_name,
                'links': all_links
            }

        except requests.RequestException as e:
            logger.error(f"Error while fetching {url}: {str(e)}")
            return {'url': url, 'error': str(e)}