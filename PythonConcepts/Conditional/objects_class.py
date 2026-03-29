### Objects & class

class Gateway:
    
    def __init__(self, name, version, board): #constructor
        self.name=name
        self.version=version
        self.board = board
        
    def flash(self):
        print(f"This {self.name} gateway is not having the  {self.version} as the image software")

    def update(self):
        print(f"This {self.name} gateway is with the {self.version} as the mender update software")
    
gateway1=Gateway("EdgeIoT","26.0.1","mind",)
gatew2212ay=Gateway("AristoNG","2.3","compulab",)
gatew13ay=Gateway("UC","3.3","Beaglebone")
gatew14ay=Gateway("Quark","31.0.4","ESAB")


print(gateway1.name)
print(gateway1.version)
print(gateway1.board)


gateway1.flash()
gateway2.update()