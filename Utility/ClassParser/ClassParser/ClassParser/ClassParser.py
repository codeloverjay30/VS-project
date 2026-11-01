import __future__
from audioop import reverse 

import inspect
from enum import Enum
import inspect
from enum import Enum
from pyclbr import Class
from pydoc import classname
from re import L
import stat
import sys

                
class DefinedMemberModeEnum(Enum):
    OWNDEFINED_MEMBER = 1 ** 2 - 1
    BUILTIN_MEMBER = 2 ** 2 - 1
    ALL_MEMBER = 3 ** 2 - 1
class MemberTypeModeEnum(Enum) :
    FUNC = 1 ** 2 - 1
    CLASS = 2 ** 2 - 1
    ALL_MEMBER = 3 ** 2 - 1
class RecursiveModeEnum(Enum):
    VISIT_DEPTH_1  = 1 ** 2 - 1
    NONRECURSIVE_ALL = 2 ** 2 - 1
class StaticModeEnum(Enum):
    STATIC = 1 ** 2 - 1
    NONSTATIC = 2 ** 2 - 1

class ListHandler:
    @staticmethod
    def IsEmpty(
        list1 : list
    ) -> bool :
        return list1 == None or len(list1) <= 0 
    @staticmethod
    def HasExactly2ElemsInTuple(
            list1 : list
    ) -> bool :
        if ListHandler.IsEmpty(list1) == True:
            return False
        eachElem = [ True if ( isinstance(x,tuple) == True and len(x) == 2 ) else False for x in list1 ]
        result = all(eachElem)
        return result
        
class StringHandler:
    @staticmethod
    def StartEnd(
        target : str  ,
        contains : str , 
        repetition : int
    ) -> bool :
        if repetition < 0:
            raise Exception("ERROR!!! The arg repetition should be a positive integer.")
        if repetition == 0:
            return True
        return target.startswith(contains*repetition) and target.endswith(contains*repetition)
    
