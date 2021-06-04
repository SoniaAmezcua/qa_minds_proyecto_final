from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.webdriver import WebDriver
import core.utils.config_helper as config
import core.factory_driver.chrome_driver as chrome_driver
import core.factory_driver.firefox_driver as firefox_driver

def get_driver() -> WebDriver :
    config.load_config()
    navegador = config.get_browser_name()
    driver = None
    if navegador == 'chrome':
        driver = chrome_driver.create_driver()
    elif navegador == 'firefox':
        driver = firefox_driver.create_driver()
    else:
        raise Exception('Navegador Invalido')

    if config.get_headless_mode():
        driver.set_window_size(config.get_headless_resolution()['width'],config.get_headless_resolution()['height'])
    else:
        driver.maximize_window()

    driver.set_page_load_timeout(config.get_page_load_timeout())
    driver.implicitly_wait(config.get_implicit_wait())

    try:
        driver.get(config.get_url())
    except Exception as e:
        print(e)
        raise TimeoutException('La pagina web no se cargo en {} segundos'.format(config.get_page_load_timeout()))
    return driver