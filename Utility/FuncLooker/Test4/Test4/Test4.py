import types
import inspect
class TestClass:
    
    def Hello():
        @classmethod
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
class DerivedClass(TestClass):
    pass
def get_class_that_defined_method(meth):
    # for cls in inspect.getmro(meth.im_class):
    for cls in meth.__self__:
        if meth.__name__ in cls.__dict__: 
            return cls
    return None

if __name__ == '__main__':
    testClass = TestClass()
    hello = testClass.Hello
    
    members= inspect.getmembers(hello)
    print("members:")
    for elem in members :
        print(elem)
        
    members= inspect.getmembers(hello.__func__)
    print("members:")
    for elem in members :
        print(elem)
    
    dirs = dir(hello.__func__)
    print("dirs:")
    for elem in members :
        print(elem)
    
    
