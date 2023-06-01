'''import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    clear_screen()
    current_time = time.strftime("%H:%M:%S")
    print(f"Relógio: {current_time}")
    time.sleep(1)
'''
import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    clear_screen()
    current_time = time.strftime("%H:%M:%S")

    clock = f"""
╔════════════════════════╗
║        Relógio         ║
╠════════════════════════╣
║      {current_time}    ║
╚════════════════════════╝
    """

    print(clock)
    time.sleep(1)
