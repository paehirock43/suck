studyList = []
gradeDic = {}
stdName = input("input name: ")
stdId = input("input id: ")

while True:
    subId = input("input subject id: ")
    subName = input("input subject name: ")
    credit = int(input("input credit: "))
    strGrade = input("input grade(A,B+,B,C+,C,D+,D,F): ")
    studyList.append([subId, subName, credit, strGrade])
    repeat = input("do you want to repeat(y/n): ")
    if repeat.upper() != "Y":
        break

print("ผลการเรียน (studyList):\n", studyList)

for course in studyList:
    credit = course[2]
    grade = course[3]
    if grade == "A":
        numGrade = 4
    elif grade == "B+":
        numGrade = 3.5
    elif grade == "B":
        numGrade = 3
    elif grade == "C+":
        numGrade = 2.5
    elif grade == "C":
        numGrade = 2
    elif grade == "D+":
        numGrade = 1.5
    elif grade == "D":
        numGrade = 1
    else:
        numGrade = 0

    gp = credit * numGrade
    course.extend([numGrade, gp])
    gradeDic[course[0]] = course[3]

CGX_total = 0
CCX_total = 0
for course in studyList:
    CGX_total += course[5]
    CCX_total += course[2]

GPA = CGX_total / CCX_total

print("ผลการเรียนหลังประมวลผล (studyList):\n", studyList)

print("รหัสวิชาและเกรด (gradeDic):\n", gradeDic)

print("ผลคูณหน่วยกิตกับเกรดสะสม (CGX):", CGX_total)
print("หน่วยกิตสะสม (CCX):", CCX_total)
print("เกรดเฉลี่ยสะสม (GPA):", GPA)
