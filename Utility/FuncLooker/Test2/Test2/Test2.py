import inspect
import dis
import types
import sys  

def LocalClass(obj):
    return locals()
class TestClass:
    @classmethod
    def Hello():
        def HelloWorld():
            print("HelloWorld!!!")
        print("Hello!!!")
    def Sound(self):
        def Speak():
            print("Speak!!!")
        class Animal:
            class Dog:
                def Bark():
                    print("Bark!!!")
            class Cat:
                def Mow():
                    print("Mow!!!")
        
        def Tune():
            print("Tune!!!")                    
        
    class a:
        @classmethod
        def a1_func1():
            print("a1_func1!!!")
        class a1_1:
            @classmethod
            def a1_1_func1():
                print("a1_1_func1!!!")
            @classmethod
            @staticmethod
            def a1_1_func2():
                print("a1_1_func2!!!")
if __name__ == '__main__':
    
    testClass = TestClass()
    
    val = testClass.Sound
    
    instructions = list(dis.get_instructions(val))

    result = list()
    a1 = list()    
    
    print(instructions)
    
    
    for elem in instructions :
        a1.append(elem.opname)
        if elem.opname != None and (elem.opname == 'STORE_FAST' or elem.opname == 'LOAD_CONST'):
            result.append( [ elem.opname ,elem.argval] )
    for elem in result:
        if elem[0] == 'LOAD_CONST':
            v = elem[1]
            print('!'*20)
            print(v)
            print(type(v))
            print(dir(v))

            if isinstance(v,types.CodeType) == True:
                print('@'*20)
                members = inspect.getmembers(v)
                print(members)
                for me in members:
                    print(me)
                print('@'*20)
            print('!'*20)

                 