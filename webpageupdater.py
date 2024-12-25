import webbrowser
import time
import random
import pyautogui

# List of URLs to open
urls = [
    "https://www.example.com",
    "https://www.wikipedia.org",
    "https://www.python.org",
    "https://www.github.com",
    "https://www.stackoverflow.com"
]


# Function to open and close URLs at random times
def open_and_close_random_urls(urls):
    while True:
        # Choose a random URL from the list
        url = random.choice(urls)

        # Open the chosen URL in the default web browser
        webbrowser.open(url)

        # Wait a random duration between 5 to 15 seconds
        duration = random.randint(5, 15)
        print(f"Opened {url}. Closing in {duration} seconds...")
        time.sleep(duration)

        # Attempt to close the current tab (CTRL + W for most browsers)
        pyautogui.hotkey('ctrl', 'w')  # Use 'cmd' instead of 'ctrl' on macOS

        # Wait for a random interval before opening the next URL (e.g., 10 to 30 seconds)
        wait_time = random.randint(10, 30)
        print(f"Waiting for {wait_time} seconds before opening the next URL...")
        time.sleep(wait_time)


# Execute the function
open_and_close_random_urls(urls)
