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
        self.pwm1 = PWM(self.in1)
        self.pwm2 = PWM(self.in2)
        #self.speed.freq(20000)
        #self.speed.duty(500)

    def turn_left(self, turn_time):
        self.pwm2.duty(0)
        self.pwm1.duty(950)
        time.sleep(turn_time)
        self.pwm1.duty(0)

    def turn_right(self, turn_time):
        self.pwm1.duty(0)
        self.pwm2.duty(950)
        time.sleep(turn_time)
        self.pwm2.duty(0)

    def forward(self):
        self.pwm1.duty(750)
        time.sleep(1)
        self.pwm1.duty(800)
        time.sleep(1)
        self.pwm1.duty(850)
        self.pwm2.duty(0)

    def backward(self):
        self.pwm1.duty(0)
        self.pwm2.duty(750)
        time.sleep(1)
        self.pwm2.duty(800)
        time.sleep(1)
        self.pwm2.duty(850)

    def stop(self):
        self.pwm1.duty(800)
        self.pwm2.duty(800)
        time.sleep(0.1)
        self.pwm1.duty(750)
        self.pwm2.duty(750)
        time.sleep(0.1)
        self.pwm1.duty(700)
        self.pwm2.duty(700)
        time.sleep(0.1)
        self.pwm1.duty(0)
        self.pwm2.duty(0)

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