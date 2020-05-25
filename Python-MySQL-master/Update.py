# Establishing a connection to DB
conn = pymysql.connect(host='remotemysql.com', port=3306, user='Tu5uTTQmXu', passwd='mNQIVOrny1', db='Tu5uTTQmXu')
conn.autocommit(True)

# Getting a cursor from Database
cursor = conn.cursor()

# Updating data inside the table
cursor.execute("UPDATE table.users SET id = '10' WHERE name = ‘john'")

cursor.close()
conn.close()
