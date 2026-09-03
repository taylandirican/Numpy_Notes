import numpy as np

# 1
np_array = np.array([10, 15, 30, 45, 60])
print(np_array)

# 2
np_array = np.arange(5, 15)
print(np_array)

# 3
np_array = np.arange(50, 100, 5)
print(np_array)

# 4
np_array = np.zeros(10)
print(np_array)

# 5
np_array = np.ones(10)
print(np_array)

# 6
np_array = np.linspace(0, 100, 5)
print(np_array)

# 7
np_array = np.random.randint(10, 30, 5)
print(np_array)

# 8
np_array = np.random.randn(10)
print(np_array)

# 9
np_array = np.random.randint(10, 50, 15)
np_multi = np_array.reshape(3, 5)
print(np_multi)

# 10
np_multi_satır = np_multi.sum(axis=1)
np_multi_sutun = np_multi.sum(axis=0)

print(np_multi_satır)
print(np_multi_sutun)

# 11
print(np_multi.max())
print(np_multi.min())
print(np_multi.mean())

# 12
print(np_multi.argmax())

# 13
np_array2 = np.arange(10, 20)
print(np_array2[:3])

# 14
np_array2_reverse = np.flip(np_array2)
print(np_array2_reverse)

# 15
print(np_multi[0, :])

# 17
print(np_multi[1, 2])

# 18
np_multi_kare = np.square(np_multi)
print(np_multi_kare)

# 19
result = np_multi[np_multi % 2 == 0]
result = result[result > 0]
print(result)
