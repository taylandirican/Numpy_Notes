import numpy as np

# Numpy Avantajları:
# - Daha hızlı işlemler
# - Daha az bellek kullanımı
# - Daha kolay dizilerle çalışma
# - Daha fazla fonksiyon ve metod desteği
# - Daha kolay veri okuma ve yazma
# - Daha kolay veri görselleştirme

# python list
py_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# numpy array
np_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

print(type(py_list))
print(type(np_array))

py_multi = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
np_multi = np_array.reshape(3, 3)  # elemanları gruplar

print(py_multi)
print(np_multi)

print(np_array.ndim)
print(np_multi.ndim)  # boyut sayısı


print(np_array.shape)
print(np_multi.shape)  # boyut bilgisi

print(np_array.size)
print(np_multi.size)  # eleman sayısı

a = np.array([1, 1, 1, 2, 3, 4, 3, 4, 5, 5, 5, 6, 7, 7])
print(np.unique(a))  # aynı elemanları tekilleştirir ve sıralar

reverse_array = np.flip(np_array)  # diziyi ters çevirir
reverse_array = np.flip(np_multi, axis=0)  # dizini satırlarını ters çevirir
reverse_array = np.flip(np_multi, axis=1)  # dizini sütunlarını ters çevirir

print(reverse_array)


np_multi = np_multi.flatten()  # çok boyutlu diziyi tek boyutlu diziye çevirir
print(np_multi)
