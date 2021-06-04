class LoginPage():

    def get_title(self):
        return '//h2[text() = "Login"]'

    def get_label_username(self):
        return '//label[@for = "username"]'

    def get_field_username(self):
        return 'username' #id

    def get_label_password(self):
        return '//label[@for = "password"]'
    
    def get_field_password(self):
        return 'password' #id

    def get_button_login(self):
        return 'login' #name

    def get_message(self, message, user):
        return '//p[contains (text(), "{}")] and //strong[contains (text(), "{}")]'.format(message, user)
    


    

    