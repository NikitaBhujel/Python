try:
    x=int(input("Enter number:"))
    ans=10/x
except ZeroDivisionError:
    print(f"Divide by 0 is not allowed.")
else:
    print(f"Ans={ans}")
finally:
    print("Division successful")
