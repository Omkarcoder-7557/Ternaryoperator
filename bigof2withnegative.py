#largest among the two no
a=float(input("enter first number:"))
b=float(input("enter second number:"))
# logic
big=a if a>b else b if b>a else "both are equal"
#showing the result
print("({},{}) ={}".format(a,b,big))