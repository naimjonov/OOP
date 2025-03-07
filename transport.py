class Transport:
    def harakatlanish(self):
        pass

class Mashina(Transport):
    def harakatlanish(self):
        print("Moshina gildiraklar yordamida harakatlanadi")

class Velosiped(Transport):
    def harakatlanish(self):
        print("velosaped pedalar yordamida harakatlanadi")

class Samolyot(Transport):
    def harakatlanish(self):
        print("samolyot uchib harakatlanadi")

print("qnaqa transpor tanlsaysiz")
tanlov = input()

if tanlov.lower()=="mashina":
    transport=Mashina()
elif tanlov.lower()=="velosiped":
    transport=Velosiped()
elif tanlov.lower()=="samolyot":
    transport=Samolyot()
else:
    print("bizda unday tranport yoq😁")
    exit()

transport.harakatlanish()
