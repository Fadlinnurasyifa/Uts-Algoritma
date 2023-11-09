# Program 6: Menentukan Status Gizi
berat_badan = float(input("Berat badan (kg): "))
tinggi_badan = float(input("Tinggi badan (m): "))
bmi = berat_badan / (tinggi_badan**2)
if bmi < 14.5:
    status = "Kurang"
elif 18.5 <= bmi < 24.9:
    status = "Normal"
elif 24.9 <= bmi < 29.9:
    status = "Kelebihan berat badan"
else:
    status = "Obesitas"
print("Status gizi: ", status)

# Flowchart Program 6:
# [Start] --> [Berat badan (kg)] --> [Tinggi badan (m)] --> [bmi = berat_badan / (tinggi_badan^2)] --> [bmi < 18.5] --> [Kurang gizi] --> [End]
#                              |
#                              +---- [18.5 <= bmi < 24.9] --> [Normal] --> [End]
#                              |
#                              +---- [24.9 <= bmi < 29.9] --> [Kelebihan berat badan] --> [End]
#                              |
#                              +---- [else] --> [Obesitas] --> [End]
