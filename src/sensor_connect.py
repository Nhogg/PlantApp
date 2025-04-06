import time
import serial
import requests
def sensor_request():
    ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
    print(ser)
    if not ser.isOpen():
        exit("Failed to open serial port")
    time.sleep(1)  # Let Pico reset
    line = ser.readline().decode('utf-8').strip()
    print(line)

sensor_request()

# ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
# print(ser)
# if not ser.isOpen():
#     exit("Failed to open serial port")
# time.sleep(1)  # Let Pico reset
#
# # Session for chat
# session_id = None
#
# while True:
#     try:
#         line = ser.readline().decode('utf-8').strip()
#         print(line)
#         if line:
#             print(f"Read from Pico: {line}")
#
#             payload = {
#                 "plant_type": "tomato",
#                 "plant_name": "Tommy",
#                 "user_message": line,
#                 "session_id": session_id
#             }
#
#             response = requests.post("https://plantapp-z7dw.onrender.com/chat", json=payload)
#             data = response.json()
#             session_id = data.get("session_id")  # Keep using same session
#
#             print(f"Response: {data.get('response')}")
#
#     except KeyboardInterrupt:
#         print("Exiting.")
#         break
#     except Exception as e:
#         print(f"Error: {e}")
#         time.sleep(10)
#
#
#
