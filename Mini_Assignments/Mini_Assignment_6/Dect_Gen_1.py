def deco(func):
    def inner(num1,num2):
        func(num1,num2)
        func(num1,num2)
    return inner
@deco
def multiply(n1, n2):
    print(n1 * n2)


n1 = int(input('Enter first number: '))
n2 = int(input('Enter second number: '))

multiply(n1, n2)







#def multiply(a,b):
#     print(a*b)
# def smart(func):
#     def inner(a,b):
#         for i in range(2):
#             print(a*b)
#         return func
#     return inner
# multiply1=smart(multiply)
# multiply1(1,2)



