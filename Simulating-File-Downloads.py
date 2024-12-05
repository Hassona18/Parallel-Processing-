import threading
import time

def file_downloader(file_name):
    print(f"{file_name}: Download started.")
    for i in range(1, 6):
        print(f"{file_name}: Downloaded {i * 20}%")
        time.sleep(1)  # Simulate time taken for downloading
    print(f"{file_name}: Download complete.")

thread1 = threading.Thread(target=file_downloader, args=("File-1.mp4",))
thread2 = threading.Thread(target=file_downloader, args=("File-2.zip",))

thread1.start()
thread2.start()

thread1.join()
thread2.join()


