"""
    ZLEGO

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
        Main module for ZLEGO
        Controlig all processes in the city
    Author:
        Bengart Zakhar
"""

from drivers.l298n import Motor
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

if __name__ == "__main__":
    switch = RailwaySwitch(26, 27)
    while True:
        switch.run_cycle(10)
     