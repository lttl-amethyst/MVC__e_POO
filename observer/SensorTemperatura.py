class SensorTemperatura:
    def __init__(self):
        self.observers = []
        self.temperatura =  0

    def add_observer(self, observer):
        self.observers.app.append(observer)

    def remover_observer(self, observer):
        self.observers.remove(observer)

    def notificcar(self):
        for observer in self.observers:
            self.observer.atualizar(self.temperatura)

    def definir_temperatura(self, temp):
        print(f"Atemperatura mudou para {temp}")
        self.temperatura = temp
        self.notificar()

#observers:
class Smartwatch:
    def atualizar(self, temp):
        print(f"Smartwatch: mostrando {temp}°C")
class SmartPhone:
    def atualizar(self, temp):
        print(f"Celular recebeu notificação {temp}°C")
class Alarm:
    def atualizar(self, temp):
        if temp >= 30:
            print("Alerta de alta temperatura")

#criar os observers
relogio = Smartwatch()
celular = SmartPhone()
alarme = Alarm()

#registrar os subscribers no publisher
sensor = SensorTemperatura()
sensor.add_observer(relogio)
sensor.add_observer(celular)
sensor.add_observer(alarme)

#mudar a temperatura para notificar automaticamente os sobscribers
sensor.definir_temperatura(25)
sensor.definir_temperatura(32)