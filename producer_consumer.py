import threading
import queue
import time

shared_queue = queue.Queue()

def producer():
    for i in range(10):
        data = f"Data {i}"
        print(f"Produced: {data}")
        shared_queue.put(data)
        time.sleep(1)
def consumer():
    for i in range(10):
        data = shared_queue.get()
        print(f"Consumed: {data}")
        time.sleep(2)
        shared_queue.task_done()

producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)
producer_thread.start()
consumer_thread.start()

producer_thread.join()

shared_queue.join()

print("Program finished.")