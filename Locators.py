from selenium.webdriver.common.by import By

class YandexSeacrhLocators:
    LOCATOR_YANDEX_SEARCH_FIELD = (By.ID, "text")
    LOCATOR_YANDEX_SEARCH_BUTTON = (By.CLASS_NAME, "search2__button")
    LOCATOR_YANDEX_NAVIGATION_BAR = (By.CSS_SELECTOR, ".service__name")


class SearchBarLocators:
    SEARCH_BAR_FIELD = (By.ID, "search__field_input")
    SEARCH_BAR_BUTTON = (By.CLASS_NAME, "search__field_search")


class SearchResultPageLocators:
    SEARCH_RESULT_HEADING = (By.CLASS_NAME, "catalog__categories_title")
    CART_POPUP_TEXT = (By.CLASS_NAME, "modal-cart")

class NavbarLocators:
    NAVBAR_LIST = (By.CLASS_NAME, "header__nav_desktop")

class ShopBagLocators:
    SHOP_BAG_BUTTON = (By.CLASS_NAME, "link__shopping")
    SHOP_BAG_LIST = (By.CLASS_NAME, "empty")