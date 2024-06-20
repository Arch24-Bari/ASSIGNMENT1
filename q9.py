s=input("ENTER THE STRING:")
sub_s=input('ENTER THE SUBSTRING TO CHECK:')
S=s.upper()
SUB_S=sub_s.upper()
if S.find(SUB_S)==-1:
    print("substring absent in input string")
else:
    print('Substring present in input string')

