![logo](logo.png)

## _Build LEGO City with ESP32_ 

![](https://img.shields.io/badge/version-1.0-blue)
![](https://img.shields.io/badge/python-3.9-blue)

## Content  
[Firmware](#Firmware)  
[Network](#Network)  
[PWM](#PWM)  

<a name="info"/>

## Info
</a>  

> Use Micropython and ESP32 to build your own city

<a name="Firmware"/>

## Firmware
</a>  

```sh
python3 -m esptool --port /dev/ttyUSB0 erase_flash
python3 -m esptool --chip esp32 --port /dev/ttyUSB0 write_flash -z 0x1000 esp32-20220117-v1.18.bin
export AMPY_PORT=/dev/ttyUSB0 
```


## Network
</a>  

```sh
import network
wlan = network.WLAN(network.STA_IF)
wlan.isconnected()
wlan.active(True)
wlan.ifconfig()
wlan.scan()
wlan.connect('lego_city', '')
```


## PWM
</a>  

```sh
pwm0 = PWM(Pin(0))
pwm0.freq(1000)
pwm0.duty(256)

freq 30000
duty 500+
```