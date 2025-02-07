def preprocess(data):  
    return (data - np.mean(data)) / np.std(data)  

# Predict kinematics (e.g., tip position)  
sensor_data = preprocess([sensor1, sensor2, sensor3])  
input_tensor = tf.convert_to_tensor([sensor_data], dtype=tf.float32)  

interpreter.set_tensor(interpreter.get_input_details()[0]['index'], input_tensor)  
interpreter.invoke()  
output = interpreter.get_tensor(interpreter.get_output_details()[0]['index'])  
print(f"Predicted tip position (x, z): {output}")  
