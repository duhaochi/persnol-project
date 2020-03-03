import random

class Pin:
    pin = "0404"

    @classmethod
    def checkPin(cls, pin):
        return cls.pin == pin

    @classmethod
    def creatRandomPin(cls):
        cls.pin = str(random.random()*1000)

    @classmethod
    def setPin(cls,pin):
        cls.pin = pin