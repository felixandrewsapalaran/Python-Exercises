# OOP Demos


# Demonstrate the use of Classes & Objects

class Employee:
    # class attribute
    # this counts the number of employee
    num_employee = 0

    # set up instance attributes
    def __init__(self, name, age, company, salary):
        self.name = name
        self.age = age
        self.company = company
        self.salary = salary
        
        # increment the num of Employee
        Employee.num_employee += 1
    
    # create another instance method
    # that would display employee infomartion
    def display_employee_info(self):
        print(f"""
        Name: {self.name} 
        Age: {self.age}
        Company: {self.age}
        Salary: {self.salary:,.2f}
        """)

# create 1st object of Employee class
emp1 = Employee("Zara", 25, "Facebook", 200_543)
# create 2nd object 
emp2 = Employee("Manni", 37, "Google", 500_300)
# create 3erd object
emp3 = Employee("Jane", 46, "Twitter", 103_512)

# display employees info
emp1.display_employee_info()
emp2.display_employee_info()
emp3.display_employee_info()

# print the total employee
print(f"Total Employee: {Employee.num_employee}\n")





# Demonstrate the use of Encapsulation & Abstraction

class BMI:
    
    # create a function that will calculate the user's BMI
    def calculate_BMI(self):
        # capture the user weight and height
        self.weight = float(input("\nEnter your weight in kg: "))
        self.height = float(input("Enter your height in meters: "))

        # calculate the user's BMI
        self.bmi = self.weight / (self.height * self.height)
        print(f"Your BMI is: {self.bmi}")

        # determine if user is underweight or overweight
        if self.bmi < 18.5:
            print("Your are underweight")
        elif self.bmi > 18.5 and self.bmi < 24.9:
            print("You are healthy")
        elif self.bmi > 24.9 and self.bmi < 29.9:
            print("Your are overweight")
        elif self.bmi >= 30:
            print("You are obese")

# create an object of this class BMI
bmi = BMI()

# use while loop to keep prompting the user 
# until they chooose to exit
while True:
    # display the user options
    # capture user input
    choice = int(input(f"""
    
    Welcome to myBMI App

    1. Calculate Your BMI
    2. Exit

    Choice: """))

    if choice == 1:
        # calculate user BMI
        bmi.calculate_BMI()
    elif choice == 2:
        # exit program
        print("Thank you for using the app")
        exit()


'''Test Cases 

# HEALTHY
Height - 1 meter
Weight - 20 kg

# underweight 
Weight - 15 kg

# overweight
Weight - 25 kg

# obese
Weight - 30 kg


'''





# Demonstrate the use of Inheritance & Single Inheritance

class Person:
    # setting up our attributes
    def setData(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

# creater another class that 
# would inherit all properties
# from parent class
class Teacher(Person):
    # child class has its own attributes
    def __init__(self, salary):
        self.salary = salary
    
    # function will show teacher data
    def showTeacherData(self):
        print(f"""
        Name: {self.name}
        Age: {self.age}
        Gender: {self.gender}
        Salary: ${self.salary:,.2f}
        """)

# create 1st object of class Teacher
teacher = Teacher(90_000)
# access the setdata
teacher.setData("Angelina Jolie", 45, "Female")
# display our teacher data
teacher.showTeacherData()




# Demonstrate the use of Polymorphism

class Philippines:
    def language(self):
        print("Tagalog\n")

# child class 
class Iloilo(Philippines):
    def language(self):
        print("ilonggo\n")

# create another child class
class Mindanao(Philippines):
    def language(self):
        print("maguindanaon")

# create object of class Philippines, Iloilo, Mindanao
philippines = Philippines()        
iloilo = Iloilo()
mindanao = Mindanao()

# access each language for each regions
print("There are 3 languages in Philippines they are: \n")
manila_lang = philippines.language()
iloilo_lang = iloilo.language()
mindanao_lang = mindanao.language()
