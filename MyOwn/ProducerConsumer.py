import threading
import queue
import time
import random

# Buffer size
BUFFER_SIZE = 5

# Shared queue
q = queue.Queue(BUFFER_SIZE)

# Producer function
def producer():
    for i in range(10):  # Producing 10 items
        item = random.randint(1, 100)  # Random item
        q.put(item)  # Add item to queue (blocks if full)
        print(f"Produced: {item}")
        time.sleep(random.uniform(0.1, 0.5))  # Simulate work
    
    q.put(None)  # Sentinel value to signal consumer termination

# Consumer function
def consumer():
    while True:
        item = q.get()  # Get item from queue (blocks if empty)
        if item is None:
            break  # Stop consuming if sentinel value received
        print(f"Consumed: {item}")
        time.sleep(random.uniform(0.1, 0.5))  # Simulate processing

# Creating threads
producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

# Starting threads
producer_thread.start()
consumer_thread.start()

# Waiting for completion
producer_thread.join()
consumer_thread.join()

print("Processing complete.")
