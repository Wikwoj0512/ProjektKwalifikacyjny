import re
import typing
from urllib.parse import urlparse


class RegEx:
    patterns = dict(
        url=re.compile(
            r'^(?:http|ftp)s?://'  # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
            r'localhost|'  # localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
            r'(?::\d+)?'  # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE),
        body=re.compile(r'<body[^>]*>([\s\S]*)(?=</body>)'),  # Find everything between <body> and </body>
        header=re.compile(r'<h1[^>]*>([\s\S]+)(?=</h1>)'),  # Find everything in header tags
        words=re.compile(r'\w{2,}'),  # Find words with at least 2 characters
        content=re.compile(r'<(?!script|title)[^>]*>([^<]*)'),  # Find everything between tags except <script> and <title>
        headerContent= re.compile(r'(<(?!script|title)[^>]*>){0,1}([^<]*)')
        # Find everything between tags except <script> and <title>
    )

    @classmethod
    def search(cls, pattern_name: str, text: str) -> typing.Union[re.Match, None]:
        """
        Search for a pattern in a string
        :param pattern_name: Type of pattern to be searched
        :param text: String to search through
        :return: Match instance or None if no match was found
        """
        return cls.patterns[pattern_name].search(text.lower())

    @classmethod
    def findall(cls, pattern_name: str, text: str) -> typing.List[str]:
        """
        Find each occurrence of a pattern inside a string
        :param pattern_name: Type of pattern to be found
        :param text: String to search through
        :return: Occurrences of the pattern in the string
        """
        return cls.patterns[pattern_name].findall(text.lower())

    @classmethod
    def match(cls, pattern_name: str, text: str) -> typing.Union[re.Match, None]:
        """
        Match a pattern to the beginning of a string
        :param pattern_name: Type of pattern to be matched
        :param text: String to search through
        :return: Match instance or None if no match was found
        """
        return cls.patterns[pattern_name].match(text.lower())


def validate_url(url: str) -> bool:
    """
    Function to validate url using urlparse
    :param url: Url address
    :return: True if url is valid, False otherwise
    """
    if isinstance(RegEx.match("url", url),re.Match):
        return True
    else:
        return False


class UrlException(Exception):
    pass


class ContentException(Exception):
    pass


class ConnectionException(Exception):
    pass
