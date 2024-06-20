print("Process: Input list of nos. and then add them using sum(list) ")
lst=[]
n=int(input("Enter no. of elements/nos. to be added:"))
for i in range(0,n):
    ele=int(input("Enter element:"))
    lst.append(ele)
print(f"These are the nos. to be added:{lst}")
print("the sum required:",sum(lst))