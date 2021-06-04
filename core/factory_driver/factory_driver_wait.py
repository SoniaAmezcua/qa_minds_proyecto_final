from selenium.webdriver.support.wait import WebDriverWait
from core.utils import config_helper as config

config.load_config()

def get_driver_wait(driver,timeout):
    w_driver = WebDriverWait(driver,timeout)
    return w_driver

def get_driver_wait_small(driver):
    w_driver = WebDriverWait(driver,config.get_explicit_wait_small())
    return w_driver

def get_driver_wait_medium(driver):
    w_driver = WebDriverWait(driver,config.get_explicit_wait_medium())
    return w_driver

def get_driver_wait_large(driver):
    w_driver = WebDriverWait(driver,config.get_explicit_wait_large())
    return w_driver