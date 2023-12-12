import requests
from urllib.robotparser import RobotFileParser

class RobotsParser:
    """
    A class to parse and interpret the robots.txt file for a given website. It uses Python's urllib.robotparser module 
    to read and analyze the robots.txt file, providing functionality to check if a specific URL can be fetched by a given user agent.

    Methods:
    can_fetch(url, user_agent): Determines if the given URL can be fetched by the specified user agent based on the robots.txt rules.

    Attributes:
    parser (RobotFileParser): An instance of RobotFileParser used to parse the robots.txt file.
    robots_url (str): The full URL to the robots.txt file of the base website.

    Args:
    base_url (str): The base URL of the website for which the robots.txt file will be parsed.

    Usage:
    To use this class, instantiate it with the base URL of the website, and then call can_fetch with the URL you wish to check.
    """
    def __init__(self, base_url):
        self.parser = RobotFileParser()
        self.robots_url = f"{base_url}/robots.txt"
        self.parser.set_url(self.robots_url)
        self.parser.read()

    def can_fetch(self, url, user_agent='*'):
        """
        Checks if the given URL can be fetched by the specified user agent according to the site's robots.txt rules.

        Args:
        url (str): The URL to check for access.
        user_agent (str): The user agent to check access for. Defaults to '*' (all user agents).

        Returns:
        bool: True if the URL can be fetched by the user agent, False otherwise.
        """
        return self.parser.can_fetch(user_agent, url)
