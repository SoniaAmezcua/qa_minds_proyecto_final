class MenuPage():

    def get_menu(self):
        return 'main-nav' #ID

    def get_option_menu(self, option):
        return '//a[text() = "{}"]'.format(option)

    def get_option_menu_start_shopping(self):
        return '//a[contains (@title, "Start shopping")]'

    

    
    
        