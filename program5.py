# Program 5: Menentukan Diskon Berdasarkan Total Belanja
total_belanja = float(input("Total belanja: "))
if total_belanja >= 1000000:
    diskon = 10
elif total_belanja >= 500000:
    diskon = 5
else:
    diskon = 0
print("Anda mendapatkan diskon sebesar", diskon, "%.")

# Flowchart Program 5:
# [Start] --> [Total belanja] --> [total_belanja >= 1000000] --> [diskon = 10%] --> [End]
#                              |
#                              +---- [total_belanja >= 500000] --> [diskon = 5%] --> [End]
#                              |
#                              +---- [else] --> [diskon = 0%] --> [End]
