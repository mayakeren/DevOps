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
