# Program 4: Menentukan Status Pendaftaran Pemilih
usia = int(input("Masukkan usia: "))
daftar_pemilih = input("Sudah mendaftar pemilih? (ya/tidak): ").lower()
if usia >= 17 and daftar_pemilih == "ya":
    print("Anda dapat memilih.")
else:
    print("Anda tidak dapat memilih.")

# Flowchart Program 4:
# [Start] --> [Masukkan usia] --> [Sudah mendaftar pemilih? (ya/tidak)] --> [usia >= 17 and daftar_pemilih == "ya"] --> [Anda dapat memilih.] --> [End]
#                              |
#                              +---- [else] --> [Anda tidak dapat memilih.] --> [End]
