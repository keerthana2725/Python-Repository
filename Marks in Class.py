class stud:
    def __init__(self,a,b,c,m1,m2,m3):
        self.sno=a
        self.sname=b
        self.age=c
        self.mark1=m1
        self.mark2=m2
        self.mark3=m3
        
    def calculate(self):
        self.tot=m1+m2+m3
        self.avg=self.tot/3
        print("Total Marks="  ,self.tot)
        print("Average ="     ,self.avg)
        if m1>=40 and m2>=40 and m3>=40:
            self.result="Pass"
        else:
            self.result="Fail"
           
    def display(self):
        print('Student Number:',self.sno)
        print('Student Name:',self.sname)
        print('Student Age:',self.age)
        print('Mark 1=:',self.mark1)
        print('Mark 2=:',self.mark2)
        print('Mark 3=:',self.mark3)
        print('total=:',self.tot)
        print('average=:',self.avg)
        print('result=:',self.result)
        
x=int(input("Enter Roll Number:"))
y=input("Enter Name:")
z=int(input("Enter Age:"))
m1=int(input("Enter M1:"))
m2=int(input("Enter M2:"))
m3=int(input("Enter M3:"))

obj=stud(x,y,z,m1,m2,m3)
obj.calculate()
obj.display()

        
