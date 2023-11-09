# Program 1: Menentukan Bilangan Positif, Negatif, atau Nol
bilangan = float(input("Masukkan bilangan: "))
if bilangan > 0:
    print("Bilangan positif")
elif bilangan < 0:
    print("Bilangan negatif")
else:
    print("Nol")

# Flowchart Program 1:
# [Start] --> [Masukkan bilangan] --> [bilangan > 0] --> [Bilangan positif] --> [End]
#                              |
#                              +---- [bilangan < 0] --> [Bilangan negatif] --> [End]
#                              |
#                              +---- [else] --> [Nol] --> [End]
