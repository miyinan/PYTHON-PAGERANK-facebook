import pymysql
import list


def sqlconnect():
    db = pymysql.connections.Connection(  # 根据个人的数据库信息来改
        host='127.0.0.1',
        port=3306,
        user='root',
        password='miyinan2000',
        charset='utf8'
    )
    print("connected!")
    return db


def establish_table(type):  # 输入两个字符串
    table_name = type
    db = sqlconnect()
    cursor = db.cursor()
    cursor.execute("USE FaceBookRank")
    cursor.execute("DROP TABLE IF EXISTS %s" % (table_name))
    sql = """
       CREATE TABLE whatever
       (
       No VARCHAR(50),
       id VARCHAR(50),
       facebook_id VARCHAR(50), 
       page_name VARCHAR(200),
       page_type VARCHAR(50),
       degree VARCHAR(50),
       rank_ VARCHAR(50),
       rank_rate VARCHAR(50)
       )"""
    cursor.execute(sql)
    cursor.execute("RENAME TABLE whatever TO %s" % (table_name))
    db.commit()
    cursor.close()
    pass


def insert_data(list, table_name):
    db = sqlconnect()
    cursor = db.cursor()
    cursor.execute("USE FaceBookRank")
    for i in range(1, len(list)):
        sql = "INSERT INTO %s VALUES (%d,%d,'%s','%s',%d,%d,%d,%d)"
        cursor.execute(sql % (table_name, i, list[i][0], pymysql.escape_string(list[i][1]),
                              pymysql.escape_string(list[i][2]), list[i][3], 0, 0, 0))
        print("yes : %d %d" % (list[i][0], i))
    db.commit()
    cursor.close()
    pass


def insert(type):
    typelist = list.alltype(type)
    establish_table(type)
    insert_data(typelist, type)


#insert('company')
#insert('politician')
#insert('government')
insert('all_')
