import string

string_value='chittesh'
for i in string_value:
    print(i)

#in operation
print('a' in string.ascii_letters)      #True
print('1' in string.digits)             #True
print(',' in string.punctuation)        #True
print('a' in 'basdad')                  #True

#method to print all CApital alapabets
for i in string.printable:
    if(i in string.ascii_uppercase):
        print(i)

#Split method
paragraph = 'Hello My Name is slim sheddy'
for i in paragraph.split(' '):
    print(i)

