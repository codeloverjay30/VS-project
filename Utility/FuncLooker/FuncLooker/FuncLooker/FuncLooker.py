import dis
import types
class FuncLooker():
    @staticmethod
    def GetNestedFuncs(f):
        ins = dis.get_instructions(f)
        for x in ins:
            try:
                if x.opcode == 100 and '<locals>' in next(ins).argval \
                                              and next(ins).opcode == 132:
                    yield next(ins).argrepr
                    yield from FuncLooker.GetNestedFuncs(x.argval)
            except Exception:
                pass
                # raise Exception("ERROR!!! There are exception during trying to find all nested funcs.")   

if __name__ == '__main__' :
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
    r = list(FuncLooker.GetNestedFuncs(func))
    print(r)
    