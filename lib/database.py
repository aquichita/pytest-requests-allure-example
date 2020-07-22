import mysql.connector


db = mysql.connector.connect(
    host="172.23.16.4",
    user="hone_dev",
    passwd="hone_dev2020",
    database="htms_op_business"
)

cursor = db.cursor()


def sql(sql):
    print(sql)
    cursor.execute(sql)
