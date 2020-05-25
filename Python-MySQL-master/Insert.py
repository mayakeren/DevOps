import pymysql

# Establishing a connection to DB
conn = pymysql.connect(host='remotemysql.com', port=3306, user='WnQ8gxwHVY', passwd='A6IkclkYr8', db='WnQ8gxwHVY')
conn.autocommit(True)

# Getting a cursor from Database
cursor = conn.cursor()

# Inserting data into table
cursor.execute("INSERT into WnQ8gxwHVY.users (name, id) VALUES ('john', 5)")

cursor.close()
conn.close()
