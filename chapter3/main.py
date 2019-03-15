import machine
import time

BUTTON_PIN = 14  # D5
LED_PIN = 2  # D4
LED2_PIN = 16  # D0


def blink():
    led = machine.Pin(LED_PIN, machine.Pin.OUT)
    led2 = machine.Pin(LED2_PIN, machine.Pin.OUT)
    button = machine.Pin(BUTTON_PIN, machine.Pin.IN, machine.Pin.PULL_UP)
    while button.value():
        led.on()
        led2.off()
        time.sleep(0.5)
        led.off()
        led2.on()
        time.sleep(0.5)
    led.on()
    led2.on()


blink()
