import threading

def print_numbers():
    for i in range(5):
        print(threading.current_thread().name, ":", i)

# Create threads
thread1 = threading.Thread(target=print_numbers, name="Thread-1")
thread2 = threading.Thread(target=print_numbers, name="Thread-2")

# Start threads
thread1.start()
thread2.start()

# Wait for threads to finish
thread1.join()
thread2.join()