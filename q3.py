def fact_numb(num):
    if num<0:
        print("Factorial cannot be evaluated")
    elif num==0 or num==1:
        return 1
    else:
        return num*fact_numb(num-1)

num=int(input('Enter the no.='))
print("factorial of no.=",fact_numb(num))