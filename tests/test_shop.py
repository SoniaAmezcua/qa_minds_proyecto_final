from actions.shop_actions import ShopActions
from core.utils import datafile_handler as data_file
from facades import menu_facade as menu
from facades import menu_categories_facade as menu_categories
from facades import shop_facade as shop
from input_data.category_product import CATEGORIES_PRODUCT, BOOKS_PRICE
import pytest
import datetime
import random
from time import sleep

#Prueba 3.-  Verificar el selector de ordenamiento   
#@pytest.mark.skip
@pytest.mark.parametrize('value,text,title_book',data_file.get_data('./input_data/order_by_options.csv'))
def test_shop_order_books(value, text, title_book):
    global test_case_name
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S') #20210511_211246
    test_case_name = 'test_shop_order_books {}'.format(timestamp)

    menu.click_menu_option_shop()
    shop.shop_order_by(value, text, title_book)

#Prueba 4.-  Verificar el filtrado por precio
@pytest.mark.parametrize('price,books',list(BOOKS_PRICE.items()))
def test_shop_filter_by_prices(price, books):
    global test_case_name
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S') #20210511_211246
    test_case_name = 'test_shop_filter_by_prices {}'.format(timestamp)

    menu.click_menu_option_shop()
    shop.shop_filter_by_price(price, books)

#@pytest.mark.skip
#Prueba 5.-  Verificar filtrado por categoría
@pytest.mark.parametrize('key,val',list(CATEGORIES_PRODUCT.items()))
def test_shop_filter_by_category(key, val):
    global test_case_name
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S') #20210511_211246
    test_case_name = 'test_shop_filter_by_category {}'.format(timestamp)

    #key, val = random.choice(list(CATEGORIES_PRODUCT.items()))
    menu.click_menu_option_shop()
    menu_categories.click_menu_option_category(key)
    shop.shop_filter_by_category(val)

#Metodo que se ejecuta siempre, despues de cada caso de prueba.
#Cierra la instancia del navegador
def teardown():
    shop_actions = ShopActions()
    shop_actions.save_screenshot(test_case_name)
    shop_actions.close_browser()

