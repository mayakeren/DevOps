#A.
first = 7
second = 44.3
print(first + second)
print(first * second)
print(second / first)

#B.
a = 8
a = 17
a= 9
b = 6
c = a+b
b = c+a
b = 8
print(a, b, c)

#C.
# No, but there should be a space before = in the second one
name = "john"
print(name)
name='john'
print(name)

#Suggested edit: add str
my_number = 5+5
print("result is: "+ str(my_number))

#D. Output is 7
x = 5
y = 2.36
print(x+int(y))

#E.
x = 17
y = 3
if x > y:
    print('BIG')
else:
    print('small')

#F.
s = int(3)
if s!=1:
    print('- 1=summer')
if s>2:
    print('- 2=winter')
if s==3:
    print('- 3=fall')
if s<4:
    print('- 4=spring')
elif s==4:
    print('all seasons')

#Challange:
a = 8
b = '123'
print(str(a) + b)