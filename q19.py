test_str = input("enter sentence:")

# printing original string
print("The original string is : " + test_str)

# initializing punctuations string
punc = '''!()-[]{};:'",<>.?@#$%^&*_~'''
res = " "

for ele in test_str:
    if ele not in punc:
        res += ele

# printing result

print("The string after punctuation filter : " + res)
