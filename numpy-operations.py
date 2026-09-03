import numpy as np

numbers1 = np.random.randint(10, 100, 6)
numbers2 = np.random.randint(10, 100, 6)

print(numbers1)
print(numbers2)

result = numbers1 + numbers2  # toplama işlemi
result = numbers1 + 10  # her bir elemana 10 ekler

result = numbers1 - numbers2  # çıkarma işlemi
result = numbers1 - 10  # her bir elemandan 10 çıkarır

result = numbers1 * numbers2  # çarpma işlemi
result = numbers1 * 10  # her bir elemanı 10 ile çarpar

result = numbers1 / numbers2  # bölme işlemi
result = numbers1 / 10  # her bir elemanı 10 ile böler


result = np.sin(numbers1)  # sinüs değerlerini verir
result = np.sqrt(numbers1)  # karekök değerlerini verir
result = np.log(numbers1)  # logaritma değerlerini verir

mnumbers1 = numbers1.reshape(2, 3)
mnumbers2 = numbers2.reshape(2, 3)

result = np.vstack((mnumbers1, mnumbers2))  # dikey olarak birleştirir
result = np.hstack((mnumbers1, mnumbers2))  # yatay olarak birleştirir

result = (
    numbers1 >= 50
)  # her bir eleman için 50'den büyük olanları True olarak döndürür

result = numbers1 % 2 == 0  # her bir eleman için çift olanları True olarak döndürür

print(numbers1[result])  # True olan elemanları ekrana yazdırır

print(result)
