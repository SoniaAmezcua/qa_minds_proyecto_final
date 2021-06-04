class ShopPage():

    def get_nav(self):
        return 'woocommerce-breadcrumb' #class name

    def get_menu(self):
        return '//a[contains (text(), "Home")]'

    def get_submenu(self):
        return '//nav[contains (text(), "Shop")]'

    def get_select_order_by(self):
        return 'orderby' #name

    def get_title_book(self, title):
        return '//h3[contains (text(), "{}")]'.format(title)

    def get_slider_filter_price(self):
        return 'price_slider_wrapper' #class name

    def get_left_slide(self):
        return '//span[contains (@class, "ui-state-default")][1]'

    def get_right_slide(self):
        return '//span[contains (@class, "ui-state-default")][2]'

    def get_price_rigth(self):
        return '//span[contains (@class, "from")]'

    def get_price_left(self):
        return '//span[contains (@class, "to")]'

    def get_percentage_filter_price(self):
        return '//span[contains (@style, "left: 100%;")]'

    def get_button_filter(self):
        return '//button[contains (text(), "Filter")]'
    
    def get_books(self):
        return '//h3'