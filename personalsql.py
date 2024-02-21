import pymysql
import hashlib


# 创建一个类
class MysqlHelper:
    # 初始化属性
    # 这里需要根据自己的mysql用户，修改用户名加密码即可，后面的三个参数在本地情况下不用改，数据库名称在初始化类对象时需要输入
    def __init__(self, database='demo', user='root', password='plmokn333', host='127.0.0.1', port=3306, charset='utf8'):
        self.host = host
        self.port = port
        self.db = database
        self.user = user
        self.passwd = password
        self.charset = charset

    # 链接的方法
    def connect(self):
        self.conn = pymysql.connect(host=self.host, port=self.port, db=self.db, user=self.user, password=self.passwd,
                                    charset=self.charset)
        self.cursor = self.conn.cursor()

    # 关闭的方法
    def close(self):
        self.cursor.close()
        self.conn.close()

    # 查询单个的方法
    def select_one(self, sql, params=[]):
        result = None
        try:
            self.connect()
            self.cursor.execute(sql, params)
            result = self.cursor.fetchone()
            self.close()
        except Exception as e:
            print(e)
        return result

    # 查询所有的方法
    def select_all(self, sql, params=[]):
        list = ()
        try:
            self.connect()
            self.cursor.execute(sql, params)
            list = self.cursor.fetchall()
            self.close()
        except Exception as e:
            print(e)
        return list

    def __edit(self, sql, params):
        count = 0
        try:
            self.connect()
            count = self.cursor.execute(sql, params)
            self.conn.commit()
            self.close()
        except Exception as e:
            print(e)
        return count

    # 插入记录的方法
    def insert(self, sql, params=[]):
        return self.__edit(sql, params)

    # 更新记录的方法
    def update(self, sql, params=[]):
        return self.__edit(sql, params)

    # 删除记录的方法
    def delete(self, sql, params=[]):
        return self.__edit(sql, params)

    # md5加密的方法（哈希加密，可不用）
    def my_md5(self, pwd):
        my_md5 = hashlib.md5()
        my_md5.update(pwd.encode('utf-8'))
        return my_md5.hexdigest()
