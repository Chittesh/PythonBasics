#Strongly typed
print(len("String"))
print(len(1)) # error
print(("String").upper())
print((1).upper()) #error

#Dynamically type Language concep
a=1
print(type(a)) #<class 'int'>
a="String"
print(type(a)) #<class 'str'>
a=[1,2]
print(type(a)) #<class 'list'>
a={1,2}
print(type(a)) #<class 'set'>




