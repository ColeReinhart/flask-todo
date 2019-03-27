import psycopg2

# connection to database
con = psycopg2.connect(
            host = "localhost",
            database="portal"
)
#cursor
cur = con.cursor()

cur.execute("INSERT INTO Links (id, you_at_tsct, email, academic_calender, athletics, commuter) values (20, 'Jimmy', 'yeet', 'yoot', 'yat', 'yes')")
# execute query
cur.execute("select * from Links")

rows = cur.fetchall()

for r in rows:
    print (r)

#commiting changes
con.commit()
#close the cursor
cur.close()
# close the connection
con.close()