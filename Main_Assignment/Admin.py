from openpyxl import load_workbook


class Admin:
    added_movies = []
    movie_timings={}

    def adminscreen(self):
        username = "ravi"
        password = "ravi123"
        while True:
            Username = input("Enter Username:-")
            Password = input("Enter Password:-")
            if Username == username and Password == password:
                while True:

                    print("-------Admin page-------")
                    print("1--> Add Movie")
                    print("2--> Edit movie")
                    print("3--> Delete Movie")
                    print("4--> Logout")
                    select2 = eval(input("Enter your select(1/2/3/4):-"))
                    if select2 == 1:
                        self.add_movies()
                    elif select2 == 2:
                        self.edit_movies()
                    elif select2 == 3:
                        self.delete_movies()
                    elif select2 == 4:
                        break
                    else:
                        print("Invalid input")
            else:
                print("Wrong Password.")
                print("1--> Try again")
                print("2--> Quit program")
                select = eval(input("Enter your select:-"))
                if select == 2:
                    print("Quitting the program...")
                    break

            break

    def add_movies(self):

        Movies = {"title": " ", "genre": " ", "length": 0, "cast": " ", "director": " ", "rating": 0, "language": " ",
                  "shows": 0, "first_show": 0, "interval": 0, "gap": 0, "capacity": 0}
        timings = []


        movie_name = input("Enter the name of the movie:-")
        movie_name = movie_name.upper()
        Movies.update({"title": movie_name})

        movie_genre = input("Enter the genre:-")
        Movies.update({"genre": movie_genre})

        movie_length = eval(input("Enter the length :-"))
        Movies.update({"length": movie_length})

        movie_cast = input("Enter the cast:-")
        Movies.update({"cast": movie_cast})

        movie_director = input("Enter the director :-")
        Movies.update({"director": movie_director})

        movie_rating = eval(input("Enter the rating :-"))
        Movies.update({"rating": movie_rating})

        movie_lang = input("Enter the language:-")
        Movies.update({"language": movie_lang})

        no_shows = eval(input("Enter number of shows:-"))
        Movies.update({"shows": no_shows})

        capacity = eval(input("Enter seating capacity:- "))
        Movies.update({"capacity": capacity})

        show_hour = int(input("Enter first show hour :-"))

        show_mn = int(input("Enter first show minutes:-"))

        first_show = "{}:{}".format(show_hour, show_mn)

        Movies.update({"first_show": first_show})


        interval = eval(input("Enter interval time:- "))
        Movies.update({"interval": interval})

        gap = eval(input("Enter gap between shows:- "))
        Movies.update({"gap": gap})


        print(Movies)
        self.added_movies.append(Movies)
        total_runtime = movie_length + interval + gap
        hours = total_runtime // 60
        minutes = total_runtime % 60
        time = "{}:{}".format(hours, minutes)
        show_hr_up = show_hour
        show_mn_up = show_mn
        start_time = first_show
        for i in range(no_shows):
            show_hr_up = show_hr_up + hours
            show_mn_up = show_mn_up + minutes
            tempdict = {}
            if (show_mn_up >= 60):
                show_hr_up += 1
                show_mn_up = show_mn_up - 60
            end_time = "{}:{}".format(show_hr_up, show_mn_up)
            st = start_time + "-" + end_time

            tempdict.update({st:capacity})
            timings.append(tempdict)
            temp={movie_name:timings}
            self.movie_timings.update(temp)
            start_time = end_time

        print(self.movie_timings)

    def edit_movies(self):

        if (len(self.added_movies) == 0):
            print("First add the movie!! ")
            self.add_movies()
            return
        for i in range(len(self.added_movies)):
            print(self.added_movies[i]["title"])

        toEditTitle = input("Enter the movie title which you want to be updated")
        if self.added_movies[i]["title"] == toEditTitle:
            cont = "y"
        else:
            self.edit_movies()
            return

        print("Enter which data you want to edit")
        print(
            "1.Genre\n2.Cast\n3.Director\n4.Admin Rating\n5.Language\n6.Length\tTimings\tNumber of Shows\t.First Show\tInterval\tTimeGap\tCapacity")
        while True:
            n = int(input("Enter your select which you want to edit or -1 to exit\n"))

            if (n == -1):
                break
            elif (n == 1):
                new_genre = input("Enter the new genre\n")
                for i in range(len(self.added_movies)):
                    if self.added_movies[i]["title"] == toEditTitle:
                        d = self.added_movies[i]
                        d.update({"genre": new_genre})
                        print("Updated")
                        break

            elif (n == 2):
                new_cast = input("Enter the new cast\n")
                for i in range(len(self.added_movies)):
                    if self.added_movies[i]["title"] == toEditTitle:
                        d = self.added_movies[i]
                        d.update({"cast": new_cast})
                        print("Updated")
                        break
            elif (n == 3):
                new_director = input("Enter the new director\n")
                for i in range(len(self.added_movies)):
                    if self.added_movies[i]["title"] == toEditTitle:
                        d = self.added_movies[i]
                        d.update({"director": new_director})
                        print("Updated")
                        break

            elif (n == 4):
                new_rating = input("Enter the new rating\n")
                for i in range(len(self.added_movies)):
                    if self.added_movies[i]["title"] == toEditTitle:
                        d = self.added_movies[i]
                        d.update({"rating": new_rating})
                        print("Updated")
                        break
            elif (n == 5):
                new_lang = input("Enter the new language\n")
                for i in range(len(self.added_movies)):
                    if self.added_movies[i]["title"] == toEditTitle:
                        d = self.added_movies[i]
                        d.update({"language": new_lang})
                        print("Updated")
                        break

            elif (n == 6):
                new_length =int(input("Enter the new length\n"))
                new_no_shows = int(input("Enter the new no of shows\n"))
                show_hr = int(input("Enter first show hour :-\n"))
                show_mn = int(input("Enter first show minutes:-\n"))
                first_show = "{}:{}".format(show_hr, show_mn)
                new_interval = int(input("Enter the new interval\n"))
                new_gap = int(input("Enter the new gap\n"))
                new_capacity=int(input("enter new capacity\n"))
                timings=[]

                total_runtime = new_length + new_interval + new_gap
                hours = total_runtime // 60
                minutes = total_runtime % 60
                time = "{}:{}".format(hours, minutes)
                show_hr_up = show_hr
                show_mn_up = show_mn
                start_time = first_show
                for i in range(new_no_shows):
                    show_hr_up = show_hr_up + hours
                    show_mn_up = show_mn_up + minutes
                    tempdict={}
                    if (show_mn_up >= 60):
                        show_hr_up += 1
                        show_mn_up = show_mn_up - 60
                    end_time = "{}:{}".format(show_hr_up, show_mn_up)
                    st = start_time + "-" + end_time

                    tempdict.update({st:new_capacity})
                    timings.append(tempdict)
                    temp = {toEditTitle: timings}
                    del self.movie_timings[toEditTitle]
                    self.movie_timings.update(temp)
                    start_time = end_time

                for i in range(len(self.added_movies)):
                    if self.added_movies[i]["title"] == toEditTitle:
                        d = self.added_movies[i]
                        d.update({"length": new_length})
                        d.update({"shows": new_no_shows})
                        d.update({"interval":new_interval})
                        d.update({"gap":new_gap})

                        print("Updated")
                        break

            print(self.added_movies)
            print(self.movie_timings)

    def delete_movies(self):
        if(len(self.added_movies)==0):
            print("first enter the details")
            self.add_movies()
            return 0
        for i in range(len(self.added_movies)):
            print(self.added_movies[i]["title"])
        toDeleteMovie = input("Enter the movie name to be deleted")
        flag=0
        flag1=0
        for i in range(len(self.added_movies)):
            if self.added_movies[i]["title"] == toDeleteMovie:
                del self.added_movies[i]
                flag=1
                flag1=1
                break

        del self.movie_timings[toDeleteMovie]

        if(flag==0):
            print("enter correct details")
            self.delete_movies()
        if(flag1):
            print(self.added_movies)
            print(self.movie_timings)

        def user_rating(self):
            for i in range(len(self.a.added_movies)):
                print(self.a.added_movies[i]["title"])
            movie_name = input("enter the movie name to give the rating")
            for i in range(len(self.a.added_movies)):
                if self.a.added_movies[i]["title"] == movie_name:
                    flag=1
                    mov_rating=eval(input("enter your rating out of 10"))
                    break
            if(flag==0):
                print("enter proper movie title from given list")
            file = "PythonData.xlsx"
            wb = load_workbook(file)
            ws = wb['Sheet2']
            li = [self.email, movie_name, mov_rating]
            final = []
            i = -1
            for row in ws:
                l = []
                for col in row:
                    l.append(col.value)
                final.append(l)
                i += 1
            final.append(li)
            # print(final)
            ws.insert_rows(i)

            i = 0
            for row in ws:
                j = 0
                for index, col in enumerate(row):
                    col.value = final[i][j]
                    j += 1
                i += 1
            wb.save("pythonData.xlsx")