from selenium.webdriver.common.by import By

from BasePage import BasePage
from Locators import SearchBarLocators, SearchResultPageLocators, NavbarLocators, ShopBagLocators


class SearchHelper(BasePage):

    def enter_word(self, word):
        search_field = self.find_element(SearchBarLocators.SEARCH_BAR_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def click_on_the_search_button(self):
        return self.find_element(SearchBarLocators.SEARCH_BAR_BUTTON,time=2).click()

    def find_title(self):
        return self.find_element(SearchResultPageLocators.SEARCH_RESULT_HEADING).text

    def check_nav_bar(self):
        all_list = self.find_elements(NavbarLocators.NAVBAR_LIST)
        nav_bar_menu = [x.text for x in all_list if len(x.text) > 0]
        return nav_bar_menu[0].split('\n')

    def click_on_bag_shop(self):
        return self.find_element(ShopBagLocators.SHOP_BAG_BUTTON,time=2).click()

    def show_bag_shop(self):
        return self.find_element(ShopBagLocators.SHOP_BAG_LIST).text