'''
while-->intialized statement,counter...
'''
#banking scenari-->pin authentiication if more than
#
'''
pin="2612"
max_attempts = 3
current_attempt = 0
while current_attempt < max_attempts :
    enter_pin = input("Enter the ATM PIN")
    if enter_pin == pin :
        print("log in successfull")
        print("withdraw the amount")
        break
    else:
        print("entered pin is wrong.try again carefully")
        current_attempt += 1
else:
    print("account locked try again ...")
'''
#BMI scenario (user case),we will makeuse of control block statements:
#bmi-->body ,mass index -->bmi = weight(kgs)/(height**) (meteres)
'''
feet-->1 feet --->12 inches-->2.54cm-->30.48cms
---->5 feet 6 inches-->1.167meters
'''
n=int(input("how many user"))
for i in range(n):
    weight = int(input("enter the weight in kgs:"))
    height = float(input("enter your height metres:"))
    name = input("enter name")
    if weight > 0 and height > 0:
        bmi= (weight)/ ((height)**2)
        if bmi < 18.5:
            print(f'{name}--> you are underweight as BMI is {bmi}')
        elif bmi >=25 and bmi <=24.9:
            print(f'{name}-->you are prefect phisque, bmi is {bmi}')
        elif bmi >=25 and bmi <=29.9:
            print(f'{name}-->you are overweight need to maintain diet{bmi}')
        elif bmi>=30:
            print(f'{name}-->obesity,bmi is {bmi}')
    else:
        print(f'enter only +ve values')


