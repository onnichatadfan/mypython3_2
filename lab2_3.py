print("วิธีคำนวณ BMI ในการหาค่าดัชนีมวลกาย")
kg = int(input("น้ำหนักตัว: "))
cm = int(input("ส่วนสูง: "))
bmi = kg/(cm/100)**2
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