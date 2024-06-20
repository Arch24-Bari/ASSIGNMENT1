def fibo(n):
    if n<0:
       print("Invalid input")
    elif n==1 or n==2:
      return 1
    else:
       return fibo(n-1)+fibo(n-2)

n=int(input("Enter the no.:"))
print("The first",n,"nos. in the sequence:",fibo(n))
