from jvm.runtime.nclass import NativeClass

class Boo(NativeClass):
    def __init__(self):
        self.name = "board/based/Boo"
        self.methods = {
            "sayBoo-()V": self.sayBoo,
            "scareYou-(Ljava/lang/String;)V": self.scareYou
        }
    
    def sayBoo(self):
        print("Boo!")
    
    def scareYou(self, name):
        print(f"{name} is scared of Boo!")