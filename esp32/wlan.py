import network

class Wifi():
    def __init__(self):
        self.station = network.WLAN(network.STA_IF)

    def connect(self, ssid, pswd):
        if self.station.isconnected() == True:
            print("Already connected")
            return
        self.station.active(True)
        self.station.connect(ssid, pswd)
