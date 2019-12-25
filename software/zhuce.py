import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.Qt import *
from zoom_picture import *
from log_mainwindow import windowList
'''
from mySQL.ADD import add_to_mysql
from mySQL.Create_table import create_table
from mySQL.delete import other_command
'''

class window_zhuce(QWidget):
    def __init__(self, parent=None):
        super(window_zhuce,self).__init__(parent=parent)
        #create_table('people_information')
        self.resize(700,500)
        #self.setMinimumSize(700,500)
        self.setMaximumSize(700,500)
        layout=self.getlayout()
        self.setLayout(layout)
        self.setContentsMargins(QMargins(60,150,50,100))
        self.setBackground()
        self.setWindowIcon(QIcon('image\icon.ico'))
        self.ID=''
        self.pwd=''
        self.inter=''
        self.job=''
        self.team=''

    def getlayout(self):
        main_layout=QGridLayout()
        
        ID_label=QLabel('用户名：')
        ID=QLineEdit()
        ID_label.setBuddy(ID)
        ID.editingFinished.connect(lambda:self.change_ID(ID.text()))
        
        
        password_label=QLabel('新密码')
        password=QLineEdit()
        password_label.setBuddy(password)
        password.editingFinished.connect(lambda:self.change_pwd(password.text()))
        
        head_label=QLabel('头像')
        head=QLabel()
        head_label.setBuddy(head)
        
        
        tags_label=QLabel('兴趣标签')
        tagsBox=QGroupBox('兴趣标签')
        tagsBox.setFlat(True)
        layout1=QGridLayout(tagsBox)
        tag1=QCheckBox('篮球')
        tag1.stateChanged.connect(lambda:self.get_interest(str(tag1.text())))
        tag2=QCheckBox('读书')
        tag2.stateChanged.connect(lambda:self.get_interest(str(tag2.text())))
        tag3=QCheckBox('跑步')
        tag3.stateChanged.connect(lambda:self.get_interest(str(tag3.text())))
        tag4=QCheckBox('足球')
        tag4.stateChanged.connect(lambda:self.get_interest(str(tag4.text())))
        tag5=QCheckBox('唱歌')
        tag5.stateChanged.connect(lambda:self.get_interest(str(tag5.text())))
        tag6=QCheckBox('电影')
        tag6.stateChanged.connect(lambda:self.get_interest(str(tag6.text())))
        layout1.addWidget(tag1,0,0,1,1)
        layout1.addWidget(tag2,0,1,1,1)
        layout1.addWidget(tag3,0,2,1,1)
        layout1.addWidget(tag4,1,0,1,1)
        layout1.addWidget(tag5,1,1,1,1)
        layout1.addWidget(tag6,1,2,1,1)
        tags_label.setBuddy(tagsBox)
        


        job_label=QLabel('职务')
        btn_layout=QHBoxLayout()
        btn1=QRadioButton('学员')
        btn1.toggled.connect(lambda:self.get_job(btn1.text()))
        btn2=QRadioButton('教员')
        btn2.toggled.connect(lambda:self.get_job(btn2.text()))
        btn3=QRadioButton('干部')
        btn3.toggled.connect(lambda:self.get_job(btn3.text()))
        btn_layout.addWidget(btn1)
        btn_layout.addWidget(btn2)
        btn_layout.addWidget(btn3)
        #job_label.setBuddy(btn_layout)
        '''
        simjob_label=QLabel('学员担任的模拟职务：')
        simjob=QLineEdit()
        simjob_label.setBuddy(simjob)
        '''


        team_label=QLabel('队别：')
        team=QLineEdit()
        team.textChanged.connect(lambda:self.get_team(team.text()))
        team_label.setBuddy(team)
        

        main_layout.addWidget(ID_label,0,0,1,1)
        main_layout.addWidget(ID,0,1,1,3)
        main_layout.addWidget(password_label,1,0,1,1)
        main_layout.addWidget(password,1,1,1,3)
        main_layout.addWidget(head_label,2,0,1,1)
        main_layout.addWidget(head,2,1,3,3)
        main_layout.addWidget(tags_label,5,0,1,1)
        main_layout.addWidget(tagsBox,6,0,2,4)
        main_layout.addWidget(job_label,8,0,1,1)
        main_layout.addLayout(btn_layout,8,1,1,3)
        main_layout.addWidget(team_label,10,0,1,1)
        main_layout.addWidget(team,10,1,1,3)

        layout2=QHBoxLayout()
        zhuce_btn=QPushButton('确认')
        cancel_btn=QPushButton('取消')
        layout2.addWidget(zhuce_btn)
        layout2.addWidget(cancel_btn)
        main_layout.addLayout(layout2,11,1,1,2)

        zhuce_btn.clicked.connect(lambda:self.type_in_info(self.ID,self.pwd,self.inter,self.job,self.team))

        return main_layout

    def setBackground(self):
        background=QPalette()
        background.setBrush(QPalette.Background,QBrush(QPixmap('image\zhuce.jpg')))
        self.setPalette(background)

    def type_in_info(self,user_ID,pwd,interests,status,team):
        print(user_ID,pwd,interests,status,team)
        with open('C:/study/软件工程/software/user_info/ID.txt','a') as ID_txt:
            ID_txt.write(user_ID+'\n')
            ID_txt.close()
        with open('C:/study/软件工程/software/user_info/password.txt','a') as pwd_txt:
            pwd_txt.write(pwd+'\n')
            pwd_txt.close()
        with open('C:/study/软件工程/software/user_info/interest.txt','a',encoding='utf-8') as inter_txt:
            inter_txt.write(interests+'\n')
            inter_txt.close()
        with open('C:/study/软件工程/software/user_info/status.txt','a',encoding='utf-8') as status_txt:
            status_txt.write(status+'\n')
            status_txt.close()
        with open('C:/study/软件工程/software/user_info/team.txt','a') as team_txt:
            team_txt.write(team+'\n')
            team_txt.close()
        with open('C:/study/软件工程/software/frient_list/friend_list.txt','a') as frilist:
            frilist.write(user_ID+' \n')
        

    def get_job(self,job):
        self.job=job

    def change_ID(self,id1):
        self.ID=id1

    def change_pwd(self,passw):
        self.pwd=passw

    def get_interest(self,interestt):
        self.inter=self.inter+interestt+' '

    def get_team(self,tt):
        self.team=tt


if __name__ == "__main__":
    app=QApplication(sys.argv)
    #zoom_picture('image\zhuce.jpg',700,600)
    win=window_zhuce()
    win.show()
    sys.exit(app.exec_())
