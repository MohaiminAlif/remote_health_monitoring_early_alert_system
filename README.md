# Health Monitoring System (MAX30100 + Raspberry Pi)

This project is a real-time health monitoring system using the MAX30100 sensor and Raspberry Pi, with backend anomaly detection and alert systems.

## 📁 Project Structure

- **Frontend**: React + TailwindCSS
- **Backend**: FastAPI (Python)
- **Machine Learning**: Isolation Forest for anomaly detection
- **Sensor**: MAX30100 via Raspberry Pi
- **Notification**: Email alerts for abnormal readings
- **Visualization**: Chart.js

## 🚀 Getting Started

### Backend (FastAPI)

```bash
cd backend
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
uvicorn main:app --reload
