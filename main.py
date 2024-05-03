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

class Arduino:
    def __init__(self,pinA1,pinA2,pinA3,pinA4,pinA5,pinD1,pinD2,pinD3,pinD4,pinD5,pinVcc,pinGnd,pin5V):
        self.pinA1=pinA1
        self.pinA2=pinA2
        self.pinA3=pinA3
        self.pinA4=pinA4
        self.pinA5=pinA5
        self.pinD1=pinD1
        self.pinD2=pinD2
        self.pinD3=pinD3
        self.pinD4=pinD4
        self.pinD5=pinD5
        self.pinVcc=pinVcc
        self.pinGnd=pinGnd
        self.pin5V=pin5V

pin5V=5
pinGround=0
pinEncodeur=None
pinAlimentation=12
pinTriceps=None
pinBiceps=None

gearMotor = Motor(num_serie="2715852",pinVccEnc=pin5V,pinGndEnc=pinGround,pinAlim=pinAlimentation,pinGndalim=pinGround,pinouputAnalog=pinEncodeur)
EMG_biceps = EMG(pinVcc=pin5V,pinGnd=pinGround,pinOutputAnalog=pinBiceps)
EMG_triceps = EMG(pinVcc=pin5V,pinGnd=pinGround,pinOutputAnalog=pinTriceps)
pont_en_h = Driver(PinVcc=pin5V,PinGnd=pinGround,pinRightPWM='pin3',pinLeftPWM='pin4')
arduino214= Arduino(pinA1=pinTriceps,pinA2=pinBiceps,pinA3=pinEncodeur,pinA4="pin",pinA5="pin",pinD1="pin",pinD2="pin",pinD3="pin",pinD4="pin",pinD5="pin",pinVcc=pinAlimentation,pinGnd=pinGround,pin5V=pin5V)