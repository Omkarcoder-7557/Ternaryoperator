#program for cheking no is even or odd
n=int(input("enter number:"))
#logic
res="invalid input" if (n<0) else "even" if (n%2==0) else "odd"
#showing
print("the number is {}".format(res))