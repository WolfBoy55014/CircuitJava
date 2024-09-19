from jvm.runtime.jclass import Method, JString
from jvm.runtime.jobject import JRef, JObject
from jvm.base.utils.print_utils import printb, printo

class NativeClassLoader(object):
    default_loader = None
    native_classes = ["board/based/Boo", "java/lang/StringBuilder", "board/Pin", "board/ADC", "board/DAC"]
    
    def __init__(self):
        self.loaded_classes = {}
    
    @staticmethod
    def default_class_loader():
        if NativeClassLoader.default_loader is None:
            NativeClassLoader.default_loader = NativeClassLoader()
        return NativeClassLoader.default_loader

    def load_class(self, class_name):
        if class_name in self.loaded_classes.keys():
            return self.loaded_classes[class_name]()
        else:
            printb([class_name.split('/')[-1]])
            module = __import__(class_name)
            nclass = getattr(module, class_name.split('/')[-1])
            self.loaded_classes[class_name] = nclass
            return nclass()
            
            # raise Exception(f'TODO in nclass.py #3. Native class {class_name}')
        

class NativeClass():
    def __init__(self):
        self.type = JObject.TYPE_NOBJ
        self.name = None
        self.methods = {}
        self.fields = {}
        
    @staticmethod
    def get_arg_desc(descs):
        return Method.get_arg_desc(descs)
    
    @staticmethod
    def get_args(n_frame, args_desc):
        args = []
        i = len(args_desc)
        for arg in args_desc:
            if arg == 'I' or arg == 'S' or arg == 'Z' or arg == 'C' or arg == 'B':
                value = n_frame.operand_stack.pop_int()
                args.append(value)
            elif arg == 'J':
                value = n_frame.operand_stack.pop_long()
                args.append(value)
            elif arg == 'F':
                value = n_frame.operand_stack.pop_float()
                args.append(value)
            elif arg == 'D':
                value = n_frame.operand_stack.pop_double()
                args.append(value)
            elif arg[0] == 'L':
                jref = n_frame.operand_stack.pop_ref()
                args.append(jref.data)
            elif arg == '[':
                jref = n_frame.operand_stack.pop_ref()
                raise Exception('TODO in nclass.py #2')
            i -= 1
        return args
    
    def get_method_name_desc(self, name, desc):
        try:
            return self.methods[f'{name}-{desc}']
        except:
            raise Exception(f'Native method {name}-{desc} not found')

    def invoke_method(self, n_frame, name, desc):
        args_desc = NativeClass.get_arg_desc(desc)
        args = NativeClass.get_args(n_frame, args_desc)
        method = self.get_method_name_desc(name, desc)
        n_frame.operand_stack.pop()
        result = method(*args)
        if result is not None:
            # Because we never made a new frame at invocation, we can still use `n_frame`
            r_type = desc.split(')')[-1]
            if r_type == 'I' or r_type == 'S' or r_type == 'Z' or r_type == 'C' or r_type == 'B':
                n_frame.operand_stack.push_int(result)
            elif r_type == 'J':
                n_frame.operand_stack.push_long(result)
            elif r_type == 'F':
                n_frame.operand_stack.push_float(result)
            elif r_type == 'D':
                n_frame.operand_stack.push_double(result)
            elif r_type == "Ljava/lang/String;":
                jstring = JString()
                jstring.data = str(result)
                n_frame.operand_stack.push_ref(jstring)
            elif r_type[0] == 'L' and r_type[1:-1] in NativeClassLoader.native_classes:
                ref = JRef.new_native_object(self)
                n_frame.operand_stack.push_ref(ref)
            elif r_type[0] == 'L':
                raise Exception('TODO in nclass.py #1, returning object')
            else:
                raise Exception(f'Native method {name}-{desc} returned unexpected type {r_type}')
        return
        
    