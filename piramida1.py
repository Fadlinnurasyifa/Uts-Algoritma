tinggi_piramida = int(input("Masukkan tinggi piramida: "))

for i in range(1, tinggi_piramida + 1):
    print(" " * (tinggi_piramida - i) + "*" * (2 * i - 1))
