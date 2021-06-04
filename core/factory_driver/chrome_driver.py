from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
import core.utils.config_helper as config

CHROME_INCOGNITO = 'incognito'
CHROME_HEADLESS = 'headless'

def create_driver():
    chrome_options = webdriver.ChromeOptions()
    if config.get_incognito_mode():
        chrome_options.add_argument(CHROME_INCOGNITO)
    if config.get_headless_mode():    
        chrome_options.add_argument(CHROME_HEADLESS)
    driver = webdriver.Chrome(options=chrome_options,executable_path=config.get_driver_path())
    return driver