"""
    ZLEGO

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    Description:
        ESP32 Driver for the L298N
    Author:
        Bengart Zakhar
"""
#

from machine import Pin, PWM
import time

class Motor():
    """
    Control of motor
    Used 2 PINs, for enable motor and speed control
    Frequency is set to 30000Hz
    Speed is controling by duty
    Working range is 500-1023
    Value of the speed is %
    """
    def __init__(self, pin_1, pin_2) :
        self.in1 = Pin(pin_1, Pin.OUT)
        self.in2 = Pin(pin_2, Pin.OUT)
        #self.speed.freq(30000)
        #self.speed.duty(0)

    def forward(self):
        self.in1.on()
        self.in2.off()

    def backward(self):
        self.in1.off()
        self.in2.on()

    def stop(self):
        self.in1.off()
        self.in2.off()

    def set_speed(self, value) :
        if value < 0 or value > 100:
            print("[-] Set correct value of speed: 0-100")
            return
        if (value == 0):
            self.stop()
        else:
            value = value * 5 + 500
            duty = self.speed.duty()
            while self.speed.duty() < value:
                duty += 100
                self.speed.duty(duty)
                time.sleep(0.1)
            self.duty(value)