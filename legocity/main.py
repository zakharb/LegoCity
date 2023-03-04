"""
    LEGOCITY

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

    Description:
        Main module for LEGOCITY
        Controlig all processes in the city
    Author:
        Bengart Zakhar
"""

from drivers.l298n import Motor
from drivers.hcsr04 import HCSR04
import time

class RailwaySwitch():
    """
    Auto change railway switch
    Need to set intervals
    """
    def __init__(self, pin_1, pin_2):
        self.motor = Motor(pin_1, pin_2)

    def run_cycle(self, interval):
        self.motor.forward()
        time.sleep(0.3)
        self.motor.stop()
        time.sleep(interval)
        self.motor.backward()
        time.sleep(0.3)
        self.motor.stop()
        time.sleep(interval)


class Train():
    """
    Train control
    """
    def __init__(self, pin_1, pin_2, sensor):
        self.motor = Motor(pin_1, pin_2)
        self.running = False
        self.sensor = sensor

    def start(self):
        self.motor.forward()
        self.running = True

    def stop(self):
        self.motor.stop()
        self.running = False

    def is_running(self):
        return self.running
    
    def run(self):
    while True:
        distance = self.sensor.distance_cm()
        #print('Distance:', distance, 'cm')
        if distance < 5 and distance > 0:
            if self.is_running() == True:
                self.stop()
        else:
            if self.is_running() == False:
                self.start()
        time.sleep(0.5)

class Car():
    """
    Car control
    """
    def __init__(self, pin_1, pin_2):
        self.motor = Motor(pin_1, pin_2)
        self.running = False

    def run(self):
        self.motor.forward()
        self.running = True

    def stop(self):
        self.motor.stop()
        self.running = False

    def is_running(self):
        return self.running
    
    def run(self):
    while True:
        #distance = self.sensor.distance_cm()
        #print('Distance:', distance, 'cm')
        direction:
        if self.is_running() == True:
            self.stop()
        else:
            self.start()
        time.sleep(3)

if __name__ == "__main__":
    #train = Train(26, 27)
    car = Car(26, 14)
    try:
        car.run()
    except Exception as e:
        print(e)

    #sensor = HCSR04(trigger_pin=5, echo_pin=18, echo_timeout_us=10000)  


