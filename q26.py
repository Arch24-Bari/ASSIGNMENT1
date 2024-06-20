str1=input("Input the string(in lowercase):")
str2=str1.lower()

Subpref=input('Enter prefix to check:')
subpref=Subpref.lower()
Subsuff=input('Enter suffix to check:')
subsuff=Subsuff.lower()
if (str2.startswith(subpref)==True):
    print('Prefix is present')
else:
        print('Prefix is absent')
if (str2.endswith(subsuff)==True):
    print('Suffix is present')
else:
        print('Suffix is absent')
