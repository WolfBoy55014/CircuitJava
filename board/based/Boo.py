from jvm.runtime.nclass import NativeClass

class Boo(NativeClass):
    def __init__(self):
        self.name = "board/based/Boo"
        self.methods = {
            "sayBoo-()V": self.sayBoo,
            "scareYou-(Ljava/lang/String;)V": self.scareYou,
            "addSpoopy-(I)I": self.addSpoopy,
            "makeSpoopy-(Ljava/lang/String;)Ljava/lang/String;": self.makeSpoopy
        }
    
    def sayBoo(self):
        print("Boo!")
    
    def scareYou(self, name):
        print(f"{name} is scared of Boo!")
    
    def addSpoopy(self, val):
        return val + 13
    
    def makeSpoopy(self, msg):
        return f"OoOoo! {msg} are sooo spoopy!"
        