class Calculator(): 
    @staticmethod
    def add(first_num, second_num):
        return first_num + second_num
    
    @staticmethod
    def subtract(first_num, second_num):
        return first_num - second_num

    @staticmethod
    def multiply(first_num, second_num):
        return first_num * second_num
        
    @staticmethod
    def divide(first_num, second_num):
        return first_num / second_num
    
    @staticmethod
    def power(first_num, second_num):
        return first_num ** second_num
    
    @staticmethod
    def root(first_num, second_num):
        return first_num ** (1/second_num)
    
    @staticmethod
    def factorial(num):
        mult = 1
        for i in range(1, num+1):
            mult *= i
        return mult
    
    @staticmethod
    def mean(num_list):
        return sum(num_list)/len(num_list)
    
    @staticmethod
    def median(num_list):
        num_list.sort()
        middle_num = len(num_list)//2
        if len(num_list) % 2 != 0:
            return num_list[middle_num]
        else: 
            return Calculator.mean([middle_num, middle_num+1])

    
print("3 Root of 8 is:", Calculator.root(8, 3))
print("Factorial of 5 is:", Calculator.factorial(5))
print("The mean of 15, 35, 70 and 60 is:", Calculator.mean([15, 35, 70, 60]))
print("The median of 2, 3, 4 and 1 is:", Calculator.median([2,3,4,1]))