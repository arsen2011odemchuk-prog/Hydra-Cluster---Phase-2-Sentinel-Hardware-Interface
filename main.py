This firmware implements a Dual-Bus SPI isolation strategy to prevent hardware race conditions between authentication slots. The logic follows the "Dead-Man-Switch" protocol: if either physical key is removed from the Sentinel chassis, the Pico immediately broadcasts a TERMINATE signal via the Serial Bridge to the Master Node, forcing an instant lock of the GPU Cluster. All data is transmitted in JSON format for seamless integration with the Phase 2 Telemetry HUD.



import machine
import utime
import ujson
from mfrc522 import MFRC522

class SentinelInterface:
    def __init__(self):
        # 1. Инициализация Зуммера
        self.buzzer = machine.Pin(15, machine.Pin.OUT)
        
        # 2. Инициализация SPI0 (Левый RFID)
        self.reader_l = MFRC522(spi_id=0, sck=18, miso=16, mosi=19, cs=17, rst=20)
        
        # 3. Инициализация SPI1 (Правый RFID)
        self.reader_r = MFRC522(spi_id=1, sck=10, miso=8, mosi=11, cs=13, rst=9)
        
        # Белый список (UID карт) — замени на свои после первого теста
        self.whitelist = ["0xABC123", "0xXYZ789"] 
        self.is_authorized = False

    def beep(self, duration=0.1):
        """Звуковой сигнал подтверждения."""
        self.buzzer.value(1)
        utime.sleep(duration)
        self.buzzer.value(0)

    def get_uid(self, reader):
        """Чтение UID с конкретного модуля."""
        (stat, tag_type) = reader.request(reader.REQIDL)
        if stat == reader.OK:
            (stat, uid) = reader.SelectTagSN()
            if stat == reader.OK:
                return "0x" + "".join(["%02X" % i for i in uid])
        return None

    def send_status(self, status, key_a=None, key_b=None):
        """Отправка JSON пакета в Serial порт (Master Node)."""
        data = {
            "system": "SENTINEL_PHASE_2",
            "status": status,
            "key_alpha": key_a,
            "key_beta": key_b,
            "timestamp": utime.ticks_ms()
        }
        print(ujson.dumps(data))

    def run(self):
        print("Sentinel Phase 2: System Online")
        self.beep(0.3)
        
        while True:
            uid_l = self.get_uid(self.reader_l)
            uid_r = self.get_uid(self.reader_r)

            # Логика "Two-Man Rule"
            if uid_l and uid_r:
                if not self.is_authorized:
                    self.is_authorized = True
                    self.beep(0.1)
                    utime.sleep(0.1)
                    self.beep(0.1)
                    self.send_status("AUTHORIZED", uid_l, uid_r)
            else:
                if self.is_authorized:
                    self.is_authorized = False
                    self.send_status("TERMINATED")
            
            utime.sleep(0.5) # Частота опроса (Hz)

# Запуск системы
if __name__ == "__main__":
    try:
        sentinel = SentinelInterface()
        sentinel.run()
    except Exception as e:
        print(f"Critical System Failure: {e}")
