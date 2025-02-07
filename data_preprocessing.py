import numpy as np  

def simulate_sensor_data(samples=10000):  
    time = np.linspace(0, 10, samples)  
    pressure = np.random.uniform(0, 3.5, samples)  # Simulated actuator input  
    sensor1 = 0.5 * np.sin(2 * np.pi * time) + 0.1 * pressure + np.random.normal(0, 0.1, samples)  
    sensor2 = 0.3 * np.cos(3 * np.pi * time) + 0.2 * pressure + np.random.normal(0, 0.1, samples)  
    return np.column_stack([sensor1, sensor2, pressure])  
