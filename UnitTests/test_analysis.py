from unittest import TestCase

from analysis import analyse_article, get_document, get_header_words, get_content_words
from utils import UrlException, ContentException, ConnectionException


class Test(TestCase):
    urls = [
        "https://www.jetbrains.com/idea/guide/tips/generate-test-methods/",
        "https://www.jetbrains.com/help/pycharm/creating-and-running-your-first-python-project.html",
        "https://www.pythontutorial.net/tkinter/tkinter-object-oriented-window/",
        "https://aszdziennik.pl/143677,zmiesci-sie-ostatnie-slowa-20-latki-zmarlej-w-eksplozji-kosza-na-pranie",
        "https://gazetalubuska.pl/te-lubuskie-miasteczka-staly-sie-wsiami-na-liscie-ponad-20-miejscowosci/ar/c3-17211047",
    ]

    def test_get_document(self):  # test if the document is parsed correctly and is not empty
        for url in self.urls:
            try:
                self.assertIsNotNone(get_document(url))
            except UrlException as e:
                self.fail(str(e))
            except ConnectionException as e:
                self.fail(str(e))

    def test_get_header_words(self):  # test if the header words are parsed correctly and are not empty
        for url in self.urls:
            try:
                self.assertTrue(bool(get_header_words(get_document(url))))
            except ContentException as e:
                self.fail(str(e))

    def test_get_content_words(self):  # test if the content words are parsed correctly and are not empty
        for url in self.urls:
            try:
                self.assertTrue(bool(get_content_words(get_document(url))))
            except ContentException as e:
                self.fail(str(e))

    def test_analyse_article(self):  # test if the analysis returns a result
        for url in self.urls:
            try:
                self.assertTrue(bool(analyse_article(url)))
            except UrlException as e:
                self.fail(str(e))
            except ConnectionException as e:
                self.fail(str(e))
            except ContentException as e:
                self.fail(str(e))
