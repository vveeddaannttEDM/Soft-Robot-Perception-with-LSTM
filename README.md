
# Soft-Robot-Perception-with-LSTM
# Soft Robot Perception with Embedded Sensors and LSTM Networks  
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)  

This repository replicates the work from *"Soft robot perception using embedded soft sensors and recurrent neural networks"* (Thuruthel et al., Science Robotics 2019). It includes code for training an LSTM model to predict soft robot kinematics and external forces using simulated sensor data.

## 📄 Paper Summary  
**Problem**: Traditional rigid sensors fail to capture high-dimensional deformations in soft robots.  
**Solution**:  
- Use **embedded soft cPDMS sensors** (carbon nanotube-PDMS composite).  
- Train **LSTM networks** to model sensor dynamics and predict:  
  - Kinematics (e.g., fingertip position)  
  - External forces  
**Key Contributions**:  
- Bio-inspired redundant sensor placement.  
- Real-time prediction robust to sensor drift/noise.  
- Graceful degradation under sensor failure.  

## 🛠️ Installation  
1. Clone the repo:  
   ```bash  
   git clone https://github.com/yourusername/soft-robot-perception.git  
   cd soft-robot-perception  
