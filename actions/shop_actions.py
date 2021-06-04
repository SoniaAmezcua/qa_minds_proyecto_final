from pages.shop_page import ShopPage as page
from core.base_actions import BaseActions
from selenium.webdriver.common.by import By
from core.assertion import assertions

class ShopActions(BaseActions):

    def __init__(self) -> None:
        self._page = page()

    def verify_nav(self):
        assertions.assert_true(self.is_visible(By.CLASS_NAME, self._page.get_nav()),'La sección de navegación no esta visible')
        assertions.assert_true(self.is_visible(By.XPATH, self._page.get_menu()),'La opción Home del menu no esta visible')
        assertions.assert_true(self.is_visible(By.XPATH, self._page.get_submenu()),'La opción Shop del menu no esta visible')

    def verify_select_order_by(self):
        assertions.assert_true(self.is_visible(By.NAME, self._page.get_select_order_by()),'El select para ordenar no esta visible')
    
    def get_order_by(self, text):
        self.get_select_by_text(By.NAME, self._page.get_select_order_by(), text)
        self.scroll_down(0,500)
       
    def verify_slider_filter_price(self):
        assertions.assert_true(self.is_visible(By.CLASS_NAME, self._page.get_slider_filter_price()),'El el slider para filtrar por precio no esta visible')
        
    def set_slider_filter_price(self, price_from):
        price = 0 
        price_from_ini = self.get_text_element(By.XPATH, self._page.get_price_rigth())[1:]
        price_to_ini = self.get_text_element(By.XPATH, self._page.get_price_left())[1:]
        if price_from >= price_from_ini and price_from <= price_to_ini:        
            while int(price) < int(price_from):
                self.move_to_slide(By.XPATH, self._page.get_left_slide(), 2, 0)
                price = self.get_text_element(By.XPATH, self._page.get_price_rigth())
                price = price[1:]       
    

    """def set_slider_filter_price(self, porcentage_change):
        #self.scroll_left(By.XPATH, self._page.get_percentage_filter_price())
        self.change_propierty_style(By.XPATH, self._page.get_percentage_filter_price(), "style", "left: {}%;".format(porcentage_change))
    """
    def verify_filter_button(self):
        assertions.assert_true(self.is_visible(By.XPATH, self._page.get_button_filter()),'El boton Filter no esta visible')
    
    def click_on_button_filter(self):
        self.get_element(By.XPATH,self._page.get_button_filter()).click()
        self.scroll_down(0,500)

    def verify_title_book(self, title_book):
        assertions.assert_true(self.is_visible(By.XPATH, self._page.get_title_book(title_book)),'El titulo del libro {} no esta visible'.format(title_book))
       
    def verify_list_books(self, lst_expected_books):
        list_books = self.get_elements(By.XPATH, self._page.get_books())
        lst_book_text = []

        for book_actual in list_books:
            title_actual_text = self.get_text_element(By.XPATH, self._page.get_title_book(book_actual.text))
            lst_book_text.append(title_actual_text)

        assertions.assert_equal(set(lst_book_text), set(lst_expected_books),'No se muestran todos los libros esperados {}, resusltado {}'. format(lst_expected_books, lst_book_text))

       

        