import inspect
class BaseClass():
    class class1():
        def class1_func1():
            pass
        class class1_1():
            pass
    def func1():
        def func1_1():
            pass
        class func1_class1():
            pass
class DerivedClass():
    pass

class DerivedClassHandler():
    class AttrHandler():
        @staticmethod
        def Copy(derivedClass,baseClass):
            allAttrs = dir(baseClass)
            allAttrs = [ v for v in allAttrs if not ( v.startswith('__') == True and v.endswith('__') == True ) ]
            for elem in allAttrs:
                if hasattr(baseClass,elem) == True:
                    setattr(derivedClass,elem,getattr(baseClass,elem))        
            return derivedClass
    
    
if __name__ == '__main__':
    baseClass = BaseClass()
    derivedClass = DerivedClass()
    
    print(dir(baseClass))
    print(dir(derivedClass))

    afterCopiedClass = DerivedClassHandler.AttrHandler.Copy(derivedClass=derivedClass,baseClass=baseClass) 
    
    print(dir(afterCopiedClass))
    