

lst = []
n = int(input("Enter no. of elements/nos. of list to create:"))
print('Given below would be the list of nos. which would be elements of the list, input given over separate lines:-')
for i in range(0, n):
        ele = int(input())
        lst.append(ele)
print(lst)
print(f"Mximum element:{max(lst)} and minimum:{min(lst)}")
