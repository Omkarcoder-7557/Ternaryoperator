#the word is vowel word or not
word=input("enter a word:")
#logic
res="vowelword" if "a" in word or "e" in word or "i" in word or "o" in word or "u" in word else "not vowelword"
print("the word is {}".format(res))