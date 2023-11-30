eid = input("กรุณาใส่เลขผู้ใช้ไฟฟ้า: ")
ename = input("กรุณาใส่ชื่อผู้ใช้ไฟฟ้า: ")

lastUnit = float(input("กรุณาใส่เลขมิเตอร์ไฟฟ้าเดือนที่แล้ว: "))
currentUnit = float(input("กรุณาใส่เลขมิเตอร์ไฟฟ้าเดือนปัจจุบัน: "))

if lastUnit > currentUnit:
    print("ข้อผิดพลาด:เลขมิเตอร์ไฟฟ้าเดือนที่แล้วมีค่ามากกว่าเดือนปัจจุบัน")
else:
    usedUnit = currentUnit - lastUnit
    if usedUnit <= 50:
        basePrice = usedUnit * 5
    elif 51 <= usedUnit <= 150:
        basePrice = 250 + (usedUnit - 50) * 10
    elif 151 <= usedUnit <= 300:
        basePrice = 1250 + (usedUnit - 150) * 15
    else:
        basePrice = 3500 + (usedUnit - 300) * 20

    ftPrice = usedUnit * 0.50  
    vat = (basePrice + ftPrice) * 0.07  

    totalPaid = basePrice + ftPrice + vat

    print("จำนวนหน่วยไฟฟ้าที่ใช้ไป: ", f'{usedUnit:,.2f}')
    print("ค่าไฟฟ้าฐาน: ", f'{basePrice:,.2f}')
    print("ค่าไฟฟ้าผันแปร: ", f'{ftPrice:,.2f}')
    print("ภาษีมูลค่าเพิ่ม: ", f'{vat:,.2f}')
    print("ค่าไฟฟ้าฟ้ารวมทั้งสิ้น: ", f'{totalPaid:,.2f}')
