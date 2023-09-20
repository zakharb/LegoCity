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
import random

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
    def __init__(self, 
                 motor_1 = None, 
                 motor_2 = None, 
                 wheel_1 = None, 
                 wheel_2 = None,
                 sensor=None):
        self.motor = Motor(motor_1, motor_2)
        self.wheel = Motor(wheel_1, wheel_2)
        self.sensor = sensor
        self.is_backward = False
        self.is_forward = False

    def forward(self):
        if not self.is_forward:
            self.motor.forward()
            self.is_forward = True
            self.is_backward = False

    def backward(self):
        if not self.is_backward:
            self.motor.backward()
            self.is_forward = False
            self.is_backward = True

    def stop(self):
        self.motor.stop()
        self.is_backward = False
        self.is_forward = False

    def turn_left(self, turn_time=0.5):
        self.wheel.turn_left(turn_time)

    def turn_right(self, turn_time=0.5):
        self.wheel.turn_right(turn_time)

    def is_running(self):
        return self.running
    
    def run(self):
        time_now = time.time()
        while True:
            print('Distance:', self.sensor.distance_cm(), 'cm')
            self.forward()
            print(time_now)
            if time.time() - time_now > 10:
                time_now = time.time()
                if int(time_now) % 2 == 0:
                    self.turn_left(turn_time=0.5)
                    self.turn_right(turn_time=0.5)
                else:
                    self.turn_right(turn_time=0.5)
                    self.turn_left(turn_time=0.5)
                if int(time_now) % 8 == 0:
                    self.stop()
                    self.backward()
                    time.sleep(3)
                    self.stop()
            distance = self.sensor.distance_cm()
            if distance > 0 and distance < 10:
                self.stop()
                if distance % 2 == 0:
                    self.turn_left(turn_time=2)
                    self.backward()
                    self.turn_right(turn_time=1.1)
                else:
                    self.turn_right(turn_time=2)
                    self.backward()
                    self.turn_left(turn_time=1.1)
                time.sleep(2)
                self.stop()
            time.sleep(0.2)

if __name__ == "__main__":
    #train = Train(26, 27)
    sensor = HCSR04(trigger_pin=33, echo_pin=26)  
    car = Car(motor_1=4, motor_2=16, wheel_1=17, wheel_2=5, sensor=sensor)
    try:
        car.run()
    except Exception as e:
        print(e)
        raise(e)

    #sensor = HCSR04(trigger_pin=5, echo_pin=18, echo_timeout_us=10000)  


