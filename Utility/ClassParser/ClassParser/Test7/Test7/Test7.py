import types
import inspect
import sys

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
     
def is_mod_function(mod, func):
    return True 
        # inspect.isfunction(func) 
        # and inspect.getmodule(func) == mod

def list_functions(mod):
    print(mod)
    print(mod.__dict__)
    return [func.__name__ for func in mod.__dict__.values()
            if is_mod_function(mod, func)]

if __name__ == '__main__':
    testClass = TestClass()
    sound = TestClass.Sound 
    
    """
    print(testClass)
    print(type(testClass))
    
    iscallable = callable(testClass)
    
    print(iscallable)
    print(type(iscallable))
    
    print(sound)
    print(type(sound))
    
    iscallable = callable(sound)
    
    print(iscallable)
    print(type(iscallable))
    
    sound1 = dir(sound)
    
    print(sound1)
    print(type(sound1))
    
    frame = sys._getframe()
    
    print(frame)
    print(type(frame))
    
    frameInfo = inspect.getframeinfo(frame)
    
    print(frameInfo)
    print(type(frameInfo))
    """
    
    r = list_functions(sys.modules[__name__])
    print(r)
    