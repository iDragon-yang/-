import pymysql
db = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', db='test', port=3307, charset='utf8')

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL语句，执行删除操作
sql = 'DELETE FROM employee WHERE income > 500000 OR age >35'

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

def other_command(name,sql):
    db1=pymysql.connect(host='127.0.0.1', user='root', passwd='123456', db='test', port=3307, charset='utf8')
    cursor1=db1.cursor()
    cursor1.execute(sql)
    db1.commit()
    db1.close()