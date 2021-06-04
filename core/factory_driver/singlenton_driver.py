from core.factory_driver import factory_driver

class SinglentonDriver():

    __instance = None

    def __init__(self):
        """
            This method doesn't be used! To create/get an instance of Driver use 'get_instance()'
            :raise RuntimeError()
        """
        raise RuntimeError('Use get_instance() instead')

    @classmethod
    def get_instance(cls):
        """
            Singleton pattern to create an instance of WebDriver in case that doesn't exist. 
            If exist an instance, return the same.
            :return: WebDriver
        """
        if cls.__instance is None:
            cls.__instance = factory_driver.get_driver()
        return cls.__instance


    @classmethod
    def close_driver(cls):
        """
            A method that close driver and set the instance at None.
        """
        if cls.__instance is not None:
            cls.__instance.quit()
            cls.__instance=None

