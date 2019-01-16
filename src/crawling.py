#!/usr/bin/env python

from selenium import webdriver

from bs4 import BeautifulSoup


class Browser:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('window-size=1920x1080')
        options.add_argument("disable-gpu")
        options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
        options.add_argument("lang=ko_KR")
        self.driver = webdriver.Chrome('/Users/jungseungyang/executable/web_drivers/chromedriver_mac64/chromedriver', chrome_options=options)
        self.driver.implicitly_wait(3)

    def readPage(self, page_id='427271'):
        self.driver.get("https://mangashow.me/bbs/board.php?bo_table=msm_manga&wr_id=" + page_id)
        html_page = self.driver.page_source
        if html_page:
            images_elem = self.driver.find_elements_by_xpath('//*[@id="thema_wrapper"]/div[2]/div/div/div[1]/div[2]/div[3]/img')
            title_elem = self.driver.find_element_by_xpath('//*[@id="thema_wrapper"]/div[2]/div/div/div[1]/div[2]/div[1]/div[1]/h1')
            select_elem = self.driver.find_element_by_xpath('//*[@id="thema_wrapper"]/div[2]/div/div/div[1]/div[2]/div[1]/div[1]/div/select')
            pages_elem = select_elem.find_elements_by_tag_name('option')
            images_detailed = [(image.get_attribute('class'), image.get_attribute('src')) for image in images_elem]
            title = title_elem.text
            pages = [(page.get_attribute('value'), page.text )for page in pages_elem]
            return {
                "images" : images_detailed,
                "title" : title, #???? ???? ???? \d+화
                "select_elem" : select_elem,
                "page_info" : pages
            }
        raise Exception("Read Problem")
