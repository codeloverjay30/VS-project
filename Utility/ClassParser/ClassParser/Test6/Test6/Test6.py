#!/usr/bin/python
def getfunc():
    from inspect import currentframe, getframeinfo
    caller = currentframe().f_back
    func_name = getframeinfo(caller)[2]
    caller = caller.f_back
    from pprint import pprint
    func = caller.f_locals.get(
            func_name, caller.f_globals.get(
                func_name
        )
    )
    return func

def main():
    def inner1():
        def inner2():
            print("Current function is %s" % getfunc())
        print("Current function is %s" % getfunc())
        inner2()
    print("Current function is %s" % getfunc())
    inner1()                
if __name__ == '__main__':
    main()
