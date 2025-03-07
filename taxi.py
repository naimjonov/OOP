class Taksi:
    def __init__(self,haydovchi,mashina_nomi):
        self.haydovchi=haydovchi
        self.mashinanomi=mashina_nomi
        self.__narx=0 
        self.__yonalish=""
        self.__boshjoylar=0 

    
    def get_narx(self):
        return self.__narx

    
    def set_bosh_joylar(self,yangibosh_joylar):
        if yangibosh_joylar>=0:
            self.__boshjoylar=yangibosh_joylar
        else:
            print("Xato! Bo'sh joylar soni manfiy bo'lmasligi kerak.")

    
    def set_haydovchi(self,yangi_haydovchi):
        self.haydovchi=yangi_haydovchi

    def set_mashina_nomi(self,yangi_mashina_nomi):
        self.mashinanomi=yangi_mashina_nomi

    def set_narx(self,yangi_narx):
        self.__narx=yangi_narx

    def set_yonalish(self, yangiyonalish):
        self.__yonalish=yangiyonalish

    def get_bosh_joylar(self):
        return self.__boshjoylar

    def get_yonalish(self):
        return self.__yonalish

    def get_haydovchi(self):
        return self.haydovchi

    def get_mashina_nomi(self):
        return self.mashinanomi

taksi=Taksi("", "")
taksi.set_haydovchi(input("shopirismini kiriting: "))
taksi.set_mashina_nomi(input("moshina nomini kiriting: "))
taksi.set_narx(float(input("taxi narxini kiriting: ")))
taksi.set_yonalish(input("yonalishni kiriting: "))
taksi.set_bosh_joylar(int(input("bosh joylar sonini kiriting: ")))

print(f"\nshofir.{taksi.get_haydovchi()}")
print(f"moshina.{taksi.get_mashina_nomi()}")
print(f"narx.{taksi.get_narx()} so'm")
print(f"yonalish.{taksi.get_yonalish()}")
print(f"bosh joylar.{taksi.get_bosh_joylar()}")
