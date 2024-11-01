import random
from time import sleep

def generate_cpf():
    state = input("Which state are you from?\n").upper()
    full_num = f"{random.randint(0, 99999999):08}"

    ninth_number = 1
    if state == "RS":
        ninth_number = 0
    elif state in ["PA", "AM", "RO", "RR", "AP", "AC"]:
        ninth_number = 2
    elif state in ["CE", "MA", "PI"]:
        ninth_number = 3
    elif state in ["AL", "PB", "PE", "RN"]:
        ninth_number = 4
    elif state in ["BA", "SE"]:
        ninth_number = 5
    elif state == "MG":
        ninth_number = 6
    elif state in ["ES", "RJ"]:
        ninth_number = 7
    elif state == "SP":
        ninth_number = 8
    elif state in ["PR", "SC"]:
        ninth_number = 9
    full_num = str(full_num) + str(ninth_number)

    def calculate_d10_d11(full_num):
        m = 0
        for n, num in enumerate(full_num):
            m += (int(num) * (10-n))
        r = m%11
        if r == 0 or r == 1:
            return "0"
        else:
            return str(11 - r)
        
    full_num += calculate_d10_d11(full_num)
    full_num += calculate_d10_d11(full_num[1:])

    return full_num

def cpf_checker(full_num):
    full_num = str(full_num)
    if len(full_num) != 11:
        print("length not corresponds to standard")
        return False
    else:
        m = 0
        for n, num in enumerate(full_num[:9]):
            m += (int(num) * (10-n))
        r = m%11
        if r == 0 or r == 1:
            if full_num[9] != "0":
                print("10th number is wrong")
                return False
        else:
            if full_num[9] != str(11 - r):
                print("10th number is wrong")
                return False
            
        m2 = 0
        for n, num in enumerate(full_num[:10]):
            m2 += (int(num) * (11-n))
        r2 = m2%11
        if r2 == 0 or r2 == 1:
            if full_num[10] != "0":
                print("11th number is wrong")
                return False
        else:
            if full_num[10] != str(11 - r2):
                print("11th number is wrong")
                return False
    return True


while True:
    print("\n", "-"*150)
    print("What do you want to do?")
    print("1 - Generate CPF")
    print("2 - Check CPF")
    print("-"*150, "\n")
    action = input()
    if action == "1":
        print("\nThe CPF is:", generate_cpf())
        sleep(1)
    elif action == "2":
        print("What's the CPF?")
        cpf = input()
        print(f"The cpf: {cpf} is {cpf_checker(cpf)}")
        sleep(1)
    else:
        print("Action not recognized")
        sleep(1)