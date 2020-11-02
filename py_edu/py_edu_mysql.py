import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="dbxor",
  password="@donusum17",
  database="mydatabase"
)

mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE mydatabase")

#mycursor.execute("SHOW DATABASES")

#mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
#mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
#mycursor.execute("SHOW TABLES")

#for x in mycursor:
#  print(x)
"""
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Michelle", "Blue Village")
mycursor.execute(sql, val)

mydb.commit()

print("1 record inserted, ID:", mycursor.lastrowid)


mycursor.execute("SELECT name, address, id FROM customers")


myresult = mycursor.fetchone()

print(myresult)

print("-" *50)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)


#sql = "SELECT * FROM customers WHERE address ='Park Lane 38'"
sql = "UPDATE customers SET address = %s WHERE address = %s"
val = ("Valley 345", "Ocean blvd 2")

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")

sql = "SELECT * FROM customers WHERE address LIKE %s"
adr = ("%", )

mycursor.execute(sql, adr)
 
myresult = mycursor.fetchall()

sql = "DELETE FROM customers"

mycursor.execute(sql)

mydb.commit()

"""

mycursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 2")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)