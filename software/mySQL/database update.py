import pymysql

db = pymysql.connect(host='127.0.0.1', user='root', passwd='lyx0601', db='test', port=3306, charset='utf8')


# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL语句，执行更新操作
sql = 'UPDATE employee SET age = age + 5'

# 异常处理
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 提交到数据库执行
    db.commit()
except:
    # 发生错误时回滚
    db.rollback()

# 关闭数据库连接
db.close()