if __name__ == '__main__':
    class C:
        def __init__(self):
            self._x = None

        def getx(self):
            return self._x

        def setx(self, value):
            self._x = value

        def delx(self):
            del self._x

        def Shit(self):
            x = property(self.getx, self.setx, self.delx, "I'm the 'x' property.")
            return x
        
    c = C()
    r = c.Shit
    print(r)
    print(dir(r))
    
