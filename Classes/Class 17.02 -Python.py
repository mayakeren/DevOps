print("Hi_Maya")
x = 10
y = 5.1
z = "Maya"
print(x)
print(y)
print(z)
print(5 + 4)
print(x, z)
print(str(x) + z)
f = 4
g = 7
print(f * g)
print(f / g)
print(f - g)
# combining string with numeric, use str or comma.
print("My age is:" + str(36))

if x > 2:
    print('x is bigger')
    # if the first doesn't exist- it won't check the second.
    if 2 < x:
        print('2 is smaller')
if x > 2:
    print('x is bigger')
    if 11 < x:
        print('11 is smaller')
a = 15
b = 2
# Multi condition - which will be evaluated in the same statement:
# Below both condition have to return true using *and*
if (a > b and a >10):
    print('a is bigger than b and 10')
# Below only one condition have to return true using *or*
if (a > b or a > 10):
    print('a is bigger than b and 10')
# Else can be added to if condition
if x > 2:
    print('x is bigger')
else:
    print('x is smaller')

m = 52
n = 99
if (m > n):
    print(m)
else:
    print(n)
if (m > n):
    print('m is bigger')
else:
    print('n is bigger')
if (m > n and m > 20):
    print('success')
if ((m * 2) > (n / 5)):
    print('great math')
# Elif always comes after if. else comes after both. as soon as one condition is met, the rest will not be tested.
a = 1
b = 2
if a >b:
    print('a is bigger')
elif a==b:
    print('equals')
elif a!=b:
    print('not equals')
else:
    print('none')

# Keyboard input. Makes the program keep running and waiting for input + enter in order to print.
name = input('Please enter name: ')
print('Hi', name)
number = int(input('What is your age? '))
if (number > 18):
    print('Adult')


password ="12345"
user_password = input('Enter your password ')
if user_password==password:
    print('Logged in')
elif user_password!=password:
    print('Access denied')

Age = int(input('How old are you? '))
Hight- int(input('How tall are you? '))
if Age > 12 and Hight > 160:
    print('OK')