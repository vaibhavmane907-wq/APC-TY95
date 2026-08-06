names = ["Amit", "Ravi", "Sita"]
ages = [25, 30, 40]

names.append("Neha")
ages.append(35)

name = input("Enter patient name: ")

if name in names:
    print("Patient Found")
else:
    print("Patient Not Found")

index = names.index("Ravi")
names.pop(index)
ages.pop(index)

for i in range(len(names)):
    print(names[i], ages[i])

print("Total Patients:", len(names))