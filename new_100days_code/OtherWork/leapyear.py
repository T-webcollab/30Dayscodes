#Adding the numbers
def add(n1, n2):
    return n1 + n2
#subtracting the numbers
def subt(n1, n2):
    return n1 - n2
#multiplyinig the numbers
def multi(n1, n2):
    return n1 * n2
# dividing the numbers
def divide(n1, n2):
    return n1 / n2



def calculator():
    end=False
    first_num=float(input("Enter the first number: "))
    while end!=True:
        choice=input("1. +\n2. -\n3. *\n4. /\n Enter here : ")
        if  choice=="+":
            second_num=float(input("Enter the second number: "))
            my_favorite_cal=add(first_num,second_num)
            print(my_favorite_cal)

        elif choice=="-":
            second_num=float(input("Enter the second number: "))
            my_favorite_cal=subt(first_num,second_num)
            print(my_favorite_cal)
        elif choice=="*":
            second_num=float(input("Enter the second number: "))
            my_favorite_cal=multi(first_num,second_num)
            print(my_favorite_cal)
        else:
            second_num=float(input('Enter the second number'))
            my_favorite_cal=divide(first_num,second_num)
            print(my_favorite_cal)
        
        choice2=input("Do you want to continue with the output or want a new calculation: Y or N").lower()
        if choice2=="y":
            first_num=my_favorite_cal
        else:
            end=True
            calculator()
calculator()

        
    