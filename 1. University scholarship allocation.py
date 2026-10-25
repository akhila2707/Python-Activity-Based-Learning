name = input("Enter student name: ")
marks = int(input("Enter aggregate marks: "))
subject = int(input("Enter subject marks: "))
attendance = int(input("Enter attendance: "))
income = int(input("Enter family income: "))

if marks >= 85 and subject >= 75 and attendance >= 80 and income <= 100000:
    print(name, "is eligible for scholarship")
else:
    print(name, "is not eligible for scholarship")
