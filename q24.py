#CALCULATOR

a=int(input("Enter no.="))
b=int(input("Enter other no.="))
op=input("Enter the operator:")

if (op=='+'):
    print(f"{a}+{b}=",a+b)
elif (op=='-'):
    print(f"{a}-{b}=",a-b)
elif (op=='*'):
    print(f"{a}*{b}=",a*b)
elif (op=='/'):
    print(f"{a}/{b}=",a/b)
else:
    print("Enter valid operator!!")