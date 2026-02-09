import keyboard


def on_key_press(event):
    print(f'Pritisnjena tipka: {event.name}')


keyboard.on_press(on_key_press)


keyboard.wait('esc')