import types
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
    sound = testClass.Sound
    
    result = list()
    print('sound.__code__:')
    print(sound.__code__)
    for obj in sound.__code__.co_consts:
        if isinstance(obj, types.CodeType):
            result.append([
                obj,
                type(obj),
                obj.co_consts
            ])
            exec(obj)
    print(result)
    