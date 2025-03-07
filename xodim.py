class Xodim:
    def __init__(self,ismi,ish_yili,maoshi,lavozimi):
        self.ismi=ismi
        self.ish_yili=ish_yili
        self.maoshi=maoshi
        self.lavozimi=lavozimi

    def kiritish(self):
        self.ismi=input("xodim ismini kiriting: ")
        self.ish_yili=int(input("ish yili kiriting: "))
        self.lavozimi=input("lavozimni kiriting --Manager yoki Engineer--: ")
        if self.lavozimi.lower()=="manager":
            self.maoshi=10000  
        elif self.lavozimi.lower()=="engineer":
            self.maoshi=5000  
        else:
            self.maoshi=0

    def chiqarish(self):
        print(f"ismi. {self.ismi} ish yili. {self.ish_yili} maoshi. {self.maoshi} lavozimi. {self.lavozimi}")

class Manager(Xodim):
    def maoshni_hisoblash(self):
        self.maoshi=12000  

class Engineer(Xodim):
    def maoshni_hisoblash(self):
        self.maoshi=7000 


xodimlar = []

for i in range(2): 
    print("\nXodim ma'lumotlarini kiriting:")
    xodim = Xodim("",0,0,"")
    xodim.kiritish()
    xodimlar.append(xodim)

print("\n5 yildan kop ishlaganlar")

for xodim in xodimlar:
    if xodim.ish_yili>5:
        xodim.chiqarish()
