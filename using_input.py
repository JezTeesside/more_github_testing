try:
    a = int(input("Enter first no "))
    b = int(input("Enter second no "))
    print(f"sum of {a} and {b} is {a+b}")
    print(f"difference of {a} and {b} is {a-b}")
    print(f"multiplication of {a} and {b} is {a*b}")
    print(f"division of {a} and {b} is {a/b}")
except ValueError:
    print("inputs should be numbers")
except ZeroDivisionError:
    print("second no can't be 0")
    