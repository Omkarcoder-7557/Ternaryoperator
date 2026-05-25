#program for cheking is this is palindrome
word = input("enter a word:")
#logic
res="palindrome" if word==word[::-1] else "not palindrome"
#showing
print("the word is {}".format(res))