# Contoh kode program Fungsional pada Python
#==========================================#

# Program untuk menghitung bilangan fibonacci dengan fungsional programming
def key(j):
    if j == 0:
        return 0
    elif j == 1:
        return 1
    else:
        return key(j-1) + key(j-2)

# Memanggil fungsi key
print(key(12))




# contoh kode program OOP pada python
#===================================#

# Program untuk menghitung luas dan keliling lingkaran dengan OOP
class Lingkaran:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return 3.14 * (self.radius ** 2)

    def get_Lingkar(self):
        return 2 * 3.14 * self.radius

# Membuat objek k
k = Lingkaran(3)

# Memanggil metode get_area() dan get_Lingkar()
print("Luas lingkaran:", k.get_area())
print("Keliling lingkaran:", k.get_Lingkar())
