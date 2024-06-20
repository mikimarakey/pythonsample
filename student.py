# class Student:
#     def SayHello(self):
#         print("Hello " + self.FName)
        
# s1 = Student()
# s2 = Student()
# s1.FName="Redwan"
# s1.SayHello()

# # print(id(Abebe))
# # print(id(Redwan))

# Constructor
class Student:
     def __init__(self,fname,lname):
         self.fname=fname
         self.lname=lname
         
     def GetFullName(self):
         print("Your Full Name is " + self.fname, self.lname)
         
s1=Student("Yoseph","Kassaye")
s1.GetFullName()

            
