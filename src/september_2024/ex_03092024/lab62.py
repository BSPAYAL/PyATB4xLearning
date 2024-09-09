class VWOLoginPage():

    def __init__(self,email_arg,password_arg):
        self.email_arg = email_arg
        self.password_arg = password_arg


    def login_confirm(self):
        if self.email_arg == "pramod@gmail.com" and self.password_arg == "Pass123":
            print("Login Allowed")

        else:
            print("Login NOt Allowed")

obj = VWOLoginPage("phhh","jjj")
obj.login_confirm()

email_arg = input("enter the email :")
password_arg = input("enter the pwd :")
new_obj = VWOLoginPage(email_arg,password_arg)
new_obj.login_confirm()