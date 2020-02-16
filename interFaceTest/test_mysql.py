#!/usr/bin/python
# -*- coding: UTF-8 -*-


import pymysql

dbinfo = {
    "host": "101.132.71.25",
    "user": "xiaxiaochao",
    "password": "037456",
    "port": 3306
}


class DbConnect(object):
    def __init__(self, db_cof, database="test"):
        self.db_cof = db_cof
        # 打开数据库连接
        self.db = pymysql.connect(database=database,
                                  cursorclass=pymysql.cursors.DictCursor,
                                  **db_cof)
        # 使用cursor()方法获取操作游标
        self.cursor = self.db.cursor()

    def execute(self, sql):
        # SQL 删除、提交、修改语句
        # sql = "DELETE FROM EMPLOYEE WHERE AGE > %s" % (20)
        try:
            # 执行SQL语句
            self.cursor.execute(sql)
            # 提交修改
            self.db.commit()
        except:
            self.db.rollback()

    def close(self):
        # 关闭连接
        self.db.close()


if __name__ == '__main__':
    insert_sql = 'insert into table_name ("id") value ("10")'
    DbConnect.execute(insert_sql)
    DbConnect.close()
