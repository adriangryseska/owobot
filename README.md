# OwO Autotyping Bot Script
AutoTyping Bot with CAPTCHA Detection

This project is a Python-based auto-typing bot designed to automate repetitive tasks in a game environment. It uses libraries like `pyautogui` for automating key presses, `pytesseract` for CAPTCHA detection, and `pygame` for audio notifications. The bot runs in the background, detects CAPTCHA prompts, and allows the user to resume the script by pressing the 'Down Arrow' key.

Key features include:

- Auto-typing commands at regular intervals.
- Captcha detection using OCR (Optical Character Recognition) via pytesseract.
- Music notifications upon CAPTCHA detection.
- Pause/Resume functionality using keyboard input.
- Multi-threading for running CAPTCHA checks and typing commands simultaneously.
This bot is useful for automating tasks in environments where CAPTCHA or user input is required intermittently.
