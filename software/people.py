class People():
    def __init__(self):
        self.ID=''
        self.password=''
        self.head_portrait=''
        self.friend_list=[]
        self.tags=[]
        self.job=0 #0代表学生，1代表教员，2代表干部

    def setID(self,id):
        self.ID=id
    
    def setpassword(self,passw):
        self.password=passw

    def sethead_portrait(self,head):
        self.head_portrait=head

    def add_friend(self,newone):
        self.friend_list.append(newone)

    def add_tag(self,newtag):
        self.tags.append(newtag)

    def setjob(self,newjob):
        self.job=newjob

class Student(People):
    def __init__(self):
        super().__init__()
        self.sim_job=0
        self.clubs=[]
        self.classes=[]
        self.team=''

    def setsim_job(self,sim):
        self.sim_job=sim

    def join_club(self,club):
        self.clubs.append(club)

    def join_class(self,newclass):
        self.classes.append(newclass)

    def set_team(self,team):
        self.team=team

class Directors(People):
    def __init__(self):
        super().__init__()
        self.team=''

    def set_team(self,team):
        self.team=team

