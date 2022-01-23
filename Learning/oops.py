# This is my way to understand POOP

class Quark():
    def __init__(self):
        print("Quark works!")
        self.word = "WTF, type something you dumbass"
    def iwant(self):
        print("Take your", self.word)

class Proton(Quark):
    def __init__(self):
        super().__init__()
        print("Proton works!")
        print(self.word)
    def iDontWant(self):
        print("Ok, you won't get", self.word, "then.")

class Nucleus(Proton):
    def __init__(self):
        super().__init__()
        print("Nucleus works!")
        print(self.word, "(This one is from Nucleus)")
    def doYouWant(self):
        a = input("Do you want pikachu? (y/n) : ")
        if a == "y":
            print("Take your pikachu")
        elif a == "n":
            print("Ok, you won't get pikachu")
        else :
            print(self.word)
# ganesh0=Quark().iwant()
# ganesh1=Proton().iDontWant()
ganesh3=Nucleus().doYouWant()