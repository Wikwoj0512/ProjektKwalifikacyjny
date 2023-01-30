from unittest import TestCase

import requests

from utils import validate_url, RegEx


class Test(TestCase):
    urls = [
        "https://www.jetbrains.com/idea/guide/tips/generate-test-methods/",
        "https://www.jetbrains.com/help/pycharm/creating-and-running-your-first-python-project.html",
        "https://www.guru99.com/python-regular-expressions-complete-tutorial.html",
        "https://aszdziennik.pl/143677,zmiesci-sie-ostatnie-slowa-20-latki-zmarlej-w-eksplozji-kosza-na-pranie",
        "https://gazetalubuska.pl/te-lubuskie-miasteczka-staly-sie" +
        "-wsiami-na-liscie-ponad-20-miejscowosci/ar/c3-17211047",
    ]  # Validate if correct url is accepted
    bad_urls = [
        "htps://www.jetbrains.com/idea/guide/tips/generate-test-methods/",
        "www.jetbrains/helppycharm/creating-and-running-your-first-python-project.html",
        "http://www.guru99.com\python-r egular-expressions-complete-tutorial.htl",
    ]  # Validate if incorrect url is rejected

    def test_validate_url(self):  # Test the validate_url function
        for url in self.urls:
            self.assertTrue(validate_url(url))
        for url in self.bad_urls:
            self.assertFalse(validate_url(url))


class TestRegEx(TestCase):
    urls = [
        "https://www.jetbrains.com/idea/guide/tips/generate-test-methods/",
        "https://www.jetbrains.com/help/pycharm/creating-and-running-your-first-python-project.html",
        "https://www.guru99.com/python-regular-expressions-complete-tutorial.html",
        "https://aszdziennik.pl/143677,zmiesci-sie-ostatnie-slowa-20-latki-zmarlej-w-eksplozji-kosza-na-pranie",
        "https://gazetalubuska.pl/te-lubuskie-miasteczka-staly-sie-" +
        "wsiami-na-liscie-ponad-20-miejscowosci/ar/c3-17211047",
    ]  # Urls with different checked and correct content

    def test_search(self):  # test search method
        for url in self.urls:
            document = requests.get(url).text
            for pattern in RegEx.patterns:
                self.assertIsNotNone(RegEx.search(pattern, document))

    def test_findall(self):  # test findall method
        for url in self.urls:
            document = requests.get(url).text
            for pattern in RegEx.patterns:
                self.assertIsNotNone(RegEx.findall(pattern, document))

    def test_patterns(self):  # test regex patterns
        self.assertEqual(len(RegEx.patterns), 5)
        for name, pattern in RegEx.patterns.items():
            self.assertIsNotNone(name)
            self.assertIsNotNone(pattern)

        text = """<head><title>Test</title></head><body class='test'><h1>lorem ipsum dolor sit amet</h1>""" \
               """<h1>masa aenaan</h1><script>aenean commodo ligula eget dolor aenean massa""" \
               """</script><p>comodo ligua dorime</p>aaaaaaa</body>"""

        expected = """<h1>lorem ipsum dolor sit amet</h1><h1>masa aenaan</h1>""" \
                   """<script>aenean commodo ligula eget dolor aenean massa</script><p>comodo ligua dorime</p>aaaaaaa"""

        self.assertEqual(RegEx.search("body", text).group(1), expected)
        text = RegEx.search("body", text).group(1)

        expected = ["lorem ipsum dolor sit amet", "masa aenaan"]
        self.assertEqual(RegEx.findall("header", text), expected)

        expected = ["lorem ipsum dolor sit amet", "", "masa aenaan", '', '', "comodo ligua dorime", "aaaaaaa"]

        self.assertEqual(RegEx.findall("content", text), expected)
        text = "!Lorem " \
               "IPsum dolor@!@ sit amet maSsa-aenaan commodo doriMe 222 aaaaaaa"

        expected = ["lorem", "ipsum", "dolor", "sit", "amet", "massa", "aenaan", "commodo", "dorime", "222", "aaaaaaa"]

        self.assertEqual(RegEx.findall("words", text), expected)
