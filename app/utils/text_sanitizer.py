def sanitize_text(text):
    """ Remove NULL bytes and non-printable characters from a string. """
    if text is None:
        return 'N/A'
    sanitized = text.replace('\x00', '')  # Remove NULL bytes
    return ''.join(char for char in sanitized if char.isprintable())
