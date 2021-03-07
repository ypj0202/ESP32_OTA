from main.ota_updater import OTAUpdater
import machine


def download_and_install_update_if_available():
    o = OTAUpdater('https://github.com/ypj0202/ESP32_OTA')
    o.install_update_if_available_after_boot('wifi-ssid', 'wifi-password')


def start():
    led0 = machine.Pin(12, machine.Pin.OUT)
    while True:
        led0.value(1)


def boot():
    download_and_install_update_if_available()
    start()


boot()
