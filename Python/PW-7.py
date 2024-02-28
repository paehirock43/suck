import MySQLdb
from dbConfig import DBDesc
myDb=DBDesc()
myConn=MySQLdb.connect(host=myDb.getHost(),user=myDb.getUser(),
                       password=myDb.getPassword(),database=myDb.getDatabase())
myCursor=myConn.cursor();
p=True
while p==True:
    print("1:ขอดูข้อมูลสินค้าที่มีราคาขาย(buyPrice) ตั้งแต่20 – 80 บาท\n2:ขอดูข้อมูลสินค้าทั้งหมดที่อยู่ในสายผลิต (productLine) ‘Trains’กับ ‘Motorcycles’\n3:ขอดูข้อมูลสินค้าที่ไม่ปรากฏในรายการสั่งซื้อเลย\n4:ขอดูยอดขายสินค้าแยกตามใบสั่งซื้อ\n5:ขอดูรายการสั่งซื้อตามหมายเลขใบสั่งซื้อที่ระบุ\n6:ออกจากโปรแกรม")
    i=int(input("กรุณาระบุคำสั่ง(1-6): "))
    while i==1:
        #
        strsql="select productCode,productName,productVendor,quantityInStock,buyPrice from products where buyPrice>=20 and buyPrice<=80"
        myCursor.execute(strsql)
        myResult=myCursor.fetchall()
        row_count = myCursor.rowcount
        print("*"*30," DATA ABOUT PRODUCT PRICE THAT BETWEEN 20 AND 80 DOLLARS","*"*30)
        print(f"จำนวนข้อมูลทั้งหมด: {row_count}")
        print("{0:12s} {1:45s} {2:26s} {3:>6} {4:>10}".format("PRODUCT ID","PRODUCT NAME","LOCATION","STOCK","PRICE"))
        for data in myResult:
            print("{0:12s} {1:45s} {2:26s} {3:6d} {4:>10.2f} $".format(data[0],data[1],data[2],data[3],data[4]))
        break
    while i==2:
        #
        strsql="select productCode,productName,productVendor,quantityInStock,buyPrice from products where productLine='Trains' or productLine='Motorcycles' "
        myCursor.execute(strsql)
        myResult=myCursor.fetchall()
        row_count = myCursor.rowcount
        print("*"*30," DATA ABOUT PRODUCT LINE FROM TRAINS AND MOTORCYCLES","*"*30)
        print(f"จำนวนข้อมูลทั้งหมด: {row_count}")
        print("{0:12s} {1:45s} {2:26s} {3:>6} {4:>10}".format("PRODUCT ID","PRODUCT NAME","LOCATION","STOCK","PRICE"))
        for data in myResult:
            print("{0:12s} {1:45s} {2:26s} {3:6d} {4:>10.2f} $".format(data[0],data[1],data[2],data[3],data[4]))
        break
    while i == 3:
        #
        strsql="SELECT products.productCode, products.productName, products.productVendor, products.quantityInStock, products.buyPrice FROM products LEFT JOIN orderdetails ON products.productCode = orderdetails.productCode WHERE orderdetails.productCode IS NULL"
        myCursor.execute(strsql)
        myResult=myCursor.fetchall()
        row_count=myCursor.rowcount
        print("*"*30," DATA ABOUT PRODUCT HAVE NOT IN ORDER DETAILS","*"*30)
        print(f"จำนวนข้อมูลทั้งหมด: {row_count}")
        print("{0:12s} {1:45s} {2:26s} {3:>6} {4:>10}".format("PRODUCT ID","PRODUCT NAME","LOCATION","STOCK","PRICE"))
        for data in myResult:
            print("{0:12s} {1:45s} {2:26s} {3:6d} {4:>10.2f} $".format(data[0],data[1],data[2],data[3],data[4]))
        break
    while i == 4:
        #
        strsql="select orderdetails.orderNumber , orders.orderDate ,sum(orderdetails.quantityOrdered) from orderdetails inner join orders on orderdetails.orderNumber = orders.orderNumber group by orderdetails.orderNumber"
        myCursor.execute(strsql)
        myResult=myCursor.fetchall()
        row_count=myCursor.rowcount
        print("*"*30," DATA ABOUT ORDERS ","*"*30)
        print(f"จำนวนข้อมูลทั้งหมด: {row_count}")
        print("{0:15s} {1:11} {2:10}".format("ORDER NUMBER","DATE","QUANTITY"))
        for data in myResult:
            print("{0:^12} {1:%d/%m/%Y} {2:^15} ".format(data[0],data[1],data[2]))
        break
    while i==5:
        #
        inputTrans=int(input("Pleas Enter Order Number : "))
        strsql=("select  distinct orderdetails.orderNumber ,orders.orderDate ,"
                "customers.customerName ,products.productCode,products.productName,"
                "products.buyPrice,orderdetails.quantityOrdered "
                "from orderdetails join customers inner join orders "
                "on orders.orderNumber = orderdetails.orderNumber inner join "
                "products on orderdetails.productCode = products.productCode "
                "where orderdetails.orderNumber = %s ")
        myCursor.execute(strsql,(inputTrans,))
        myResult=myCursor.fetchall()
        row_count=myCursor.rowcount
        print("*"*35," RECIPE ","*"*35)
        print("{0:^18s} {1:^15s} {2:^15s}".format("ORDER NUMBER","DATE","NAME"))
        print("{0:^20d} {1:%d/%m/%Y} {2:>20s} ".format(myResult[0][0],myResult[0][1],myResult[0][2]))
        print("-"*80)
        print("{0:15s} {1:42} {2:6} {3:10} {4:10}".format("PRODUCT ID","PRODUCT NAME","PRICE","AMOUNT","TOTAL"))
        totalAll=0
        for data in myResult:
            total = int(data[5]) * int(data[6])
            totalAll += total
            print("{0:12} {1:45} {2:5} {3:5} {4:10.2f} $".format(data[3],data[4],data[5],data[6],total))
        print("*"*80)
        print(f"จำนวนรายการที่สั่งซื้อ: {row_count} รายการ")
        print("รวมเป็นเงินทั้งสิ้น: ", totalAll, " $")
        print("*" * 80)
        break
    while i==6:
        p=False
        break
myCursor.close()
myConn.close()