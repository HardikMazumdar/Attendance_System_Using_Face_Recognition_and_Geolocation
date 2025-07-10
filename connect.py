import mysql.connector
try:
    connection = mysql.connector.connect(host="127.0.0.1",user="root",port="3006",password="Haldia@2025")
    print("Connected to database")
    print(connection)
    cursor=connection.cursor()
    cursor.execute("show databases")
    for database in cursor:
        print(database[0])
    cursor.execute("use employees")
    connection.commit()
    cursor.execute("create table intern(id varchar(50) PRIMARY KEY, name varchar(100) unique not null)")
    connection.commit()
except Exception as err:
    print(err)
#cursor=connection.cursor()