print ('Enter 2 string inputs:-')
a=input('1st:')
b=input('2nd:')
p=sorted(a.upper())
q=sorted(b.upper())
if (p==q):
    print("the input words are anagrams of each other!")
else:
    print("Not anagrams of each other, try again!")
