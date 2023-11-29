customerId='65342110481-6'
customerName='ปิยวัฒน์ ปานเรือนแสน'
#price = float(input("กรุณาป้อนราคาสินค้า: "))
#quantity = int(input("กรุณาป้อนจำนวนที่ซื้อ: "))
#total = price * quantity
#discount=0.2*total
#net=total-discount
myFavoritesRelax = [
    "สุขุมวิท",
    "ไม่อยากฟัง",
    "ข้างกัน",
    "ฉันคิด",
    "สักวันคงได้เจอ"
]
menus = {
    "ก๋วยเตี๋ยว": 50,
    "ข้าวหมูแดง": 40,
    "ผัดไทย": 60,
    "ส้มตำ": 35,
    "ข้าวผัด": 45,
    "ลาบ": 70,
    "ต้มยำกุ้ง": 80
}
#print("\nราคาสินค้า: {:.2f} บาท".format(price))
#print("จำนวนที่ซื้อ: {}".format(quantity))
#print("ยอดซื้อ: {:.2f} บาท".format(total))
#print("ส่วนลด 20%: {:.2f} บาท".format(discount))
#print("ยอดเงินที่ต้องชำระ: {:.2f} บาท".format(net))
print("\n",myFavoritesRelax[2])
print(list(menus.items())[1:5])
myFavoritesRelax.append("ฝนตกไหม")
menus["ก๋วยเตี๋ยวหมูกรอบ"] = 55
print("\n",myFavoritesRelax)
print(menus)
for key in list(menus.keys())[1:5]:
    print(f"{key}: {menus[key]} บาท")
