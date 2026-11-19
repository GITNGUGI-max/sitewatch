import requests
from time import perf_counter, sleep
from datetime import datetime
import os
import json

def check_website(url):


    start_time = perf_counter()

    try:
        response = requests.get(url, timeout=10)

        print("HTTP Status: ", response.status_code)

        if response.status_code == 200:
            result = "PASSED"
            print("CHECK PASSED: the page is responding as expected.")
        else:
            result = "FAILED"
            print("CHECK FAILED: the HTTP status is unexpected.")

    # except requests.exceptions.Timeout:
    #     print("CHECK FAILED: the request timed out.")
    # except requests.exceptions.ConnectionError:
    #     print("CHECK FAILED: could not connect to the requested website.")
    except requests.exceptions.RequestException as error:
        print("CHECK FAILED: could not complete the request")
        print("DETAILS: ", error)

    duration_ms = round((perf_counter()-start_time)*1000, 2)
    print("Check Duration: ", duration_ms, "ms")


    checked_at = datetime.now().astimezone().isoformat(timespec="seconds")
    entry = f"{checked_at} | {url} | {result} | {duration_ms} ms\n"
    with open("checks.log", "a", encoding="utf-8") as log_file:
        log_file.write(entry)

    print("Results saved to checks.log")

interval = int(os.getenv("CHECK_INTERVAL_SECONDS", "30"))

urls = json.loads(
    os.getenv("TARGET_URLS", '["https://example.com"]')
)

if interval <= 0:
    raise ValueError("CHECK_INTERVAL_SECONDS must be greater than zero")

if not isinstance(urls, list) or not urls:
    raise ValueError("TARGET_URLS must be a non-empty JSON list")

print("Configured URLs:", urls)

try:
    while True:
        for url in urls:
            check_website(url)

        print(f"Waiting {interval} seconds before the next round...\n")
        sleep(interval)

except KeyboardInterrupt:
    print("\nMonitoring stopped.")