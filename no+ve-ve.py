#logic for the number is +ve or +ve or zero
n=float(input("enter the number:"))
#logic
res="zero" if(n==0) else "positive" if(n>0) else "negative"
#showing
print("the number is {}".format(res))