import numpy as np

even = np.arange(10)
print(even)

array = np.ones((3, 3), dtype=bool)
print(array)

a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
b = a[a % 2 == 1]
print(b)

c = a - 1
print(c)


d = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10,])

e = d.reshape (5, 2)
print(e)



a1 =np.arange (1,10).reshape (3,3)
b1 = np.arange (10,19).reshape (3,3)
c1 = np.dot (a1, b1)
d1 = np.sum (c1)
print(d1)

array_1 = np.arange(1, 6)
array_2 = np.arange(4, 10)

print(array_2[2:])

array_3 = np.concatenate((array_1, array_2))
print(array_3)


array_4 = np.sort(array_3, axis=None)

print(array_4)

array_5 = array_4 [5:]

print(array_5)

sum = np.sum(array_5)

print(sum)