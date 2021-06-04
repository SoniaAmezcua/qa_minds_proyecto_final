from actions.login_actions import LoginActions

def login_facade(label_username,label_password, data_username, data_password, message):
    registratin_actions = LoginActions()    
    registratin_actions.verify_title()
    registratin_actions.verify_label_email(label_username)
    registratin_actions.verify_field_email(label_username)
    registratin_actions.verify_label_password(label_password)
    registratin_actions.verify_field_email(label_password)
    registratin_actions.set_data(data_username,data_password)
    registratin_actions.verify_button()
    registratin_actions.verify_button_clickable()
    registratin_actions.click_on_button()
    user = data_username.split("@")   
    registratin_actions.verify_field_message_login(message, user[0])
   
  


    
