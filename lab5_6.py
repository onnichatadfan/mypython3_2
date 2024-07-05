def beforMidterm(a,c,b):
    d = a+b+c
    return d

score = int(input("รับค่าคะแนนเก็บ: "))
jitpisai = int(input("รับค่าคะแนนจิตยิสัย: "))
Midterm = int(input("รับค่าคะแนนกลางภาค: "))
print("ผลรวม %.2f" % beforMidterm(score, jitpisai, Midterm))