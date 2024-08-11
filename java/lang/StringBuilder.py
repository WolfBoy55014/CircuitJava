from jvm.runtime.nclass import NativeClass

class StringBuilder(NativeClass):
    def __init__(self):
        self.name = "java/lang/StringBuilder"
        self.methods = {
            "<init>-()V": self.init0,
            "<init>-(Ljava/lang/String;)V": self.init1,
            "<init>-(I)V": self.init2,
            "append-(Ljava/lang/String;)Ljava/lang/StringBuilder;": self.append,
            "append-(C)Ljava/lang/StringBuilder;": self.append,
            "append-(I)Ljava/lang/StringBuilder;": self.append,
            "append-(J)Ljava/lang/StringBuilder;": self.append,
            "append-(D)Ljava/lang/StringBuilder;": self.append,
            "append-(Z)Ljava/lang/StringBuilder;": self.append,
            "append-(F)Ljava/lang/StringBuilder;": self.append,
            "delete-(II)Ljava/lang/StringBuilder;": self.delete,
            "deleteCharAt-(I)Ljava/lang/StringBuilder;": self.deleteCharAt,
            "replace-(IILjava/lang/String;)Ljava/lang/StringBuilder;": self.replace,
            "insert-(ILjava/lang/String;)Ljava/lang/StringBuilder;": self.insert,
            "insert-(IC)Ljava/lang/StringBuilder;": self.insert,
            "insert-(II)Ljava/lang/StringBuilder;": self.insert,
            "insert-(IJ)Ljava/lang/StringBuilder;": self.insert,
            "insert-(ID)Ljava/lang/StringBuilder;": self.insert,
            "insert-(IZ)Ljava/lang/StringBuilder;": self.insert,
            "insert-(IF)Ljava/lang/StringBuilder;": self.insert,
            "indexOf-(Ljava/lang/String;)I": self.index_of,
            "lastIndexOf-(Ljava/lang/String;)I": self.last_index_of,
            "reverse-()Ljava/lang/StringBuilder;": self.reverse,
            "toString-()Ljava/lang/String;": self.toString
        }
    
    def init0(self):
        self.value = ""
        
    def init1(self, value: str):
        self.value = value
    
    def init2(self, length: int):
        self.value = ""
    
    def append(self, value):
        self.value += str(value).lower()
        return self

    def delete(self, start, end):
        self.value = self.value[:start] + self.value[end:]
        return self

    def deleteCharAt(self, index):
        self.value = self.value[:index] + self.value[index + 1:]
        return self
    
    def replace(self, start, end, value: str):
        self.value = self.value[:start] + value + self.value[end:]
        return self

    def insert(self, offset, value):
        self.value = self.value[:offset] + str(value).lower() + self.value[offset:]
        return self
    
    def index_of(self, value: str):
        try:
            return self.value.index(value)
        except ValueError:
            return -1
    
    def last_index_of(self, value: str):
        try:
            return self.value.rindex(value)
        except ValueError:
            return -1

    def reverse(self):
        self.value = self.value[::-1]
        return self

    def toString(self):
        return self.value
    