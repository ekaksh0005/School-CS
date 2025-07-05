try:
    print("Sum of Two Numbers: ")
    x=float(input("Enter a Number: "))
    y=float(input("Enter a Number: "))
    print(x+z)
except ZeroDivisionError:
    print("Division by Zero is not possible")
except NameError:
    print("Z is not defined but",x+y)
finally:
    print("Sum of X & Y is",x+y)
