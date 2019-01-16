from unittest import TestCase, main
from src.crawling import Browser


class TestCrawling(TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    
    def test_db_session_close(self):
        browser = Browser()
        self.assertEqual(35, len(browser.readPage()['images']))

if __name__ == '__main__':
    main()
