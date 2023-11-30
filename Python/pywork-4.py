studyList = []
gradeDic = {}

stdId = input("รหัสนักศึกษา: ")
name = input("ชื่อนักศึกษา: ")

con = "Y"
while con == "Y" or con == "y":
    courseId = input("ป้อนรหัสวิชา: ")
    courseName = input("ป้อนชื่อวิชา: ")
    credit = float(input("ป้อนหน่วยกิต: "))
    grade = input("ป้อนเกรด[A,B+,B,C+,C,D+,D]: ")

    studyList.append([courseId, courseName, credit, grade])
    con = input("มีวิชาเรียนวิชาอื่นอีกหรือไม่ [Y/N]? :")

print(studyList)

for numbers in studyList:
    print(f"รหัสวิชา:{numbers[0]} ชื่อวิชา:{numbers[1]} หน่วยกิต:{numbers[2]} เกรด:{numbers[3]}")
i = 0
for numbers in studyList:
    if numbers[3] == "A":
        grade = 4
    elif numbers[3] == "B+":
        grade = 3.5
    elif numbers[3] == "B":
        grade = 3
    elif numbers[3] == "C+":
        grade = 2.5
    elif numbers[3] == "C":
        grade = 2
    elif numbers[3] == "D+":
        grade = 1.5
    elif numbers[3] == "D":
        grade = 1
    else:
        grade = 0
    totalGP = grade* numbers[2]
    numbers.append(grade)
    numbers.append(totalGP)
    gradeDic[numbers[0]] = numbers[3]
cgx = 0.00
ccx = 0.00
for totalsum in studyList:
    cgx += totalsum[-1]
    ccx += totalsum[2]
    gpa = cgx / ccx
print('ผลการเรียน(studyList)', studyList)
print('รหัสวิชาและเกรด (gardeDic)',gradeDic)
print('ผลคูณหน่อยกิตกับเกรดสะสม (CGX)', cgx)
print('หน่อยกิตสะสม (CCX)', ccx)
print('เกรดเฉลี่ยสะสม (GPA)', gpa)
