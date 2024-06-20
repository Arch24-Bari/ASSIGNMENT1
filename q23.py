

#CONVERT

ans=input(" 'Fahreneit to celsius' or 'Celsius to Fahreneit' conversion: ")
if ans.lower()=="celsius to fahreneit":
#Celsius to Fahreneit conversion, deg means degree
   c=float(input("Enter the temp. in Celsius="))
   f=((c*9)/5) + 32
   print(f"{c} celsius is equivalent to {f} fahreneit")
elif ans.lower()=="fahreneit to celsius":
# Fahreneit to celsius  conversion, deg means degree
    _f=float(input("Enter the temp. in Fahreneit="))
    _c=((_f-32)*5)/ 9
    print(f"{_c} celsius is equivalent to {_f} fahreneit")
else:
    print("run the program again and state your answer according to options given in qoutation marks!!")