import MySQLdb,csv
from dbConfig import DBDesc

# เชื่อมต่อฐานข้อมูล
def connect_db():
    myDb = DBDesc()
    conn = MySQLdb.connect(host=myDb.getHost(), user=myDb.getUser(),
                             password=myDb.getPassword(), database=myDb.getDatabase())
    return conn


# ฟังก์ชันสำหรับการอ่านข้อมูลจากไฟล์ CSV แล้วนำไปบันทึกลงในตารางในฐานข้อมูล
def load_data_from_csv(file_path):
    conn = connect_db()
    cursor = conn.cursor()
    with open(file_path, 'r',encoding='utf-8') as file:
        next(file)  # ข้ามหัวตาราง
        for line in file:
            data = line.strip().split(',')
            query = "INSERT INTO tbOpenData (customer,zooName,year,amount) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (data[0], data[1], data[2], data[3]))
    conn.commit()
    conn.close()


# ฟังก์ชันสำหรับการแสดงข้อมูลจากตารางในฐานข้อมูล
def display_data():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tbOpenData")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    conn.close()


# ฟังก์ชันสำหรับการลบข้อมูลในตารางในฐานข้อมูล
def clear_data():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tbOpenData")
    conn.commit()
    conn.close()



while True:
    print("เมนูการทำงาน:")
    print("L. Load (อ่านข้อมูลจากไฟล์ CSV และบันทึก)")
    print("D. Display (แสดงข้อมูลจากฐานข้อมูล)")
    print("C. Clear (ลบข้อมูลในฐานข้อมูล)")
    print("E. Exit (ออกจากโปรแกรม)")

    choice = input("โปรดเลือกทำรายการ: ").upper()

    if choice == "L":
        file_path = input("โปรดระบุชื่อไฟล์ CSV: ")
        load_data_from_csv(file_path+".csv")
    elif choice == "D":
        display_data()
    elif choice == "C":
        clear_data()
        print("ลบข้อมูลเรียบร้อยแล้ว")
    elif choice == "E":
        print("ขอบคุณที่ใช้บริการ ออกจากโปรแกรม")
        break
    else:
        print("โปรดเลือกรายการให้ถูกต้อง")
