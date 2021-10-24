from network import WLAN
import config
import time

class WLANClient:

    def __init__(self):
        self.wlan = WLAN(mode=WLAN.STA)

    def connect(self):
        self.wlan.connect(config.WIFI_SSID, auth=(None, config.WIFI_PASS), timeout=5000)
        while not self.wlan.isconnected():
            time.sleep(0.5)
        print('WLAN connection succeeded!')
