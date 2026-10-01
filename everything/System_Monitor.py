# Das ist ein System Monitor
# Mein Python-Projekt zeigt live CPU, RAM, Festplatte, Netzwerk
# Braucht pip install psutil

import os
import time
import psutil
from datetime import datetime


def balken(prozent):
    """Prozentzahl(%) = Balken mit 10 Kästchen(# = 10%/- = leer)"""
    voll = int(prozent / 10)  # 1 Kästchen = 10 %
    leer = 10 - voll
    return f"[{'#' * voll}{'-' * leer}] {prozent}%"


def in_gb(bytes_wert):
    """Bytes in Gigabyte Umrechnung """
    return round(bytes_wert / 1024 ** 3, 1)


def top_prozesse(anzahl):
    """Prozesse mit dem höchsten Ram-Verbrauch"""
    liste = []
    for prozess in psutil.process_iter(["name", "memory_percent"]):
        info = prozess.info  # info ist ein Dictionary
        if info["name"] is None or info["memory_percent"] is None:
            continue  # keine Zugriffsrechte = überspringen
        liste.append(info)
    liste.sort(key=lambda p: p["memory_percent"], reverse=True)
    return liste[:anzahl]


# Windows Hauptfestplatte = C:\, sonst /
if os.name == "nt":
    laufwerk = "C:\\"
    clear_befehl = "cls"
else:
    laufwerk = "/"
    clear_befehl = "clear"

print("Monitor startet... (beenden = Strg+C)")

try:
    while True:
        #Anmerkung: CPU Messung dauert 1 Sekunde
        cpu = psutil.cpu_percent(interval=1)
        ram = psutil.virtual_memory()
        platte = psutil.disk_usage(laufwerk)
        netz = psutil.net_io_counters()

        
        sekunden = time.time() - psutil.boot_time()
        stunden = int(sekunden // 3600)
        minuten = int(sekunden % 3600 // 60)

    
        os.system(clear_befehl)
        print("SYSTEM MONITOR")
        print("Uhrzeit:     ", datetime.now().strftime("%H:%M:%S"))
        print("Laufzeit:    ", stunden, "Std", minuten, "Min")
        print()
        print("CPU:         ", balken(cpu), f"({psutil.cpu_count()} Kerne)")
        print("RAM:         ", balken(ram.percent),
              f"({in_gb(ram.used)} von {in_gb(ram.total)} GB)")
        print("Festplatte:  ", balken(platte.percent),
              f"({in_gb(platte.used)} von {in_gb(platte.total)} GB)")

        # Akku nur bei Laptops
        akku = psutil.sensors_battery()
        if akku is not None:
            print("Akku:        ", balken(round(akku.percent)))

        print()
        print("Netzwerk:")
        print("  empfangen:", round(netz.bytes_recv / 1024 ** 2), "MB")
        print("  gesendet: ", round(netz.bytes_sent / 1024 ** 2), "MB")

        print()
        print("RAM lastige Prozesse:")
        for p in top_prozesse(3):
            print(f"  {p['name'][:22]:<24} {round(p['memory_percent'], 1)}%")

except KeyboardInterrupt:
    print("\nMonitor beendet")