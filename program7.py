# Program 7: Menentukan Masa Kerja Karyawan
masa_kerja = int(input("Masa kerja karyawan (tahun): "))
if masa_kerja < 1:
    kategori = "Pegawai baru"
elif 1 <= masa_kerja < 5:
    kategori = "Pegawai junior"
elif 5 <= masa_kerja < 10:
    kategori = "Pegawai senior"
else:
    kategori = "Pegawai senior tinggi"
print("Kategori karyawan: ", kategori)

# Flowchart Program 7:
# [Start] --> [Masa kerja karyawan (tahun)] --> [masa_kerja < 1] --> [Pegawai baru] --> [End]
#                              |
#                              +---- [1 <= masa_kerja < 5] --> [Pegawai junior] --> [End]
#                              |
#                              +---- [5 <= masa_kerja < 10] --> [Pegawai senior] --> [End]
#                              |
#                              +---- [else] --> [Pegawai senior tinggi] --> [End]
