#f string:(f')
class Student:
    def __init__(self,name,roll,address,email):
        self.name=name  
        self.roll=roll
        self.address=address
        self.email=email
    def __str__(self):
        return f'{self.name} {self.roll} {self.address} {self.email}'

s1=Student("srija",102,"hyderabad","srija25@gmail.com")
print(s1)
