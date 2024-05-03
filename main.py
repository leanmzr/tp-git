class Motor:
    def __init__(self,num_serie,pinVccEnc,pinGndEnc,pinAlim,pinGndalim,pinouputAnalog):
        self.num_serie=num_serie
        self.pinVccEnc=pinVccEnc
        self.pinGndEnc=pinGndEnc
        self.pinAlim=pinAlim
        self.pinGndalim=pinGndalim
        self.pinouputAnalog=pinouputAnalog
        self.pos=None
    
    def position (self):
        print(f"j'envoi a {self.ouputAnalog} ma position : {self.pos}")

    def TurnRight (self):
        print(f"tourne a droite selon les signaux")

    def TurnLeft (self):
        print(f"tourne a gauche selon les signaux")