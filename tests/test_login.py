from actions.login_actions import LoginActions
from facades import login_facade as login
from core.utils import datafile_handler as data_file
from facades import menu_facade as menu
import datetime
import pytest

#Prueba 1.-  Registro con correo electrónico no válido  
@pytest.mark.parametrize('label_email,label_password,data_email,data_password,message',data_file.get_data('./input_data/login.csv'))
def test_login_success(label_email, label_password, data_email, data_password, message):
    global test_case_name
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S') #20210511_211246
    test_case_name = 'test_login_success {}'.format(timestamp)

    menu.view_menu_option('My Account')
    menu.click_menu_option('My Account')
    login.login_facade(label_email, label_password, data_email, data_password, message)


#Metodo que se ejecuta siempre, despues de cada caso de prueba.
#Cierra la instancia del navegador
def teardown():
    login_actions = LoginActions()
    login_actions.save_screenshot(test_case_name)
    login_actions.close_browser()