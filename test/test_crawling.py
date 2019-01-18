from unittest import TestCase, main
from src.crawling import Browser, get_title_parsed, get_page_parsed, get_remove_hwa


class TestCrawling(TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    
    def test_browser(self):
        browser = Browser()
        self.assertEqual(35, len(browser.read_page()['images']))

    def test_browser_choose_option(self):
        browser = Browser()
        readen = browser.read_page(page_id='427271')
        first_page_info = [one_page_info for one_page_info in readen['page_info'] if one_page_info[1] == '1'][0]
        readen2 = browser.choose_option(first_page_info[0])
        self.assertEqual(39, len(readen2['images']))

    def test_print_result(self):
        browser = Browser()
        print(browser.read_page())



    def test_get_title(self):
        self.assertEqual(
            ['뭔가 다른 이야기', '3'],
            get_title_parsed("뭔가 다른 이야기 3화")
        )

    def test_get_page_parsed_0(self):
        self.assertEqual(0, get_page_parsed('page-0'))

    def test_get_page_parsed_32(self):
        self.assertEqual(32, get_page_parsed('page-32'))

    def test_getpage_parsed_none(self):
        self.assertEqual(None, get_page_parsed('page-'))

    def test_get_remove_hwa_13(self):
        self.assertEqual('13', get_remove_hwa("13화"))

    def test_get_remove_hwa_number_space(self):
        self.assertEqual('13', get_remove_hwa("13     화"))

    def test_get_remove_hwa_dot(self):
        self.assertEqual('13.5', get_remove_hwa("13.5     화"))

    def test_get_remove_hwa_dash(self):
        self.assertEqual('13-5', get_remove_hwa(" 13-5     화"))

    def test_get_remove_hwa_none(self):
        self.assertEqual(None, get_remove_hwa("화"))

if __name__ == '__main__':
    main()
