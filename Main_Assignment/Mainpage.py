import Admin

class MainPage:

    def main(self):
        while True:
            print("\t\t_________________________________________")
            print("\t\t\t ********Main page********")
            print("\t\t_________________________________________")
            print("\t\t\t1-> Admin")
            print("\t\t\t2-> User")
            print("\t\t\t3-> Exit")
            choice1 = eval(input("\t\t\tEnter your choice(1/2/3):-"))
            if choice1 == 1:
                am = Admin.Admin()
                am.adminscreen()

            # elif choice1 == 2:
            #     user()
            elif choice1 == 3:
               exit()
            # else:
            #     print("Invalid input")


mn = MainPage()
mn.main()
