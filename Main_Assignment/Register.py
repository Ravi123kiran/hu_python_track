from openpyxl import *
class Register:
    def Register_user(self):
        print("****Create new Account*****\n")
        name = input("Enter the name")
        email = input("Enter the email")
        password = input("Enter the password")
        phone = int(input("Enter the Phone number"))
        age = int(input("Enter the age"))
        file = "PythonData.xlsx"
        workBook = load_workbook(file)
        workSheet = workBook['Sheet1']
        li = [name, email, password, phone, age]
        result = []
        i = -1
        for row in workSheet:
            l = []
            for col in row:
                l.append(col.value)
            result.append(l)
            i += 1
        result.append(li)
        print(result)
        workSheet.insert_rows(i)

        i = 0
        for row in workSheet:
            j = 0
            for index, col in enumerate(row):
                col.value = result[i][j]
                j += 1
            i += 1
        workBook.save("PythonData.xlsx")