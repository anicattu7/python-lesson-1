
while(True):
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    op = input("Select the arithemtic operator to perform the calculation, ( + , - , * , / ) : ")

    if op == "+":
        print("Addition for "+str(num1)+" and "+str(num2)+" "+"is: "+ str(num1+num2))
    elif op == "-":
        print("Subtraction for "+str(num1)+" and "+str(num2)+" "+"is: "+ str(num1-num2))
    elif op == "*":
        print("Subtraction for "+str(num1)+" and "+str(num2)+" "+"is: "+ str(num1*num2))
    elif op == "/":
        print("Subtraction for "+str(num1)+" and "+str(num2)+" "+"is: "+ str(num1/num2))
    else:
        print("Enter the operator from the selection menu please.")
        continue

    cont = (input("Want to continue (y/n)?: "))
    if cont == "y":
        continue
    else:
        break