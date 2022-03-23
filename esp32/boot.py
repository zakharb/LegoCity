# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)

import wlan
interface = wlan.Wifi()
interface.connect('lego_city', 'ushIk418~')