class ClassFuncFinder:    
    """
    @staticmethod
    def GetTopClass(
            className ,
            availables
    ):
      dicts = availables
      if not className in dicts :
          raise Exception("Error!!! The val with specified className does NOT exists in availables!")
      return dicts[className]
    """    
    """
    @staticmethod
    def GetMembers(
                class1 : list,
                availables , 
                searchMode : ClassModeEnum , 
                staticMode : StaticModeEnum = StaticModeEnum.NONSTATIC 
    ):
        match staticMode :
            case StaticModeEnum.NONSTATIC :
                nestedClass = inspect.getmembers(class1[0][1])
            case StaticModeEnum.STATIC :
                nestedClass = inspect.getmembers_static(class1[0][1])
            case _ :
                raise Exception("ERROR!!! Invalid val of arg staticMode which should be one of value defined in StaticModeEnum!")
            
        nestedClassPair = list()
        match searchMode:
            case ClassModeEnum.OWNDEFINED_MEMBER:
                nestedClassPair = [ (k,v) for (k,v) in nestedClass if ( StringHandler.StartEnd(target = k , contains = '_', repetition = 2) == False )]
            case ClassModeEnum.BUILTIN__MEMBER:
                nestedClassPair = [ (k,v) for (k,v) in nestedClass if ( StringHandler.StartEnd(target = k , contains = '_', repetition = 2) == True )]
            case ClassModeEnum.ALL_MEMBER:
                nestedClassPair = [ (k,v) for (k,v) in nestedClass]
            case _:
                raise Exception("ERROR!!! Invalid value of arg searchMode.")
        if ListHandler.IsEmpty(nestedClassPair) == True:
            raise Exception("ERROR!!! Invalid value of nestedClassPair. It can not be empty.")
        return nestedClassPair
    """
    """
    @staticmethod
    def GetChild(
            childPair ,
            funcName , 
            availables , 
            searchMode : ClassModeEnum
    ):
        if funcName == None:
            return childPair      
        if ListHandler.HasExactly2ElemsInTuple(childPair) == False:
            raise Exception("Error!!! The attr with specified childPair either is NOT a tuple, or is a tuple but at least one elem of them does NOT have exactly 2 elems.")          
        child = [k for (k,v) in childPair]
        if not funcName in child:
            raise Exception("Error!!! The attr with specified string does NOT exists in the class!")
        targetClass = [ (k,v) for (k,v) in childPair if ( k == funcName )]
        return targetClass
    """
    
    @staticmethod
    def GetMember(
                    src,
                    memberName : str
    ):
        if hasattr(src,memberName) == False:
            raise Exception("ERROR!!! The class src:"+src.__name__+" has no attribute called:"+memberName+"!")
        r = getattr(src,memberName)
        return [r.__name__,r]
    
    @staticmethod
    def GetMembers(
                    src , 
                    definedMemberModeEnum : DefinedMemberModeEnum , 
                    memberTypeModeEnum : MemberTypeModeEnum
    ):
        members = list()
        if inspect.isclass(src) == True:
            members = inspect.getmembers(src)
        elif inspect.isfunction(src) == True:
            members = list(dir(src))
            members = [ (elem , elem ) for elem in members]
            
        match definedMemberModeEnum : 
            case definedMemberModeEnum.OWNDEFINED_MEMBER :
                 result = [ (k,v) for (k,v) in members if 
                           inspect.isbuiltin(v) == False and 
                           StringHandler.StartEnd(target = k,contains = '_', repetition = 2) == False
                 ]
            case definedMemberModeEnum.BUILTIN_MEMBER :
                 result = [ (k,v) for (k,v) in members if inspect.isbuiltin(v) == True]
            case definedMemberModeEnum.ALL_MEMBER :
                 result = members            
            case _ :
                raise Exception("ERROR!!! Invalid value of arg named: definedMemberModeEnum!")
        match memberTypeModeEnum : 
            case MemberTypeModeEnum.FUNC :
                result = [ (k,v) for (k,v) in result if inspect.ismethod(v) == True or inspect.isfunction(v) == True]
            case MemberTypeModeEnum.CLASS :
                 result = [ (k,v) for (k,v) in result if inspect.isclass(v) == True]
            case MemberTypeModeEnum.ALL_MEMBER :
                 result = result            
            case _ :
                raise Exception("ERROR!!! Invalid value of arg named: memberTypeModeEnum!")      
        return result
   
    @staticmethod
    def GetNestedMembers(
                            src ,
                            definedMemberModeEnum : DefinedMemberModeEnum , 
                            memberTypeModeEnum : MemberTypeModeEnum   
     ):
        stack1 = [ [ src.__name__, src ] ]
        result = list()
        while True:
            if ListHandler.IsEmpty(stack1) == True:
                break           
            lastMemberPair = stack1[-1]
            stack1.pop()
            if ListHandler.IsEmpty(lastMemberPair) == True:
                 continue
            if inspect.isfunction(lastMemberPair[1]) == True or \
            inspect.ismethod(lastMemberPair[1]) == True or \
            inspect.isclass(lastMemberPair[1]) == True :
                members = ClassFuncFinder.GetMembers(
                                                        src = lastMemberPair[1] ,
                                                        definedMemberModeEnum = definedMemberModeEnum , 
                                                        memberTypeModeEnum = memberTypeModeEnum   
                                                     )
                print(members)
                if ListHandler.IsEmpty(members) == False:
                    l = list()
                    idx = 0
                    cnt = idx
                    # Access and change the value of last elem in last elem in resultant list.
                    for subelem in members:    
                        stack1.insert(cnt,subelem)
                        l.insert(cnt,subelem)
                        cnt += 1
                    result.insert(-1,l)          
        result.reverse()
        return result
    
class TestClass:
    def Hello():
        def HelloWorld():
            print("HelloWorld!!!")
        print("Hello!!!")
    def Sound():
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
        print("Sound!!!")
    class a:
        def a1_func1():
            print("a1_func1!!!")
        class a1_1:
            def a1_1_func1():
                print("a1_1_func1!!!")
            @staticmethod
            def a1_1_func2():
                print("a1_1_func2!!!")

def GetInfo(obj):
    def Get():
        return "Get"
    return [obj,type(obj)]
if __name__ == '__main__':
    r = ClassFuncFinder.GetNestedMembers(
                                        src =  TestClass ,
                                        definedMemberModeEnum= DefinedMemberModeEnum.OWNDEFINED_MEMBER,
                                        memberTypeModeEnum = MemberTypeModeEnum.ALL_MEMBER
                                   )
    print("result:")
    print(r)