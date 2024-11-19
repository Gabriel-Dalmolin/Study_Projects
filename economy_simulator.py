# ECONOMY SIMULATOR - Objective: Practicing object oriented programming 

import random

crisis_level = 1

names = [
    "James", "Mary", "John", "Patricia", "Robert", "Jennifer", "Michael", "Linda", "William", "Elizabeth",
    "David", "Barbara", "Richard", "Susan", "Joseph", "Jessica", "Thomas", "Sarah", "Charles", "Karen",
    "Christopher", "Nancy", "Daniel", "Margaret", "Matthew", "Lisa", "Anthony", "Betty", "Mark", "Dorothy",
    "Paul", "Sandra", "Steven", "Ashley", "Andrew", "Kimberly", "Joshua", "Donna", "Kenneth", "Emily",
    "Kevin", "Michelle", "Brian", "Carol", "George", "Amanda", "Edward", "Melissa", "Ronald", "Deborah",
    "Timothy", "Stephanie", "Jason", "Rebecca", "Jeffrey", "Laura", "Ryan", "Sharon", "Jacob", "Cynthia",
    "Gary", "Kathleen", "Nicholas", "Amy", "Eric", "Shirley", "Jonathan", "Angela", "Stephen", "Helen",
    "Larry", "Anna", "Justin", "Brenda", "Scott", "Pamela", "Brandon", "Nicole", "Frank", "Emma",
    "Benjamin", "Samantha", "Gregory", "Katherine", "Samuel", "Christine", "Raymond", "Debra", "Patrick", "Rachel",
    "Alexander", "Catherine", "Jack", "Carolyn", "Dennis", "Janet", "Jerry", "Ruth", "Tyler", "Maria"
]

class enterprise():
    def __init__(self, name, money, mean_production, employees=[]):
        self.name = name
        self.money = money
        self.storage_products = 0 
        self.mean_production = mean_production
        self.employees = employees
        self.running = True

    def produce(self):
        self.storage_products += random.randint(int(self.mean_production*0.75), int(self.mean_production*1.25))*(1/crisis_level)
        return self.storage_products
    
    def sell_products(self, quantity="all"):
        if quantity == "all":
            quantity = self.storage_products
        if quantity >= self.storage_products:
            selling_price = random.randint(int(mean_selling_price*0.75), int(mean_selling_price*1.25))*(1/crisis_level)
            self.money += selling_price*quantity
            self.storage_products -= quantity
            return quantity
        else:
            return "Insufficient storage"
        
    def pay_employees(self):
        for employee in self.employees:
            if self.money > employee.salary:
                employee.money += employee.salary
                self.money -= employee.salary
            else:
                self.bankrupt() 
            
    def bankrupt(self):
        self.running = False

        
    def __str__(self):
        return f"Enterprise: {self.name} | Money: {self.moneys}"
    
class Market():
    def __init__(self):
        self.storage = 0
        self.enterprises = []

    def add_enterprise(self, _enterprise):
        self.enterprises.append(_enterprise)

    def getting_storage_from_enterprises(self):
        storage_sum = 0
        for _enterprise in self.enterprises:
            storage_sum += _enterprise.storage_products
        self.storage += storage_sum

    def sell(self, quantity, person):
        _mean_selling_price = random.randint(int(mean_selling_price*0.75), int(mean_selling_price*1.25))*(1/crisis_level)
        if person.money > quantity * _mean_selling_price:
            person.products += quantity
            person.money -= _mean_selling_price*quantity
            return True
        else:
            return False
            

class person():
    def __init__(self, name, salary, necessary_products_pmonth, money=0):
        self.name = name
        self.salary = salary 
        self.necessary_products_pmonth = necessary_products_pmonth
        self.money = money
        self.products = 0
        self.alive = True

    def consume(self, market):
        return market.sell(self.necessary_products_pmonth, self)
    
    def die(self):
        self.alive = False

    def __str__(self):
        return f"Person {self.name}"

def simulate():
    global crisis_level

    market = Market()
    employees_per_enterprise = num_of_persons//num_of_enterprises


    # Creating the persons
    persons = [person(
        random.choice(names), 
        random.randint(int(mean_salary*0.5), int(mean_salary*2)), 
        random.randint(int(mean_necessary_products_pmonth*0.5), int(mean_necessary_products_pmonth*2))) 
        
        for i in range(num_of_persons)]
    

    enterprises = [enterprise(
            i, 
            0, 
            random.randint(int(mean_production*0.5), int(mean_production*2)), 
            persons[(employees_per_enterprise*(i-1)) : (employees_per_enterprise*(i))])
        
            for i in range(1, num_of_enterprises+1)]

    
    for month in range(num_of_months):
        print(f"MONTH {month} ___________________________________________________________________\n")
        
        crisis_level *= (random.randint(int(80*crisis_multiplier), int(120*crisis_multiplier))/100*crisis_multiplier)

        for _enterprise in enterprises:
            if _enterprise.running:
                _enterprise.produce()
                _enterprise.sell_products()
                _enterprise.pay_employees()
                print("Enterprise:", _enterprise.name, "now has", _enterprise.money)
            else:
                print(f"Enterprise: {_enterprise.name} bankrupt")
            

        for _person in persons:
            if _person.alive:
                _person.consume(market)

    
        


# ------------------------- Control Pannel
mean_selling_price = 10
num_of_persons = 30
num_of_enterprises = 5 
mean_salary = 3000
mean_necessary_products_pmonth = 150
mean_production = 3000
crisis_multiplier = 1  # <--- Get this thing up with caution, it really can mess up everything
num_of_months = 12

simulate()