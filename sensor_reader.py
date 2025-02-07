import spidev  
import time  
import numpy as np  

# MCP3008 ADC setup  
spi = spidev.SpiDev()  
spi.open(0, 0)  # CE0 pin  
spi.max_speed_hz = 1350000  

def read_sensor(channel):  
    adc = spi.xfer2([1, (8 + channel) << 4, 0])  
    return ((adc[1] & 3) << 8) + adc[2]  

# Simulate 3 cPDMS sensors (channels 0-2)  
while True:  
    sensor1 = read_sensor(0)  # Resistance ≈ 500-1000Ω  
    sensor2 = read_sensor(1)  
    sensor3 = read_sensor(2)  
    print(f"S1: {sensor1}, S2: {sensor2}, S3: {sensor3}")  
    time.sleep(0.1)  # 10 Hz sampling  
