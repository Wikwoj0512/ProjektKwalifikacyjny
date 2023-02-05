import typing

import requests

from utils import RegEx, UrlException, ContentException, ConnectionException


def get_document(url: str) -> str:
    """
    Function to get document from url
    :param url: Url address
    :return: Body of the document
    """
    try:
        response = requests.get(url)
    except requests.exceptions.ConnectionError:
        raise ConnectionException("Connection error - website could not be reached")
    if response.status_code != 200:
        raise UrlException("Invalid url - status code: {}".format(response.status_code))
    try:
        return RegEx.search("body", response.text).group(1)
    except AttributeError:
        raise UrlException("Invalid url - no body tag found on the page")


def get_header_words(document: str) -> typing.Dict[str,int]:
    """
    Function to get all words from the header section of the document
    :param document: Document to be analysed
    :return: A dictionary with all words from the header section of the document
    """
    header_words = {}
    for header in RegEx.findall("header", document):
        for content in RegEx.findall("headerContent", header):
            for word in RegEx.findall("words", content[1]):
                header_words[word] = 0
    if not header_words:
        raise ContentException("No header found on the page")
    return header_words


def get_content_words(document: str) -> typing.List[str]:
    """
    Function to get all words from the content section of the document
    :param document: Document to be analysed
    :return: All words from the content section of the document
    """
    content_words = []  # find all words in the content section of the document
    for content_set in RegEx.findall("content", document):
        for word in RegEx.findall("words", content_set):
            content_words.append(word)

    if not content_words:
        raise ContentException("No content found on the page")
    return content_words


def analyse_article(url: str) -> typing.Dict[str, int]:
    """
    Function to analyse contents of an article and count
    occurrences of each word in the header section on the page
    :param url: Url address
    :return: A dictionary with amount of occurrences of each word in the header section
    """
    try:
        document = get_document(url)  # get document from url
    except UrlException as e:  # if there is an error with the url
        raise e
    except ConnectionException as e:  # if there is an error with the connection
        raise e

    try:
        header_keywords = get_header_words(document)  # get all words from the header section of the document
        content_words = get_content_words(document)  # get all words from the content section of the document
    except ContentException as e:  # if there is an error with the content
        raise e
    for word in header_keywords:  # count occurrences of each word in the header section on the page
        header_keywords[word] = content_words.count(word)
    return header_keywords
