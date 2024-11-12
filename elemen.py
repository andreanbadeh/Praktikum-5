# Buat sebuah list sebanyak 5 elemen dengan nilai bebas
list_a = [1, 2, 3, 4, 5]

# akses list:
# tampilkan elemen ke 3
print(list_a[2])

# ambil nilai elemen ke 2 sampai elemen ke 4
print(list_a[1:4])

# ambil elemen terakhir
print(list_a[-1])

# ubah elemen list:
# ubah elemen ke 4 dengan nilai lainnya
list_a[3] = 10
print(list_a)

# ubah elemen ke 4 sampai dengan elemen terakhir
list_a[3:] = [11, 12, 13]
print(list_a)

# tambah elemen list:
# ambil 2 bagian dari list pertama (A) dan jadikan list ke 2 (B)
list_b = list_a[:2]
print(list_b)

# tambah list B dengan nilai string
list_b.append("hello")
print(list_b)

# tambah list B dengan 3 nilai
list_b.extend([14, 15, 16])
print(list_b)

# gabungkan list B dengan list A
list_a.extend(list_b)
print(list_a)