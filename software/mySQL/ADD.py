import pymysql

def add_to_mysql(ID,password,friend_list,tags,job,team,sim_job=0,clubs='',classes=''):
    db1 = pymysql.connect(host='127.0.0.1', user='root', passwd='', db='test', port=3306, charset='utf8')
    cursor=db1.cursor()
    sql="""INSERT INTO people_information(ID,
         password, friend_list, tags, job, team, sim_job, clubs, classes)
         VALUES ("""+ID+','+password+','+friend_list+','+tags+','+job+','+team+','+sim_job+','+clubs+','+classes+')'
    try:
        cursor.execute(sql)
        db1.commit()
    except :
        db1.rollback()
