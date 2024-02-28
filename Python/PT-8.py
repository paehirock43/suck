import MySQLdb
from dbConfig import DBDesc

myDb = DBDesc()
myConn = MySQLdb.connect(host=myDb.getHost(), user=myDb.getUser(),
                         password=myDb.getPassword(), database=myDb.getDatabase())
myCursor = myConn.cursor()
menu = "1"
while menu != "Q":
    menuComplete = False
    while menuComplete == False:
        print("A. แสดงประเภทสินค้า")
        print("B. เพิ่มประเภทสินค้า")
        print("C. แก้ไขประเภทสินค้า")
        print("D. ลบประเภทสินค้า")
        print("Q. ออกจากโปรแกรม ")
        menu = input("โปรดเลือกเมนู [A...Q]: ")
        menu = menu.upper()
        if menu in ("A", "B", "C", "D", "Q"):
            menuComplete = True
    if menu == "A":
        strsql = "select * from tbtypes"
        myCursor.execute(strsql)
        myResult = myCursor.fetchall()
        print("************ Type Listing ***********")
        print("{0:<10s} {1:40s} ".format("ID", "Type"))
        print("*************************************")

        for data in myResult:
            print("{0:<10s} {1:40s} ".format(data[0], data[1]))
            print("*************************************")
    elif menu == "B":
        inputComplete = False
        while inputComplete == False:
            typeID = input("Enter type id: ")
            typeName = input("Enter type name: ")
        if typeID.strip() != "" and typeName.strip() != "":
            inputComplete = True
            strsql = "insert into tbtypes(typeID, typeName) values(%s, %s)"
            value = (typeID, typeName)
            myCursor.execute(strsql, value)
            myConn.commit()
            print("เพิ่มขอ้ มูลเรียบร้อย...")
    elif menu == "C":
        searchComplete = False
        while searchComplete == False:
            typeID = input("Enter type id that you want to update: ")
            strsql = "select * from tbtypes where typeID = %s"
            value = (typeID,)
            myCursor.execute(strsql, value)
            myResult = myCursor.fetchall()
    if myResult:
        searchComplete = True
        for data in myResult:
            print("{0:<10s} {1:40s} ".format(data[0], data[1]))
        updateComplete = False
        while updateComplete == False:
            typeName = input("Enter type name: ")
            if typeName.strip() != "": updateComplete = True
        strsql = "update tbtypes set typeName = %s where typeID= %s"
        value = (typeName, typeID)
        myCursor.execute(strsql, value)
        myConn.commit()
        print("แก้ไขข้อมูลเรียบร้อย...")
    elif menu == "D":
        deleteComplete = False
        while deleteComplete == False:
            typeID = input("Enter type id that you want to delete: ")
            strsql = "select * from tbtypes where typeID = %s"
            value = (typeID,)
            myCursor.execute(strsql, value)
            myResult = myCursor.fetchall()
            if myResult:
                deleteComplete = True
                for data in myResult:
                    print("{0:<10s} {1:40s} ".format(data[0], data[1]))
            strsql = "delete from tbtypes where typeID = %s "
            value = (typeID,)
            myCursor.execute(strsql, value)
            myConn.commit()
            print("ลบข้อมูลเรียบร้อย...")
myConn.close()
myCursor.close()
