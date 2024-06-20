
lst=[]
n=int(input("Enter no. of elements/nos. to be considered:"))
print('Given below is the list of nos. we need to input to form the list(input over different lines)')
for i in range(0,n):
    ele=input()
    lst.append(ele)
print('this is the list:',lst)
occ=input("Enter which element's occurence frequency to find:")
print(f"counted occurence of {occ} in {lst} is {lst.count(occ)}")
