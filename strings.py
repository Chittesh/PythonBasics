value='string'
print(type(value))                  #<class 'str'>
#upper
print(value.upper())                #STRING
#lower
print(value.lower())                #string
#capital
print(value.capitalize())           #String
#checking is lower
print(value.islower())              #True
#checking is upper
print(value.upper().isupper())      #True
#checking is First letter is capital
print(value.istitle())              #False
print(value.capitalize().istitle()) #True
#checking contains only alphabets
print(value.isalpha())              #True
number='123'
#checking contains only digits
print(number.isdigit())             #True
#checking contains only alphabets and digits
print('asd234'.isalnum())           #True
#checking String ends with
print('Hello World'.endswith('World'))#True
print('Hello World'.startswith('Hel'))#True
#Finds the index of occurance
print('Hello World'.find('Hel'))      #0
print('Hello World'.find('el'))       #1
print('Hello World'.find('z'))        #-1









