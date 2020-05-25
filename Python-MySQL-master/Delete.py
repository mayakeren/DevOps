# Establishing a connection to DB
conn = pymysql.connect(host='remotemysql.com', port=3306, user='Tu5uTTQmXu', passwd='mNQIVOrny1', db='Tu5uTTQmXu')
conn.autocommit(True)

# Getting a cursor from Database
cursor = conn.cursor()

# Deleting data into table
cursor.execute("DELETE FROM table.users WHERE name = ‘john'")

cursor.close()
conn.close()
