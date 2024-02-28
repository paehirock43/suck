import MySQLdb
from dbConfig import DBDesc
myDb=DBDesc()
myConn=MySQLdb.connect(host=myDb.getHost(),user=myDb.getUser(),
                       password=myDb.getPassword(),database=myDb.getDatabase())
myCursor=myConn.cursor();
strsql="select * from customers where country = 'USA'"
myCursor.execute(strsql)
myResult=myCursor.fetchall()
print("*"*30," Customers from USA ","*"*30)
for data in myResult:
    print("{0:<5d} {1:40s} {2:20s} {3:10s}".format(data[0],data[1],data[7],data[8]))
cont=input("Please Enter to Continue....")
strsql="select productCode,productName,productVendor,buyPrice, " \
       "quantityInStock from products where quantityInStock < 500"
myCursor.execute(strsql)
myResult=myCursor.fetchall()
print("*"*30," Our Product ","*"*30)
for data in myResult:
    print("{0:10s} {1:40s} {2:30s} {3:>10f} {4:^10d}"\
          .format(data[0],data[1],data[2],data[3],data[4]))
cont=input("Please Enter to Continue....")
strsql="select orders.orderNumber,orderDate,orderdetails.productCode,productName,priceEach,quantityOrdered,(priceEach*quantityOrdered)"\
        "as total from orders, orderdetails,products where "\
        "orders.orderNumber=orderdetails.orderNumber and "\
        "orderdetails.productCode=products.productCode and "\
        "status='In Process'"
myCursor.execute(strsql)
myResult=myCursor.fetchall()
print("*"*30," Order Details ","*"*30)
for data in myResult:
    print("{0:7} {1} {2:13s} {3:50s} {4:>10f} {5:^5d} {6:>10f}"\
          .format(data[0],data[1],data[2],data[3],data[4],data[5],data[6]))
cont=input("Please Enter to End....")
print("Good Bye.")
myConn.close()