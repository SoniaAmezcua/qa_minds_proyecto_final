from pages.login_page import LoginPage as page
from core.base_actions import BaseActions
from selenium.webdriver.common.by import By
from core.assertion import assertions

class LoginActions(BaseActions):

    def __init__(self) -> None:
        self._page = page()

    def verify_title(self):
        assertions.assert_true(self.is_visible(By.XPATH, self._page.get_title()),'El titulo no esta visible'.format())
    
    def verify_label_email(self, label):
        assertions.assert_true(self.is_visible(By.XPATH, self._page.get_label_username()),'La etiqueta {} no esta visible'.format(label))
        resultado = self.get_text_element(By.XPATH, self._page.get_label_username())
        assertions.assert_equal(label, resultado , 'Etiqueta incorrecta, esperado:{} resultado:{}'.format(label, resultado))

    def verify_label_password(self, label):
        assertions.assert_true(self.is_visible(By.XPATH, self._page.get_label_password()),'La etiqueta {} no esta visible'.format(label))
        resultado = self.get_text_element(By.XPATH, self._page.get_label_password())
        assertions.assert_equal(label, resultado , 'Etiqueta incorrecta, esperado:{} resultado:{}'.format(label, resultado))

    def verify_field_email(self, field):
        assertions.assert_true(self.is_visible(By.ID, self._page.get_field_username()),'El campo {} no esta visible'.format(field))

    def verify_field_password(self, field):
        assertions.assert_true(self.is_visible(By.ID, self._page.get_field_password()),'El campo {} no esta visible'.format(field))

    def verify_button(self):
        assertions.assert_true(self.is_visible(By.NAME, self._page.get_button_login()),'El boton no esta visible')

    def set_data(self, email, password):
        self.input_send_keys(By.ID, self._page.get_field_username(), email)
        self.input_send_keys(By.ID, self._page.get_field_password(), password)

    def verify_button_clickable(self):
        assertions.assert_true(self.is_clickable(By.NAME,self._page.get_button_login(),5),'El botton no es clickable')

    def click_on_button(self):       
        self.click_element(By.NAME,self._page.get_button_login())

    def verify_field_message_login(self, message, user):
        assertions.assert_true(self._page.get_message(message, user),'El mensaje {} {} no esta visible'.format(message, user))

   

