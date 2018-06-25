#Ques1.

class Animal:
    def Animal_attribute(self):
        print("ox")
class Tiger(Animal):
     print("ape")
t=Tiger()
t.Animal_attribute()


#Ques2.

print("output = (A,B),(A,B)")


#Ques3.

class Cop():
    def __init__(self,name,age,work,designation,experience):
        self.n= name
        self.a= age
        self.w= work
        self.d= designation
        self.e= experience
    def add(self):
        print("follwing details of the cop is")
    def display(self):
        print("name is : " + self.n)
        print("age is : " + self.a)
        print("work is : " + self.w)
        print("designation is : " + self.d)
        print("experience is : " + self .e)
    def Update(self,name,age,work,designation,experience):
        self.z= name
        self.x= age
        self.c= work
        self.v= designation
        self.b= experience
        print("name is : " + self.z)
        print("age is : " + self.x)
        print("work is : " + self.c)
        print("designation is : " + self.v)
        print("experience is : " + self.b)
class Mission(Cop):
    print("mission details of cop")
m=Mission("arti",str(20),"work for navy","no experience","navy")
m.add()
m.display()
m.Update("priya",str(22),"work for police","completed 5 mission","police")


#Ques4.

class Shape:
    def __init__(self,lenth,breadth):
       self.l= lenth
       self.b= breadth
class Rectangle(Shape):
    def area1(self):
        rectangle= self.l*self.b
        print(rectangle)

class Square(Rectangle):
    def area2(self):
        square= self.l*4
        print(square)
m=Square(2,4)
m.area1()
m.area2()

