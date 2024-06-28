#ชนิดข้อมูลแบบ Tuple --> Immutable
person = ("Onnicha",18,161,50,"6529011040@cdti.ac.th")
print(person)
#person[1] = 19
print("อายุ %d" % (person[1]))
print("ส่วนสูง %d น้ำหนัก %d" % (person[2], person[3]))
print("อีเมล %s" % (person[4]))