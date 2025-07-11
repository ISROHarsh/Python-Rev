# 1. Create a class “Programmer” for storing information of few programmers working at Microsoft.
class Programmer:
    def __init__(self,nm,emp_id,lng,exp):
        self.nm     = nm
        self.emp_id = emp_id
        self.lng    = lng
        self.exp    = exp
        self.cmp    = "Microsoft"

    def get_details(self):
        print(f"""                  Name: {self.nm}
           Employee Id: {self.emp_id}
              Language: {self.lng}
            Experience: {self.exp} Years
               Company: {self.cmp}
              """)

# 2. Write a class “Calculator” capable of finding square, cube and square root of a number. 
class Calculator:
    def sqr(self):
        print(self*self)

    def cube(self):
        print(self*self*self)
        
    def root(self):
        print(round(pow(self,0.5),2))
Calculator.root(2)

# 3. Create a class with a class attribute a; create an object from it and set ‘a’ directly using ‘object.a = 0’. Does this change the class attribute? 
class object:
    a = 1
    print(a)
object.a = 0
print(object.a) # No this is just an instance attribute but the class attribute remains

# 4. Add a static method in problem 2, to greet the user with hello. 
class Calculator:
    @staticmethod
    def greet():
        print("Good Morning vau")

    def sqr(self):
        print(self*self)

    def cube(self):
        print(self*self*self)
        
    def root(self):
        print(pow(self,0.5))
        
# 5. Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) and get fare information of train running under Indian Railways.
class Train:
    def __init__(self, nm):
        self.nm = nm
        self.board = None        
        self.deboard = None
        self.date = None
        self.passen = 0
        print(f"Indian Railways Welcomes You {self.nm}!!")
    
    def book_ticket(self):
        self.board   = input("Enter the name of boarding station: ")
        self.deboard = input("Enter the name of deboarding station: ")
        self.date    = input("Enter the date of journey (fmt = dd/mm/yyyy): ")
        self.passen  = int(input("Enter number of passengers travelling: "))
        print(f"{self.nm} your informations have been saved!!")
        
    def status(self):
        com = {
         ('Chennai', 'Delhi'): 115,
         ('Chennai', 'Mumbai'): 67,
         ('Chennai', 'Bengaluru'): 31,
         ('Delhi', 'Mumbai'): 56,
         ('Delhi', 'Bengaluru'): 86,
         ('Mumbai', 'Bengaluru'): 69
        }
        if self.board and self.deboard in ['Chennai',"Delhi",'Mumbai','Bengaluru']:
            print(f"There are {com.get((self.board,self.deboard))} seats left")
        else:
            print("No Trains Available !! hehehehhe")
    
    def fair_info(self):
        com = {
         ('Chennai', 'Delhi'): 2194,
         ('Chennai', 'Mumbai'): 1333,
         ('Chennai', 'Bengaluru'): 300,
         ('Delhi', 'Mumbai'): 1250,
         ('Delhi', 'Bengaluru'): 2147,
         ('Mumbai', 'Bengaluru'): 900
        }
        print(""" The fare prices are as follows.
              [1] for every km in Second class = Rs. 2.5
              [2] for every km in Sleeper class = Rs. 4.2
              [3] for every km in AC 3 Tier = Rs. 5.5
              [4] for every km in AC 2 Tier = Rs. 6.5
              [5] for every km in AC 1 Tier = Rs. 9       
             """)
        prc = [2.5,4.2,5.5,6.5,9]
        self.st_type = int(input("Enter your travel seat choice: "))
        print(f"Your final pay to price would be {com.get((self.board,self.deboard)) * prc[self.st_type - 1]}")

harsh = Train("Harsh")
harsh.book_ticket()
harsh.status()
harsh.fair_info()

# 6. Can you change the self-parameter inside a class to something else (say “harry”). Try changing self to “slf” or “harry” and see the effects.
class hehe:
    def greet(harry,name):
        harry.name = name
        print(name + " hellow vau")

harsh = hehe()
harsh.greet("harsh")

#self is just a convention, the parameter could be anything. Self is a standard one