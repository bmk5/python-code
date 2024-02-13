from art import logo
#from replit import clear
print(logo)


def execute(num1, num2, operation):
    if (operation == '+'):
        return num1 + num2

    elif (operation == '-'):
        return num1 - num2

    elif (operation == '*'):
        return num1 * num2

    return num1 / num2


def run_calc(ch, num1):
    if (ch == 'n'):
        num1 = float(input("What's the first number?: "))
        print("+\n-\n*\n/")

    op = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))

    res = execute(float(num1), float(num2), op)
    print(f" {num1} {op} {num2} = {res}")
    return res


currRes = 0
#flag = 0
status = 'n'

while True:
    if (status == 'n'):
        # if (flag == 1):
        #     clear()
        currRes = run_calc(status, 0)
    else:
        currRes = run_calc(status, currRes)

    flag = 1

    status = input(f"Type y to continue calculating with {currRes}, or type n to start a new calculation: ")

