def bmi(kg, cm):
    BMI = kg/(cm/100)**2
    return BMI

def check(b):
    if(b < 18.50):
        print("น้ำหนักต่ำกว่าเกณฑ์")
    elif(b >= 18.50 and  b <= 22.90):
        print("สมส่วน")
    elif(b >= 23 and  b <= 24.90):
        print("น้ำหนักเกิน")
    elif(b >= 25 and  b <= 29.90):
        print("โรคอ้วน")
    elif(b >= 30):
        print("โรคอ้วนอันตราย")

kg = int(input("น้ำหนัก "))
cm = int(input("ส่วนสูง "))
print("BMI= %.2f" % bmi(kg,cm))
check(bmi(kg,cm))