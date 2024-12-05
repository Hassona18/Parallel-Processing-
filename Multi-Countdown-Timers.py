# Multiple Countdown Timers

import threading
import time

def countdown_timer(name, seconds):
    while seconds > 0:
        print(f"{name}: {seconds} seconds remaining")
        time.sleep(1)
        seconds -= 1
    print(f"{name}: Time's up!")

thread1 = threading.Thread(target=countdown_timer, args=("Timer-1", 5))
thread2 = threading.Thread(target=countdown_timer, args=("Timer-2", 8))

thread1.start()
thread2.start()

thread1.join()
thread2.join()
