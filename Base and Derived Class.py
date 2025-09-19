class stud:
    def __init__(self,a,b,c):
        self.sno=a
        self.sname=b
        self.sage=c
    def disp(self):
        print("Student Number:",self.sno)
        print("Student Name:",self.sname)
        print("Student Age:",self.sno)
        
class marks(stud):
    def __init__(self,a,b,c,m1,m2,m3):
        super().__init__(a,b,c)
        self.mark1=m1
        self.mark2=m2
        self.mark3=m3
    def disp(self):
        super().disp()
        print("Mark 1:",self.mark1)
        print("Mark 2:",self.mark2)
        print("Mark 3:",self.mark3)
ob=marks(18,"xyz",20,60,70,80)
ob.disp()
