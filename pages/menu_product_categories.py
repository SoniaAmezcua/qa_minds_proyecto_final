class MenuProductCategoriesPage():

    def get_menu(self):
        return 'sidebar' #ID

    def get_title_refine_by(self):
        return '//h4[contains (text(), "Refine By >")]'

    def get_title_product_categories(self):
        return '//h4[contains (text(), "Product Categories")]'

    def get_option_menu_category(self, option):
        return '//a[contains (text(), "{}")]'.format(option)
    
    def get_option_menu_count(self, category, count):
        return '//ul/li/a[text()="{}"] and //ul/li/span[text()="({})"]'.format(category,count)
    
        