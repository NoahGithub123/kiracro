import colorama
from colorama import Fore
import time
import os
from pynput.mouse import Listener as MouseListener
from pynput.mouse import Button
from pynput import keyboard
from pynput.mouse import Controller

mouse = Controller()

colorama.init()
keyboard_controller = keyboard.Controller()
mouse = Controller()

title = Fore.RED + """  _  _______ _____            _____ _____   ____  
 | |/ /_   _|  __ \     /\   / ____|  __ \ / __ \ 
 | ' /  | | | |__) |   /  \ | |    | |__) | |  | |
 |  <   | | |  _  /   / /\ \| |    |  _  /| |  | |
 | . \ _| |_| | \ \  / ____ \ |____| | \ \| |__| |
 |_|\_\_____|_|  \_\/_/    \_\_____|_|  \_\\____/ 
                                                  
""" + Fore.LIGHTMAGENTA_EX + "Made by JNN and edi\n" + Fore.CYAN + "Need support \ OR / Want TO support? " + Fore.RED + "Join the discord!: https://discord.gg/dsaJRn9wnr" + Fore.RESET
os.system("cls")
print(Fore.GREEN + "EXE VERSION!!" + Fore.RESET)

kts = input("What key would you like the macro to be? For mouse buttons type mouse: ").lower()

key_to_start = None

if kts == "mouse":
    middlemousebutton = input("What mouse button would you like to have as your keybind? (Middle, X1, or X2): ").lower()
    if middlemousebutton == "middle":
        key_to_start = Button.middle
    elif middlemousebutton == "x1":
        key_to_start = Button.x1
    elif middlemousebutton == "x2":
        key_to_start = Button.x2
else:
    key_to_start = keyboard.KeyCode.from_char(kts)

macro_enabled = False


def on_press(key):
    global macro_enabled
    try:
        if key == key_to_start:
            macro_enabled = not macro_enabled
            print_status()
    except AttributeError:
        pass


def on_release(key):
    pass


def print_status():
    os.system("cls")
    print(f"Press {key_to_start} to toggle the macro.")
    print(title)
    print("------------------------------------------")
    if macro_enabled:
        print(Fore.GREEN + "KIRACO STARTED" + Fore.RESET)
    else:
        print(Fore.RED + "KIRACO STOPPED" + Fore.RESET)


def run_macro():
    if macro_enabled:
        keyboard_controller.press('i')
        time.sleep(0.01)
        keyboard_controller.release('i')

        keyboard_controller.press('o')
        time.sleep(0.01)
        keyboard_controller.release('o')


def on_click(x, y, button, pressed):
    global macro_enabled
    if button == key_to_start and pressed:
        macro_enabled = not macro_enabled
        print_status()


def main():
    print_status()

    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener, MouseListener(on_click=on_click) as mouse_listener:
        while True:
            run_macro()
            time.sleep(0.01)


if __name__ == "__main__":
    main()

input()
