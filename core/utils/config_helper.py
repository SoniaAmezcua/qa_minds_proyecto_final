import json

_config_file_path = './config.json'

_browser = None
_driver_path = None
_incognito = False
_headless_enabled = False
_resolution = None
_page_load = 0
_implict_wait = 2
_explicit_waits = None
_url = None
_screenshots_path = None

def load_config():
    global _browser, _driver_path,_incognito, _headless_enabled, _resolution, _page_load, _implict_wait,_explicit_waits, _url, _screenshots_path
    with open(_config_file_path,'r') as config_file:
        config_data = json.load(config_file)
        _browser = config_data['browser_name']
        _driver_path = config_data['path']
        _incognito = config_data['incognito']
        _headless_enabled = config_data['headless']['enabled']
        _resolution = config_data['headless']['resolution']
        _page_load = config_data['page_load']
        _implict_wait = config_data['implicit_wait']
        _explicit_waits = config_data['explicit_waits']
        _url = config_data['url']
        _screenshots_path = config_data['screenshots']
        
def get_browser_name():
    return _browser

def get_driver_path():
    return _driver_path

def get_incognito_mode():
    return _incognito

def get_headless_mode():
    return _headless_enabled

def get_headless_resolution():
    return _resolution

def get_page_load_timeout():
    return _page_load

def get_implicit_wait():
    return _implict_wait

def get_explicit_wait_small():
    return _explicit_waits['small']

def get_explicit_wait_medium():
    return _explicit_waits['medium']

def get_explicit_wait_large():
    return _explicit_waits['large']

def get_url():
    return _url

def get_path_screenshots():
    return _screenshots_path

