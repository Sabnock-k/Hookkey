# 🪝 Hookkey

**Hookkey** is a simple, lightweight keylogger built **for educational purposes only**.  
This project was inspired by Acrylic (https://youtu.be/ZnAhKwHLWd4) demonstrating a keylogger setup using a USB Rubber Ducky.

---

## 🎯 Why I Made This

I created **Hookkey** after seeing a YouTube video showcasing a hardware-based keylogger using a USB Rubber Ducky. I was curious to explore the concept purely with software and minimal payloads without using a USB rubber ducky (because i can't afford one).

The goal of this project is to send a payload script as short as possible with the help of pastebin.com,to help others understand the basics of how keyloggers work and encourage ethical security research.

---

## ✨ Difference From the Video

In the original video, the creator:
- Used a **USB Rubber Ducky** to run a pre-written payload.

With **Hookkey**:
- ✅ **Software-only:** No special hardware is required.
- ✅ **Smaller payload:** The injection code is minimal — simple enough to write manually.
- ✅ **More transparent:** Easier to read and understand so you can learn.
- ✅ **Keylogger-focused:** Although in the video his logger can read mouse movements and other inputs, this logger can **only read keystrokes**, making it easy for anyone to modify this code and use it for their own learning.

---

## 🧠 How It Works

**Hookkey** works by capturing keyboard inputs and storing them into a log file for review.  
Here’s a high-level overview of the process:
1. **Keyboard hook:** Hookkey sets up a listener for all keyboard presses.
2. **Logging keys:** Every key pressed is appended to a log file.
3. **Trigger on 300 keystrokes:** Once the log file reaches **300 keystrokes**, the contents of `log.txt` will automatically be sent to your specified **Discord webhook**.
4. **Data review:** You can review the keystrokes in the local log file or on your Discord channel.
5. **Simple payload:** The code to set this up is small and easy to reproduce manually — perfect for educational purposes.

This structure allows you to understand how a keylogger intercepts and records keystrokes without relying on specialized hardware.

---

## ⚠️ Disclaimer

This is **for educational purposes only**.  
**Do not use this on computers or networks without explicit permission.**  
I take no responsibility for any unethical or illegal use of this code.

---

## 🧑‍💻 Usage

1. Modify the contents of the the inject txt file
2. Run in CMD
---

## 🤝 Contributing

Contributions are welcome!  
If you’d like to help improve **Hookkey**, feel free to **Fork** this repository.
