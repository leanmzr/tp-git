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



class Sensor:
    def __init__(self,pinVcc,pinGnd,pinOutputAnalog):
        self.pinVcc=pinVcc
        self.pinGnd=pinGnd
        self.pinOutputAnalog=pinOutputAnalog

class EMG(Sensor):
    def __init__(self,pinVcc,pinGnd,pinOutputAnalog):
        super().__init__(self,pinVcc,pinGnd,pinOutputAnalog)
        self.valeur_de_contraction=None
        self.freq_echantillonage = 100

    def read_contraction(self):
        read_val = None #une val
        print(f"j'envoi a {self.valeur_de_contraction} ce que j'ai lu selon ma freq d'echantillonage {self.freq_echantillonage}")
        self.valeur_de_contraction = read_val
        self.send_read_val(read_val)

    def send_read_val(self,read_val):
        print(f"j'envoi a {self.pinOutputAnalog} ce que j'ai lu ")

class Driver:
    def __init__(self,PinVcc,PinGnd,pinRightPWM,pinLeftPWM):
        self.PinVcc=PinVcc
        self.PinGnd=PinGnd
        self.pinRightPWM=pinRightPWM
        self.pinLeftPWM=pinLeftPWM

    def commande(self):
        print("je commande le moteur")

