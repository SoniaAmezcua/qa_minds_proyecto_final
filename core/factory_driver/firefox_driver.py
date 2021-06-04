from selenium import webdriver
import core.utils.config_helper as config

FIREFOX_PRIVATE = 'browser.privatebrowsing.autostart'

def create_driver():
    ff_options = webdriver.FirefoxOptions()
    ff_profile = webdriver.FirefoxProfile()
    ff_profile.set_preference(FIREFOX_PRIVATE,config.get_incognito_mode())
    ff_options.headless = config.get_headless_mode()
    driver = webdriver.Firefox(executable_path=config.get_driver_path(),firefox_profile=ff_profile,options=ff_options,)
    return driver