#largest among the two no
a=float(input("enter first number:"))
b=float(input("enter second number:"))
# logic
big=a if a>b else b
#showing the result
print("({},{}) greter is ={}".format(a,b,big))