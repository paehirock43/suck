employee='Piyawat Panruensan'
status='dev'
department='game dev'
taxRate=0.07
salary= int(input("ระบุเงินเดือน : "))
allowance= int(input("เงินประจำตำแหน่ง : "))
bonus=salary*3
inComePerYear=((salary+allowance)*12)+bonus
tax=inComePerYear*taxRate
print("ชื่อพนักงาน: ",employee)
print("ตำแหน่ง: ",status)
print("แผนก: ",department)
print(f"เงินเดือน: {salary:.2f}")
print(f"เงินประจำตำแหน่ง: {allowance:.2f}")
print(f"โบนัส: {bonus:.2f}")
print(f"รายได้ต่อปี: {inComePerYear:.2f}")
print(f"ภาษี: {tax:.2f}")