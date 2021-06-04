from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.remote.webelement import WebElement
from core.factory_driver.singlenton_driver import SinglentonDriver
from core.factory_driver import factory_driver_wait as f_driver_w
import core.utils.config_helper as config
from selenium.webdriver.support import  expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains

import datetime


class BaseActions():

    def _get_driver(self):
        return SinglentonDriver.get_instance()

    def close_browser(self):
        SinglentonDriver.close_driver()

    def save_screenshot(self, filename=datetime.datetime.now().strftime('%Y%m%d_%H%M%S')):
        self._get_driver().save_screenshot('{}{}.png'.format(config.get_path_screenshots(),filename))

    # Método para limpiar un input
    def clear_input(self, by, locator):
        self._get_driver().find_element(by,locator).clear()

    # Método para escribir en INPUTS
    def input_send_keys(self, by, locator, text):
        self._get_driver().find_element(by,locator).send_keys(text)
    
    # Método para hacer clic a un elemento
    def click_element(self, by, locator):
        self._get_driver().find_element(by,locator).click()
    
    # Método para obtener la url actual
    def get_current_url(self):
        return self._get_driver().current_url()

    # Método para retornar el texto de un elemento
    def get_text_element(self, by, locator):
        return self._get_driver().find_element(by,locator).text

    #Método para retornar una lista de elementos
    def get_elements(self, by, locator):
        return self._get_driver().find_elements(by,locator)

    def get_element(self, by, locator) -> WebElement:
        element = None
        try:
            element = self._get_driver().find_element(by,locator)
        except NoSuchElementException as nsee:
            print(nsee)
        return element

    def exist_element(self, by, locator) -> bool:
        exist =  self.get_element(by,locator) != None
        return exist

    def is_visible(self, by, locator) -> bool:
        visible = False
        element = self.get_element(by,locator)
        if element != None:
            visible = element.is_displayed()
        return visible

    def is_clickable(self, by, locator, timeout) -> WebElement:
        w_driver = f_driver_w.get_driver_wait(self._get_driver(),timeout)
        try:
            w_driver.until(ec.element_to_be_clickable((by,locator)))
            return True
        except TimeoutException:
            return False  

    # Método para hacer esperar a que un elemento se encuentre presente
    def wait_element_present(self, by, locator, timeout) -> WebElement:
        w_driver = f_driver_w.get_driver_wait(self._get_driver(),timeout)
        try:
            w_driver.until(ec.presence_of_element_located((by,locator)))
            return True
        except TimeoutException:
            return False

    # Método para seleccionar elemento de una lista (etiqueta select) por el texto visible
    def get_select_by_text (self, by, locator, text) -> WebElement:
        element = None
        try:
            element = Select(self.get_element(by,locator)).select_by_visible_text(text)
        except NoSuchElementException as nsee:
            print(nsee)
        return element

    # Método para seleccionar elemento de una lista (etiqueta select) por el valor
    def get_select_by_value (self, by, locator, value) -> WebElement:
        element = None
        try:
            element = Select(self.get_element(by,locator)).select_by_value(value)
        except NoSuchElementException as nsee:
            print(nsee)
        return element 

    # Método para retornar el texto del primer elemento seleccionado de una lista (select)
    def get_select_by_value (self, by, locator, value) -> WebElement:
        element = None
        try:
            element = Select(self.get_element(by,locator)).first_selected_option.text
        except NoSuchElementException as nsee:
            print(nsee)
        return element   

    # Método para mostrar el estatus (booleano) de un elemento de una lista o checkbox
    def get_selected_status(self, by, locator)  -> bool:
        return self._get_driver().find_element(by,locator).is_selected()
 
    # Método para mostrar el valor de un atributo del elemento    
    def get_attribute_value(self, by, locator, attribute) -> WebElement:
        element = None
        try:
            element = self._get_driver().find_element(by,locator).get_attribute(attribute)

        except NoSuchElementException as nsee:
            print(nsee)
        return element  

    def scroll_down(self, x, y):
        self._get_driver().execute_script("window.scrollTo({}, {});".format(x,y))

    # Método para para cambiar un argumento a un elemento
    def change_propierty_style(self, by, locator, name_atributo, change):
        element = self._get_driver().find_element(by,locator)
        self._get_driver().execute_script("arguments[0].{} = '{}'".format(name_atributo, change), element)
        
    # Método ejecutar código javascript
    def execute_javascript(self, code):
        self._get_driver().execute_script(code)

    # Método para mover slide
    def move_to_slide(self, by, locator, x=0, y=0):
        element = self._get_driver().find_element(by,locator)
        actions = ActionChains(self._get_driver())
        actions.click_and_hold(element).move_by_offset(x,y).release().perform()

    # Método para hacer scroll left
    def scroll_left(self, by, locator):
        element = self._get_driver().find_element(by,locator)
        self._get_driver().execute_script("arguments[0].scrollLeft = arguments[0].offsetWidth", element)

    # Método para hacer scroll right
    def scroll_right(self, by, locator):
        element = self._get_driver().find_element(by,locator)
        self._get_driver().execute_script("arguments[0].scrollRight = arguments[0].offsetWidth", element)

    
    def get_element_location(self, by, locator):
        """ Método para devolver la posición del elemento
            @return {'x', 'y'} (diccionario de datos: int)
        """
        return self._get_driver().find_element(by,locator).location 
        

    def get_element_size(self, by, locator):
        """ Método para devolver la posición del elemento
            @return {'width', 'height'} (diccionario de datos: int)
        """
        return  self._get_driver().find_element(by,locator).location .size

    