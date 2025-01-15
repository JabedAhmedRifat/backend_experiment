import requests
import time

while True:
    response = requests.get("http://127.0.0.1:8000/polling/poll/")
    print("Received:", response.json())
    time.sleep(3)  # Simulate short polling every 3 seconds
