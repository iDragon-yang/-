import pymysql
'''
db = pymysql.connect(host='127.0.0.1', user='root', passwd='lyx0601', db='test', port=3306, charset='utf8')
cur = db.cursor()
cur.execute('DROP TABLE IF EXISTS EMPLOYEE')
sql = ("CREATE TABLE `employee`(\n"
       "`first_name` varchar(255) DEFAULT NULL COMMENT '姓',\n"
       "`last_name` varchar (255) DEFAULT NULL COMMENT '名',\n"
       "`age` int(11) DEFAULT NULL COMMENT '年龄',\n"
       "`sex` varchar (255) DEFAULT NULL COMMENT '性别',\n"
       "`income` varchar (255) DEFAULT NULL COMMENT '收入'\n"
       ")ENGINE=InnoDB DEFAULT CHARSET=utf8;\n")
cur.execute(sql)
db.close()
'''
def create_table(name):
       name='users'
       db1=pymysql.connect(host='localhost', user='root', passwd='123456', db='test', port=3307, charset='utf8')
       cur = db1.cursor()
       cur.execute('DROP TABLE IF EXISTS '+name)
       sql = ("CREATE TABLE `"+name+"`(\n"
       "`ID` varchar(255) DEFAULT NULL COMMENT '昵称',\n"
       "`password` varchar (255) DEFAULT NULL COMMENT '密码',\n"
       "`friend_list` varchar (255) DEFAULT NULL COMMENT '朋友列表',\n"
       "`tags` varchar (255) DEFAULT NULL COMMENT '兴趣标签',\n"
       "`job` varchar (255) DEFAULT NULL COMMENT '身份'\n"
       "`team` varchar (255) DEFAULT NULL COMMENT '身份'\n"
       "`sim_job` varchar (255) DEFAULT NULL COMMENT '身份'\n"
       "`clubs` varchar (255) DEFAULT NULL COMMENT '身份'\n"
       "`classes` varchar (255) DEFAULT NULL COMMENT '身份'\n"
       ")ENGINE=InnoDB DEFAULT CHARSET=utf8;\n")
       cur.execute(sql)
       db1.close()