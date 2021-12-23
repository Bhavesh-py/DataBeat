#First Principle: "Single Responsibility Principle".
"""According to this principle one class should have only one responsibility"""

"""Consider a company "Rajani Enterprises" which deals in IT Outsourcing, the company needs to add
the employee data into the database."""

class  Employee:
    def __init__(self, name):
        self.name = name
    
    def get_name(self):
        pass

    def save(self, info):
        pass
    
    
"""In the above code snippet, the first principle has been violated and the correct code snippet that
does not violates the first principle is:"""
class  Data:
    def __init__(self, name):
        self.name = name
    
    def get_data(self):
        pass
    
class  Database:
    def save(self, info):
        pass

"""As we can see that now there are two classes, one is responsible for getting the data and the
other one is responsible for saving the data"""


"""------------------------------------------------------------------------------------------------"""


#Second Principle: "Open-Closed Principle".
"""According to this principle,
the classes and methods should be open for extension and closed for modification. """

"""Consider it is festive season and Mr. Bhavesh Rajani, the founder of Rajani Enterprises wishes 
to reward all the employees based on their position (20% to the sde) and (10% percent to the tester)"""


class Employee:
  def __init__(self, name, position, salary):
      self.name = name
      self.position = position
      self.salary = salary
      
  def give_bonus(self):
      if self.position == "sde":
          return self.salary * 0.2
      elif self.position == "tester":
          return self.salary * 0.1

"""The above code snippet violated the second principle because if we want to add another profile
we will have to modify the "give_bonus()" method. The correct code snippet would be:"""


class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary
        
    def give_bonus(self):
        return self.salary * 0.1
  
class SDEBonus(Employee):
    def give_bonus(self):
        return super().give_bonus() * 2

"""As we acn see,now if we wish to add another profile (lets say team lead), we can create another
class TeamLeadBonus and give the required bonus"""


"""------------------------------------------------------------------------------------------------"""


# Third Principle: "Liskov Substitution Principle":
"""According to this principle Functions that use pointers of references to base classes must 
be able to use objects of derived classes without knowing it."""

"""Assume, at Rajani Enterprises there is a rule that no SDE will deal withclients directly, 
only the developer advocates will deal with the client and inform to the SDE regarding the requirements"""


class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary
    
    def drink_coffee(self):
        return "Drinking Coffee"
    def have_lunch(self):
        return "Having Lunch"
    def deal_with_client(self):
        return "Dealing with Client"
    
class SDE(Employee):
    def drink_coffee(self):
        return "SDE is drinking coffee"
    
class DeveloperAdvocate(Employee):
    def deal_with_client(self):
        return "Developer Advocate is in a client meeting"
    
"""The problem in the above code snippet is that we can make an SDE deal with the client. 
The Employee class violates the second principle, due to the deal_with_client method in 
this example. Since an SDE cannot deal with the client directly,
we should not be able to call the deal_with_client method for SDEs."""

class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary
    
    def drink_coffee(self):
        return "Drinking Coffee"
    def have_lunch(self):
        return "Having Lunch"
    
class DeveloperAdvocateClass(Employee):
    def deal_with_client(self):
        return "Dealing with Client"

class SDE(Employee):
    def drink_coffee(self):
        return "SDE is drinking coffee"
    
class DeveloperAdvocate(DeveloperAdvocateClass):
    def deal_with_client(self):
        return "Developer Advocate is in a client meeting"
    
"""In the abopve code snippet the SDE now cannot call the "deal_with_client" method"""


"""------------------------------------------------------------------------------------------------"""


# Fourth Principle: "Interface Segregation Principle":
"""According to this principle Classes should not be forced to depend on methods that they do not use."""

"""Assume at Rajani Enterprises is working on multiple projects together, and the manager 
has assigned the SDE1 the task to work on Project1"""

class Projects():
    def Project1():
        raise NotImplementedError
  
    def Project2():
      raise NotImplementedError
  
    def Project3():
        raise NotImplementedError
    
class SDE1(Projects):
  def Project1():
    return "Started working on Project1"
  
  def parse_JSON():
    pass
  
  def parse_other():
    pass

"""In the above code snippet,The SDE1 starts working on Project1 BUT It would still carry 
the Project2() and the  Project3() from the interface,and since SDE1 does not need it, 
He/She will have to pass. This forces SDE1 to work with methods that they do not need."""

class ProjectOne():
    def Project1():
        raise NotImplementedError

class ProjectTwo():
    def Project2():
        raise NotImplementedError
        
class ProjectThree():
    def Project3():
        raise NotImplementedError
        
class SDE1(ProjectOne):
  def Project1():
    return "Started working on Project1"

"""The SDE1 one now doesn't need to pass the methods that are not required"""


"""------------------------------------------------------------------------------------------------"""


#Fifth Principle: "Dependency Inversion Principle".
"""According to this principle, The High-level modules should not depend on low-level modules.
Both should depend on abstractions."""

"""Assume, at Rajani Enterprises, we want to implement a manager class 
for the company and assign to employees that are supervised by him/her."""

class Manager(): 
    def __init__(self): 
        self.SDEs=[] 
        self.DevAdvocates=[] 
        self.Testers=[] 
  
    def add_sde(self,sde): 
        self.SDEs.append(sde) 
          
    def add_devAdvocate(self,devAdvocate): 
        self.DevAdvocates.append(devAdvocate) 
          
    def add_tester(self,tester): 
        self.Testers.append(tester) 
        
class SDE(): 
    def __init__(self): 
        print("SDE added")

class DevAdvocate(): 
    def __init__(self): 
        print("Developer Advocate added")

class Tester(): 
    def __init__(self): 
        print("Tester added")
        
"""There is a problem in the above code snippet which is, If there comes another employee
under the manager (e.g Designer) then the whole class will have to be redesigned."""

class Employee(): 
    def task(): 
        pass

class Developer(Employee): 
    def __init__(self): 
        print("SDE added")
    def task():
    	print("Code")  
        
class DevAdvocate(Employee): 
    def __init__(self): 
        print("Developer Advocate added")
    def task():
    	print("Client Meeting")
        
class Tester(Employee): 
    def __init__(self): 
        print("Tester added")
    def work():
    	print("Testing")
        
class Manager(): 
    def __init__(self): 
        self.employees=[] 
    def add_employee(self,a): 
        self.employees.append(a) 
        
"""Now if any other employee is added it can be simply added to Manager,
without the need to make the Manager explicitly aware of it."""