from pages.menu_product_categories import MenuProductCategoriesPage as page
from core.base_actions import BaseActions
from selenium.webdriver.common.by import By
from core.assertion import assertions

class MenuCategoriesActions(BaseActions):

    def __init__(self) -> None:
        self._page = page()

    def verify_menu_cartegories(self):
        assertions.assert_true(self.is_visible(By.ID,self._page.get_menu()),'El menu no es visible')

    def verify_title_refine(self):
        assertions.assert_true(self.is_visible(By.XPATH,self._page.get_title_refine_by()), \
            'El titulo refine by no esta visible')
        
    def verify_title_product_categories(self):
        assertions.assert_true(self.is_visible(By.XPATH,self._page.get_title_product_categories()), \
            'El titulo product categories no esta visible')

    def verify_title_product_category(self, option_menu):
        assertions.assert_true(self.is_visible(By.XPATH,self._page.get_option_menu_category(option_menu)), \
            'La opcion {} no esta visible'.format(option_menu))

    def verify_count_product_category(self, option_menu, count):
         assertions.assert_true(self._page.get_option_menu_count(option_menu, count), \
            'El conteo de la categoria {} es incorrecto'.format(option_menu))
  
    def click_on_menu_option(self, option_menu):
        self.get_element(By.XPATH,self._page.get_option_menu_category(option_menu)).click()

