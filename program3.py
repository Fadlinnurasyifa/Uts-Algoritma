# Program 3: Menentukan Jenis Segitiga
sisi1 = float(input("Masukkan panjang sisi 1: "))
sisi2 = float(input("Masukkan panjang sisi 2: "))
sisi3 = float(input("Masukkan panjang sisi 3: "))
if sisi1 == sisi2 == sisi3:
    print("Segitiga sama sisi")
elif sisi1 == sisi2 or sisi1 == sisi3 or sisi2 == sisi3:
    print("Segitiga sama kaki")
else:
    print("Segitiga sembarang")

# Flowchart Program 3:
# Copy code
# [Start] --> [Masukkan panjang sisi 1] --> [Masukkan panjang sisi 2] --> [Masukkan panjang sisi 3] --> [sisi1 == sisi2 == sisi3] --> [Segitiga sama sisi] --> [End]
#                              |
#                              +---- [sisi1 == sisi2 or sisi1 == sisi3 or sisi2 == sisi3] --> [Segitiga sama kaki] --> [End]
#                              |
#                              +---- [else] --> [Segitiga sembarang] --> [End]
