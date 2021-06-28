# code for update operation
import sqlite3

# database name to be passed as parameter
conn = sqlite3.connect('site.db')

# update the student record
# conn.execute("UPDATE User SET username = 'SagarK' where username = 'sagar'")
# conn.commit()
# print("Total number of rows updated :", conn.total_changes )

# cursor = conn.execute("SELECT Username FROM User")
# for row in cursor:
# 	print(row)
# db.session.delete(post)
# db.session.commit()
cursor1 = conn.execute("SELECT * FROM Post")
cursor2 = conn.execute("SELECT * FROM User")
# for row in cursor1:
# 	print(row)
for row in cursor2:
	print(row)

sql = 'DELETE FROM User WHERE id=?'
cur = conn.cursor()
cur.execute(sql, (7, ))
conn.commit()
sql = 'DELETE FROM Post WHERE id=?'
cur = conn.cursor()
cur.execute(sql, (1, ))
conn.commit()
# delete post by id
# for i in range(0,29):
# 	sql = 'DELETE FROM Post WHERE id=?'
# 	cur = conn.cursor()
# 	cur.execute(sql, (i, ))
# 	conn.commit()
# sql = 'DELETE FROM Post WHERE id=?'
# cur = conn.cursor()
# cur.execute(sql, (i, ))
# conn.commit()
# cursor1 = conn.execute("SELECT * FROM Post")
# for row in cursor1:
# 	print(row)
conn.close()
