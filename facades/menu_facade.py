from actions.menu_actions import MenuActions 

def view_menu_option(title):
    menu_actions = MenuActions()
    menu_actions.verify_menu()
    menu_actions.verify_menu_title(title)
    
def click_menu_option(title):
    menu_actions = MenuActions()
    menu_actions.click_on_menu_option(title)

def click_menu_option_shop():
    menu_actions = MenuActions()
    menu_actions.click_on_shopping_menu_option()
    
