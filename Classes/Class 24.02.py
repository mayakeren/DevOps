name = 'Maya'
# Statements:

# 1.Loops: For and While
# for: Increment x value by 1 in each iteration, and keep running as long as x is smaller than 5
for x in range(5):
    print(x)
# for loops have a few variations:
#run from a specific index x times:
for x in range(3,5):
    print(x)
#Run from a specific index x times, but increment x in 2 every iteration: first=x, second=range, third=increment.
for x in range(3,8,2):
    print(x)

# while:
password = '12345'
user_password = input('Please enter password ')
while password != user_password:
    user_password = input('Wrong password! Please re-enter password ')

print('Success')

# 2.Break statement: When a break statement is incountered inside a loop, the loop is terminated and program control resumes at the next statement following the loop.
count = 0
while 1 > 0:
    print(count)
    count += 1
    if count >= 5:
        break

# add break to password:
count = 1
password = '12345'
user_password = input('Please enter password ')
while password != user_password:
    if count < 3:
        count = count + 1
        user_password = input('Wrong password! Please re-enter password ')
    else:
        print('Try again in 5 minuets')
        break
# 3.Continue statement: forces an early iteration of the loop. In this example it skips the number 3.
for x in range(5):
    if x == 3:
        continue
    print(x)
# 4. Else in loop:
count = 1
password = '12345'
user_password = input('Please enter password ')
while password != user_password:
    if count < 2:
        count = count + 1
        user_password = input('Wrong password! Please re-enter password ')
    else:
        print('Try again in 5 minuets')
        break
else:
    print('Success')

# 5.Modules (files):

#Functions: starts with def and ends in ()
def main():
    print('hello')

if __name__ == '__main__':
    main()

# OOP
def return_hello():
    return 'Hello'
def print_name(name):
    print(name)
def is_bigger_than_one(num)
    return num > 1

if __name__ == '__main__':
    print(return_hello())
    print_name('Maya')
    print_name('Keren')
    is_bigger_than_one(10)
    is_bigger_than_one(1)

def is_bigger_than_one(num, num2):
    if num > num2:
        return num
    if num2 > num:
        return num2
# another option is to put a default value for num2, so if you enter only 1 value it will enter the default for the second one:
#(num, num2 = 1)

if __name__ == '__main__':
    is_bigger_than_one(10, 5)
    y = is_bigger_than_one(10, 5)
    print(y)
    print(is_bigger_than_one(3, 9))

# Variables: Global variables: not under def, in the module.

#OOP: Packages and imports: see datetime

#Data structures-
# 1.Array
import array as arr
a = arr.array('i',[5, 7, 6])
print(a[0])
print(a[1])
print(a[2])
a[0] = 1
print(a[0])
a.append(8)
print(a[3])
a.pop(0)
print(a[0])
a.insert(0, 8)
print(a[0])
for x in a:
    print(x)
my_list = [5, 'p']
b = 1, 'u'
c = (1, 'u')
