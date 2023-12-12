from urllib.parse import urlparse

def is_valid_url(url):
    """
    Checks if a given URL is valid.

    This function uses urllib.parse.urlparse to analyze the URL. A URL is considered valid if it has both a scheme 
    (e.g., http, https) and a network location (netloc).

    Args:
    url (str): The URL to be validated.

    Returns:
    bool: True if the URL is valid, False otherwise.

    Raises:
    ValueError: If the URL parsing fails, indicating an invalid URL format.
    """
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

def is_internal(link, domain):
    """
    Determines if a given link is internal to the specified domain.

    This function compares the network location (netloc) of the link to the provided domain. If they match,
    the link is considered internal to the domain.

    Args:
    link (str): The link to check.
    domain (str): The domain to compare against.

    Returns:
    bool: True if the link is internal to the domain, False otherwise.
    """
    return urlparse(link).netloc == domain
