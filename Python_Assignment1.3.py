# The diameter of sphere is 12 cm means radius would be 6 cm(diameter/2)
d = input("Please enter the diameter of sphere in cm : ")

def volumeofsphere(d):
    r = int(d)/2
    V= (4/3)*3.14*(r*r)
    return V

VOS = volumeofsphere(d)
print(VOS)