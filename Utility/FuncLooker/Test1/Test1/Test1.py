import inspect

def Func1(obj):
    return [
            obj , 
            type(obj),
            vars(obj),
            [ d for d in dir(obj) if inspect.isclass(getattr(obj, d))] 
           ] 
if __name__ == '__main__':
    def func():
        x = 1
        y = 2
        print ('foo')
        class A:
            def method1(self):
                pass
        def f1():
            z = 3
            print ('bar')
            def f1_1():
                class class1():
                   def Joke():
                       pass
                   def Kidding():
                       pass
                a = 4
                def f1_1_1():
                    b = [1, 2, 3]
                def Nothing():
                    class Trash():
                        pass
                    return None
        def f2():
            pass
    r = Func1(func)
    print('-'*20)
    print(r)
    
    # r = Func1( getattr(func,'A') )
    r = Func1(func)
    print('-'*20)
    print(r)