#ชนิดข้อมูล Dictionary
x = {
     "name": "อรณิชา ทัดฝัน",
     "age":18,
     "wt":50,
     "h": 161
     }
print(x)
print("สวัสดีค่ะคุณ %s" % x ["name"])
print("พ.ศ.เกิด %d อายุ %d" % (2567-x["age"], x["age"]))
print("น้ำหนัก %d ส่วนสูง %d" % (x["wt"], x["h"]))