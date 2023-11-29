import datetime
print("**************************************************************")
print("Welcome to my practice condition program")
print("**************************************************************")
name=input("โปรดป้อนชื่อของท่าน: ")
yearBirth=int(input("โปรดป้อน พ.ศ. เกิด: "))
gender=int(input("โปรดเลือกเพศ [0=ชาย/1=หญิง]: "))
job=int(input("ท่านมีรายได้หรือไม่ [0=มี/1=ว่างงาน]: "))
salary= 0.00
if job==0:
    salary=float(input("โปรดป้อนเงินเดือน: "))
currentYear=datetime.datetime.today().year
age=(currentYear+543)-yearBirth
if gender==0:
    strGender="ชาย"
else:
    strGender="หญิง"
if job==0:
    strJob="มีงานทำ"
else:
    strJob="ว่างงาน"
livingAllowance=0.00
if age>=60:
    livingAllowance=600+((age-60)*100)
tax=0.00
if job==0:
    incomes=salary*12
    net=incomes-30000
    if net<=300000:
        tax=0.00
    elif net<=500000:
        tax=(net-300000)*0.03
    else:
        tax=60000+((net-500000)*0.05)

print("************************* Result ****************************")
print("ชื่อ: ",name)
print("ปีเกิด: ",yearBirth)
print("อายุ: ",age)
print("เพศ: ",strGender)
print("สถานะการทำงาน: ",strJob)
if age>=60:
    print("{0:<50s}{1:10,.2f} บาท".format("ค่าครองชีพคนชรา: ",livingAllowance))
if age >= 60:
    print("{0:<50s}{1:10,.2f} บาท".format("เงินเดือน: ",salary))
    print("{0:<50s}{1:10,.2f} บาท".format("รายได้ทั้งปี: ",incomes))
    print("{0:<50s}{1:10,.2f} บาท".format("รายได้หลังหักค่าลดหย่อน: ",net))
    print("{0:<50s}{1:10,.2f} บาท".format("ภาษีที่ต้องจ่าย: ",tax ))
print("*********************** Good Bye ****************************")