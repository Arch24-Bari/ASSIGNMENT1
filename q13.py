curr_yr=int(input('Enter current year='))
b_yr=int(input('Enter birth year='))
a=curr_yr-b_yr
ques=input(f'Have you celebrated your birthday in {curr_yr}?--')
if (ques.upper()=='YES'):
    print("age=",a)
elif (ques.upper()=='NO'):
    print("age=",a-1)
else:
    print('age cannot be found, enter either yes or no,run the program again')
