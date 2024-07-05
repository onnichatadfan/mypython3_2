def Fa(C):
    F = (9/5)*C+32
    return F

def Kal(C):
    K = C+273.15
    return K

C = int(input("รับค่าองศาเซลเซียส:"))
print("องศาฟาเรนไฮส์ %.2f" % Fa(C))
print("องศาเคลริน %.2f" % Kal(C))