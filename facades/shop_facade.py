from actions.shop_actions import ShopActions

def shop_order_by(value, text, title_book):
    shop_actions = ShopActions()    
    shop_actions.verify_nav()
    shop_actions.verify_select_order_by()
    shop_actions.get_order_by(text)
    shop_actions.verify_title_book(title_book)

def shop_filter_by_price(price, lst_expected_books):
    shop_actions = ShopActions()    
    shop_actions.verify_nav()
    shop_actions.verify_slider_filter_price()
    shop_actions.set_slider_filter_price(price)
    shop_actions.verify_filter_button()
    shop_actions.click_on_button_filter()
    shop_actions.verify_list_books(lst_expected_books)

def shop_filter_by_category(lst_expected_books):
    shop_actions = ShopActions()    
    shop_actions.verify_list_books(lst_expected_books)

    





   
    
  


    
