import time
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

from PageElements import SearchHelper
from config import config


class Tests(TestCase):
    def setUp(self) -> None:
        profile_path = config["profile_path"]
        options = Options()
        options.set_preference('profile', profile_path)
        service = Service(config['firefox_webdriver'])
        self.browser = webdriver.Firefox(service=service, options=options)


    def test_search(self):
        main_page = SearchHelper(self.browser)
        main_page.go_to_site()
        main_page.enter_word("платье")
        main_page.click_on_the_search_button()
        text = main_page.find_title()
        assert "повседневные платья" == text.lower()
        self.browser.close()

    def test_navbar(self):
        main_page = SearchHelper(self.browser)
        main_page.go_to_site()
        elements = main_page.check_nav_bar()
        assert "Новинки" and "Одежда" in elements
        self.browser.close()

    def test_shop_bag(self):
        main_page = SearchHelper(self.browser)
        main_page.go_to_site()
        main_page.click_on_bag_shop()
        text = main_page.show_bag_shop()
        assert "корзина пуста" == text.lower()
        self.browser.close()
