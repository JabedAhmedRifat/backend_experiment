from django.http import JsonResponse
from django.shortcuts import render
import time
import threading

# Simulating data that changes over time
polling_data = {"status": "No new data"}

# Function to simulate data update after a delay
def update_data():
    global polling_data
    while True:
        time.sleep(5)  # Update every 5 seconds
        polling_data = {"status": "New data available!"}

# Start the background thread to simulate data updates
thread = threading.Thread(target=update_data)
thread.daemon = True
thread.start()

def poll(request):
    return JsonResponse(polling_data)
