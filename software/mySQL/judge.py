#用于检测输入的账号密码是否在数据库中保存
import pymysql

def judge(user,password):
    db1=pymysql.connect(host='localhost', user='root', passwd='123456', db='test', port=3307, charset='utf8')
    cur = db1.cursor()
    sql = "SELECT * FROM test.users WHERE ID = "+user+"AND test.password = "+password
    try:
        cur.execute(sql)
        return True
    except:
        return False