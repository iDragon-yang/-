import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.Qt import *
from socket import *
import random
from server import server
import threading

class chat_win(QWidget):
    def __init__(self, my_id,friend_id,server,parent=None):
        super(chat_win,self).__init__(parent=parent)
        self.resize(800,700)
        self.setWindowIcon(QIcon('image\icon.ico'))
        self.my_id=my_id
        self.friend_id=friend_id
        self.setWindowTitle(str(self.friend_id))
        self.layout=QVBoxLayout(self)
        self.Text=QTextEdit()
        self.ready_text=QLineEdit()
        self.btn=QPushButton('发送')
        self.get_order()
        self.server=server
        self.btn.clicked.connect(self.sendMessage)
    
    def get_order(self):
        self.layout.addWidget(self.Text)
        middle_layout=QHBoxLayout()
        middle_layout.addWidget(self.ready_text)
        middle_layout.addWidget(self.btn)
        cancel=QPushButton('返回朋友列表')
        self.layout.addLayout(middle_layout)
        self.layout.addWidget(cancel)

    
    def sendMessage(self):
        a=self.ready_text.text()
        self.update_message(a)
        self.server.sendMessage(a)
        return
    
    def update_message(self,message):
        self.Text.moveCursor(QTextCursor.End)
        self.Text.insertPlainText(str(self.my_id)+':  '+message+'\n')
        self.ready_text.clear()
        return 

    def if_get_Message(self):
        end=''
        while 1:
            if (self.server.newmessage[-1]!=end):
                self.update_message(self.server.newmessage[-1].split('@')[0])
                end=self.server.newmessage[-1]


    

if __name__ == "__main__":
    app=QApplication(sys.argv)
    server1=server(1,2)
    server2=server(2,1)
    win=chat_win(my_id=1,friend_id=2,server=server1)
    win2=chat_win(my_id=2,friend_id=1,server=server2)
    win.show()
    win2.show()
    t=threading.Thread(target=win.server.receive_message,args=())
    t.start()
    t1=threading.Thread(target=win2.server.receive_message,args=())
    t1.start()
    t3=threading.Thread(target=win.if_get_Message,args=())
    t3.start()
    t4=threading.Thread(target=win2.if_get_Message,args=())
    t4.start()
    sys.exit(app.exec_())
