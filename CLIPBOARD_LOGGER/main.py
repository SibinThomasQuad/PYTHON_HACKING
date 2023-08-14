import time
import pyperclip
import datetime
import os
import threading

# Maintain a set to store previously logged clipboard contents
logged_clipboard_contents = set()

def save_clipboard_data(data):
    now = datetime.datetime.now()
    date_folder = now.strftime("%Y-%m-%d")
    time_stamp = now.strftime("%H-%M-%S")
    folder_path = f"clipboard_logs/{date_folder}"
    os.makedirs(folder_path, exist_ok=True)  # Create the date folder if it doesn't exist
    filename = f"{time_stamp}.txt"
    file_path = f"{folder_path}/{filename}"
    
    if data not in logged_clipboard_contents:
        with open(file_path, "w") as file:
            file.write(data)
        logged_clipboard_contents.add(data)

def clipboard_monitor():
    while True:
        clipboard_data = pyperclip.paste()
        save_clipboard_data(clipboard_data)
        time.sleep(5)  # Adjust the interval as needed

if __name__ == "__main__":
    try:
        # Create the logs directory
        os.makedirs("clipboard_logs", exist_ok=True)
        
        # Start clipboard monitoring thread
        monitor_thread = threading.Thread(target=clipboard_monitor)
        monitor_thread.daemon = True
        monitor_thread.start()
        
        print("Clipboard logger started. Press Ctrl+C to stop.")
        monitor_thread.join()
    except KeyboardInterrupt:
        print("\nClipboard logger stopped.")
