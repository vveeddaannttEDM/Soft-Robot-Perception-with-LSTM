import csv  
from datetime import datetime  

with open('sensor_data.csv', 'w', newline='') as f:  
    writer = csv.writer(f)  
    writer.writerow(["Timestamp", "Sensor1", "Sensor2", "Sensor3"])  
    while True:  
        timestamp = datetime.now().isoformat()  
        data = [timestamp, read_sensor(0), read_sensor(1), read_sensor(2)]  
        writer.writerow(data)  
        time.sleep(0.1)  
