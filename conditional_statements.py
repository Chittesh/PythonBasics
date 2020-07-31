x_string=input("Enter a number")
x=int(x_string)
if x > 2:
    print(f'{x} is greater than 2')
else:
    print(f'{x} is smaller than 2')

#Simple form of if else
#variable = return value 1 if conditon else return value 2
condtion = (f'{x} is greater than 2') if x > 2 else (f'{x} is smaller than 2')
print(condtion)

#elif keyword
if x > 2:
    print(f'{x} is greater than 2')
elif x > 3:
    print(f'{x} is greater than 3')
else:
    print(f'{x} is smaller than 2')


i = 45
print(bool(i))      #True
print(bool(-45))    #True
print(bool(0))      #False
print(str(""))      #False
print(float(0.0))   #False



