

def add(a ,b):
    return a + b
def subtract(a , b):
    return a - b
def divide(a , b):
    if b == 0 :
        return None
    else :
     return a / b
def multiply(a, b):
    return a * b
is_running = True
print("WELCOME TO THE CALCULATOR")
while is_running:
    print("1 . ADD")
    print("2 . SUBTRACT")
    print("3 . DIVIDE")
    print("4 . MULTIPLY")
    print("5 . EXIT")
    userchoice = input("ENTER YOUR NUMBER FROM CHOICES :")
    if userchoice.isdigit():
        if userchoice == "5":
            print("THANKS FOR USING US")
            break
        elif userchoice not in ["1","2","3","4"]:
            print("only 1 to 5 choice allowed")
        else :
            try:
                a = float(input("enter your 1st number : "))
                b = float(input("enter your 2nd number : "))
            except ValueError:
                print("ONLY NUMBERS ALLOWED")
                continue
            if userchoice == "1":
                result =(add(a, b))
                print(f"result is {result}")
            elif userchoice == "2":
                result =(subtract(a, b))
                print(f"result is {result}")
            elif userchoice == "3":
                result = divide(a, b)
                if result is not None:
                    print(f"result is {round(result , 2)}")
                else:
                    print("ZERO DIVISIBLE ERROR")
            elif userchoice == "4":
                result =(multiply(a, b))
                print(f"result is {result}")
    else:
        print("ONLY 1 TO 5 NUMBERS ARE ALLOWED")





