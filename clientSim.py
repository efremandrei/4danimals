import requests
import time
import random
from datetime import datetime, timedelta

def check_endpoints(endpoints, run_duration_hours=24):
    end_time = datetime.now() + timedelta(hours=run_duration_hours)
    consecutive_failures = 0

    while datetime.now() < end_time:
        endpoint = random.choice(endpoints)
        attempt_count = 0
        success = False

        while attempt_count < 3:
            try:
                response = requests.get(endpoint)
                if response.status_code == 200:
                    print(f"Success: {endpoint} returned 200")
                    time.sleep(2)
                    success = True
                    consecutive_failures = 0
                    break
                else:
                    print(f"Failed: {endpoint} returned {response.status_code}")
                    attempt_count += 1
                    time.sleep(5)
            except requests.exceptions.RequestException as e:
                print(f"Exception for {endpoint}: {e}")
                attempt_count += 1
                time.sleep(5)

        if not success:
            consecutive_failures += 1
            if consecutive_failures >= 3:
                print("Three consecutive endpoints failed 3 times in a row. Stopping execution.")
                return
        else:
            consecutive_failures = 0

        print("Completed one iteration.")

# Example list of endpoints
endpoints = [
    "http://test-container:8080/",
    "http://test-container:8080/faqs",
    "http://test-container:8080/about-us",
    "http://test-container:8080/add-volunteer",
    "http://test-container:8080/add-adopter",
    "http://test-container:8080/add-animal",
    "http://test-container:8080/view-volunteers",
    "http://test-container:8080/view-adopters",
    "http://test-container:8080/view-animals",
    "http://test-container:8080/log-in",
]

# Run the function
check_endpoints(endpoints)
