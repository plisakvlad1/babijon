class Student():
    def _init_(self,name,surname,age,logiks,group,login,password,telegram):
        self.name = name
        self.surname = surname
        self.age = age
        self.logiks = logiks
        self.group = group
        self.login = login
        self.password = password
        self.telegram = telegram

    def all_info(self):
        print("All infomation of student")
        print("Name -",self.name)
        print("Surname -",self.name)
        print("Age -",self.name)
        print("Logiks -",self.name)
        print("Group -",self.name)
        print("Login -",self.name)
        print("Password -",self.name)
        print("Telegram -",self.name)
        print("===========================================================")
    def logik_info(self):
        print("=========================Logiks of Student=========================")
        lg = ""
        for logik in self.logiks:


















