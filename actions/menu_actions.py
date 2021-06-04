from pages.menu_page import MenuPage as page
from core.base_actions import BaseActions
from selenium.webdriver.common.by import By
from core.assertion import assertions

class MenuActions(BaseActions):

    def __init__(self) -> None:
        self._page = page()

    def verify_menu(self):
        assertions.assert_true(self.is_visible(By.ID,self._page.get_menu()),'El menu no es visible')

    def verify_menu_title(self, option_menu):
        assertions.assert_true(self.is_visible(By.XPATH,self._page.get_option_menu(option_menu)), \
            'La opcion {} no esta visible'.format(option_menu))

    def click_on_menu_option(self, option_menu):
        self.get_element(By.XPATH,self._page.get_option_menu(option_menu)).click()

    def click_on_shopping_menu_option(self):
        self.get_element(By.XPATH,self._page.get_option_menu_start_shopping()).click()




"""
    def click_on_elements_option(self):
        self.get_element(By.XPATH,self._page.get_elements_option()).click()

    def verify_element_clickable(self):
        assertions.assert_true(self.is_clickable(By.XPATH,self._page.get_elements_option(),5),'El elemento no es clickable')
    
"""
