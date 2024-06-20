#Input string and then check frequency by making string ch and s in capital,no case sensitivity
s=input("Enter string data:")
ch=input("Enter substring whose frequency in string to be checked:")
CH=ch.upper()
S=s.upper()
print(f"frequency of {CH} in {S} is",S.count(CH))