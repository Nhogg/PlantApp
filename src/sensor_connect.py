import time
import serial
import requests

ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
if not ser.isOpen():
    exit("Failed to open serial port")
time.sleep(2)  # Let Pico reset

session_id = None

while True:
    try:
        raw = ser.readline().decode('utf-8').strip()
        if not raw or not raw.isdigit():
            continue  # Skip empty or non-numeric lines

        sensor_value = int(raw)
        moisture_percent = 100 - int((sensor_value - 12500) / (60000 - 12500) * 100)
        moisture_percent = max(0, min(100, moisture_percent))  # Clamp to 0–100

        print(f"Moisture: {moisture_percent}%")

        payload = {
            "plant_type": "tomato",
            "plant_name": "Tommy",
            "user_message": str(moisture_percent),
            "session_id": session_id
        }

        response = requests.post("https://plantapp-z7dw.onrender.com/chat", json=payload)
        data = response.json()
        session_id = data.get("session_id")

        print(f"Bot: {data.get('response')}")

    except KeyboardInterrupt:
        print("Exiting.")
        break
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(5)
