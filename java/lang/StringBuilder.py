instances = {}
methods = {}

methods["()V"] = "init0"
methods["(Ljava/lang/String;)V"] = "init1"
methods["(I)V"] = "init2"
methods["(Ljava/lang/String;)Ljava/lang/StringBuilder;"] = "append"
methods["(C)Ljava/lang/StringBuilder;"] = "append"
methods["(I)Ljava/lang/StringBuilder;"] = "append"
methods["(J)Ljava/lang/StringBuilder;"] = "append"
methods["(D)Ljava/lang/StringBuilder;"] = "append"
methods["(Z)Ljava/lang/StringBuilder;"] = "append"
methods["(F)Ljava/lang/StringBuilder;"] = "append"

def new(index):
    instances[index] = StringBuilder()

def get_method_by_desc(desc):
    return getattr(instances[desc[0]], desc[1])


class StringBuilder:
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
    