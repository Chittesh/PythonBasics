#Boolean to String
print(str(True))        #True
#String to Boolean expecept '' all other is conveterd to True
print(bool('True'))     #True
print(bool('true'))     #True
print(bool('tru'))      #True
print(bool('tr'))       #True
print(bool('asd'))      #True
print(bool('False'))    #True
print(bool(''))         #False

# Integer to String
print(str(12))          #12
# Float to String
print(str(12.234324))   #12.234324
# String to int
print(int('12'))        #12
print(int('12.3434'))   #ValueError: invalid literal for int() with base 10: '12.3434'
# String to float
print(float('12.3434')) #12.3434
# String to Hexadecimal
print(int('12ad',16))   #4781




