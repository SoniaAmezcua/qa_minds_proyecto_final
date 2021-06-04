from actions.menu_categories_actions import MenuCategoriesActions 

def view_menu_options(title, count):
    menu_actions = MenuCategoriesActions()
    menu_actions.verify_menu_cartegories()
    menu_actions.verify_title_refine()
    menu_actions.verify_title_product_categories()
    menu_actions.verify_title_product_category(title)
    menu_actions.verify_count_product_category(title, count)
    
def click_menu_option_category(title):
    menu_actions = MenuCategoriesActions()
    menu_actions.verify_title_product_category(title)
    menu_actions.click_on_menu_option(title)


