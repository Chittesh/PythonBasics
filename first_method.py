def hello_world():
    print('hello world')
    print('hello world')

#hello_world()

def for_loop(times):
    for i in range(times):
        print('hello world')
# times output
def for_loop_with_range(times):
    for i in range(1, times):
        print('hello world')
# times-1 output
def for_loop_with_range_two(times):
    for i in range(1, times+1):
        print('hello world')
# times output

for_loop(5)
print('*****************************')
for_loop_with_range(5)
print('*****************************')
for_loop_with_range_two(5)