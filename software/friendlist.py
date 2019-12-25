import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.Qt import *
from chat_win import chat_win
from server import server
import threading

class friend_list(QWidget):
    def __init__(self,ID, parent=None):
        super(friend_list,self).__init__(parent=parent)
        self.setWindowTitle('朋友列表')
        self.setWindowIcon(QIcon('image\icon.ico'))
        self.id=str(ID)
        self.main_layout=QVBoxLayout(self)
        friends=self.get_list(self.id)
        self.get_order(friends)
        self.windowLIst=[]

    def get_list(self,id):
        with open('C:/study/软件工程/software/frient_list/friend_list.txt','r') as f:
            friend1=f.readlines()
            f.close()
        #print(len(friend1))
        for i in range(0,len(friend1)):
            if friend1[i][0:len(id)]==id:
                return friend1[i][len(id):].split()
        QMessageBox.warning(self,'初始化失败','无好友',QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
        return []

    def get_order(self,friends):
        Frinum=len(friends)
        with open('C:/study/软件工程/software/user_info/ID.txt','r') as f:
            user_info=f.readlines()
            f.close()
        indexs=[]
        for i1 in friends:
            for i2 in range(0,len(user_info)):
                #3print(len(i1),len(user_info[i2]))
                if (i1==user_info[i2].split('\n')[0]):
                    indexs.append(i2)
        interests=[]
        with open('C:/study/软件工程/software/user_info/interest.txt','r',encoding='utf8') as f1:
            inte=f1.readlines()
            f1.close()
        for index in indexs:
            interests.append(inte[index])
        '''
        print(user_info)
        print(inte)
        print(indexs)
        print(Frinum)
        '''
        for num in range(0,Frinum):
            layout1=QHBoxLayout()
            btn=QPushButton('聊天')
            ID=QLabel('名字：'+user_info[indexs[num]])
            self_interest=QLabel('兴趣：'+inte[indexs[num]])
            layout1.addWidget(ID)
            layout1.addWidget(self_interest)
            layout1.addWidget(btn)
            self.main_layout.addLayout(layout1)
            btn.clicked.connect(lambda:self.start_chat(self.id,user_info[indexs[num]]))
        btn2=QPushButton('添加朋友')
        btn1=QPushButton('退出')
        btn1.clicked.connect(self.close)
        btn2.clicked.connect(lambda: self.start_finding())
        self.main_layout.addWidget(btn1)
        self.main_layout.addWidget(btn2)
    
    
    def start_finding(self):
        self.windowLIst.append(self)
        new_win=add_friend(self.id)
        self.windowLIst.append(new_win)
        new_win.show()
        self.close()
        #new_win=add_friend(id)

    def start_chat(self,my_id,fri_id):
        server1=server(str(my_id),str(fri_id))
        new=chat_win(my_id,fri_id,server1)
        t=threading.Thread(target=new.server.receive_message,args=())
        t.start()
        t1=threading.Thread(target=new.if_get_Message,args=())
        t1.start()
        new.show()
        self.windowLIst.append(new)
        self.windowLIst.append(self)
        self.close()



class add_friend(QWidget):
    def __init__(self,id, parent=None):
        super(add_friend,self).__init__()
        self.layout=QVBoxLayout(self)
        self.getorder()
        self.id=id
        self.winlist=[]

    def getorder(self):
        tishi=QLabel('请输入你要查找的好友的ID:')
        finding_id=QLineEdit('fyq')
        go=QPushButton('查找')
        tishi.setBuddy(finding_id)
        interesting_info=QTextEdit('请输入ID后查看该用户兴趣')
        interesting=self.get_inter(finding_id.text())
        middle_layout=QHBoxLayout()
        middle_layout.addWidget(tishi)
        middle_layout.addWidget(finding_id)
        middle_layout.addWidget(go)
        self.layout.addLayout(middle_layout)
        self.layout.addWidget(interesting_info)
        go.clicked.connect(lambda: interesting_info.setText(self.get_inter(finding_id.text())))
        middle_layout1=QHBoxLayout()
        add=QPushButton('确认添加')
        cancel=QPushButton('返回朋友列表')
        middle_layout1.addWidget(add)
        middle_layout1.addWidget(cancel)
        self.layout.addLayout(middle_layout1)
        add.clicked.connect(lambda: self.get_new_friend(finding_id.text(),self.get_id_num(self.id)))
        cancel.clicked.connect(lambda: self.back())
    
    def get_inter(self,id):
        with open('C:/study/软件工程/software/user_info/ID.txt','r') as ID_file:
            ID_list=ID_file.read().split('\n')
            ID_file.close()
        try:
            ID_num=ID_list.index(id)
        except ValueError:
            QMessageBox.warning(self,'账号错误','无使用该ID的用户',QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
            return
        with open('C:/study/软件工程/software/user_info/interest.txt','r',encoding='utf8') as ID_file1:
            interest_list=ID_file1.read().split('\n')
            ID_file1.close()
        return interest_list[ID_num]
    

    def get_new_friend(self,id,num):
        with open('C:/study/软件工程/software/frient_list/friend_list.txt','r',encoding='utf8') as ID_file1:
            friend_list=ID_file1.read().split('\n')
            ID_file1.close()
        #print('id_num=',num)
        if id in friend_list[num]:
            return
        friend_list[num]=friend_list[num]+' '+id+'\n'
        for a in friend_list:
            a=a+'\n'
        result=''
        for b in friend_list:
            if b=='':
                result=result+'\n'
            else:
                result=result+b
        with open('C:/study/软件工程/software/frient_list/friend_list.txt','w',encoding='utf8') as ID_file2:
            ID_file2.write(result)
            ID_file1.close()

    def get_id_num(self,id):
        with open('C:/study/软件工程/software/user_info/ID.txt','r',encoding='utf8') as f2:
            ids=f2.read().split('\n')
            f2.close()
        return ids.index(id)
    
    def back(self):
        self.winlist.append(self)
        new_win=friend_list(self.id)
        self.winlist.append(new_win)
        new_win.show()
        self.close()
        


if __name__ == "__main__":
    app=QApplication(sys.argv)
    win=friend_list('lkc')
    win2=friend_list('fyq')
    win.show()
    win2.show()
    sys.exit(app.exec_())