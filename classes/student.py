class Student:
    school="AkiraChix"
    def __init__(self,first_name, last_name, age, country):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.country=country 
    def greet_student(self):
        return f"Hello {self.name} from {self.country} welcome to {self.school}"  

    def  show_full_name(self):
        return self.first_name+" "+self.last_name

    def  year_of_birth(self):
        year=2023-self.age
        return year

    def show_initials(self):
        return self.first_name[0].upper()+self.last_name[0].upper()   


