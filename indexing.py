import numpy as np

numbers = np.array([0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50])

# result = numbers[6]
# result = numbers[-1]
# result = numbers[1:8]
# result = numbers[1:]
# result = numbers[:8]
# result = numbers[::-1]  # diziyi ters çevirir
# result = numbers[::-2]  # diziyi ikişerli adımlarla ters çevirir

numbers2 = np.array([[0, 5, 10], [15, 20, 25], [50, 75, 85]])

result = numbers2[2, 2]  # 3. satır 3. sütundaki elemanı verir
result = numbers2[1, 1]  # 2. satır 2. sütundaki elemanı verir
result = numbers2[:, 2]  # tüm satırlardaki 3. sütundaki elemanları verir
result = numbers2[:, 0:2]  # tüm satırlardaki 1. ve 2. sütundaki elemanları verir
result = numbers2[-1, :]  # son satırdaki tüm elemanları verir
result = numbers2[:2, :3]  # 2 satır ve 3 sütundaki tüm elemanları verir
# print(result)


arr1 = np.arange(0, 10)
# arr2 = arr1  # referans kopyalama, aynı adresteki veriyi gösterir, birinde değişiklik diğerini etkiler

arr2 = (
    arr1.copy()
)  # deep copy, farklı adresteki veriyi gösterir, birinde değişiklik diğerini etkilemez
# print(arr1)
# print(arr2)

arr2[0] = 20
print(arr2)
print(arr1)
