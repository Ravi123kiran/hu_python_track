import Admin
import Register
import User

class Main_page:

     def main(self):
        while True:

            print("-------Main Screen-------")
            print("1-> Admin")
            print("2-> RegisterUser")
            print("3-> Userlogin")
            print("4-> Exit")
            select1 = eval(input("Enter your select(1/2/3):-"))
            if select1 == 1:
                ad = Admin.Admin()
                ad.adminscreen()
            elif select1 == 2:
                r=Register.Register()
                r.Register_user()
            elif select1 == 3:
                u=User.User()
                u.user_login()
            elif select1 == 4:
                exit()
            else:
               print("Invalid input")
mn = Main_page()
mn.main()
