def square_of_number(number):
    for i in range(1,number+1):
        print(i*i)

square_of_number(10)
print('************************************************')

def odd_numbers(number):
    for i in range(1,number+1,2):
        print(i)

odd_numbers(10)
print('************************************************')



def even_numbers(number):
    for i in range(2,number+1,2):
        print(i)

even_numbers(10)
print('************************************************')

def reverse_order(number):
    for i in range(number,1,-1):
        print(i)

reverse_order(10)

