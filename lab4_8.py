def bmi(cm, kg):
    b = kg/(cm/100)**2
    return b

#ให้เขียนฟังก์ชั่นเปรียบเทียบเพิ่ม
def compare(bmi):
    if bmi < 18.50:
        print("น้ำหนักน้อย")
    elif bmi >= 18.50 and  bmi <= 22.90:
        print("ปกติ(สุขภาพดี)")
    elif bmi >= 23 and  bmi <= 24.90:
        print("ท้วม")
    elif bmi >= 25 and  bmi <= 29.90:
        print("อ้วน")
    elif bmi > 30:
        print("อ้วนมาก")

#ให้เขียนรับค่าส่วนสูงและน้ำหนัก
a = int(input("รับค่าส่วนสูง "))
c = int(input("รับค่าน้ำหนัก "))
print("BMI= %.2f" % bmi(a,c))
compare(bmi(a,c))