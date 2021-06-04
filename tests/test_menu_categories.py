from actions.shop_actions import ShopActions
from core.utils import datafile_handler as data_file
from facades import menu_facade as menu
from facades import menu_categories_facade as menu_categories
import pytest
import datetime
from time import sleep

#Prueba 2.-  Verificar los elementos del menú de categorías 
@pytest.mark.parametrize('title_category, products_by_category',data_file.get_data('./input_data/menu_category.csv'))
def test_menu_categories(title_category, products_by_category):
    global test_case_name
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S') #20210511_211246
    test_case_name = 'test_menu_categories {}'.format(timestamp)

    menu.click_menu_option_shop()
    menu_categories.view_menu_options(title_category, products_by_category)

#Metodo que se ejecuta siempre, despues de cada caso de prueba.
#Cierra la instancia del navegador
def teardown():
    shop_actions = ShopActions()
    shop_actions.save_screenshot(test_case_name)
    shop_actions.close_browser()

