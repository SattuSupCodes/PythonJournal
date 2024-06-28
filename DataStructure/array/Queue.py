'''queue functions such as pop and deque. 
'''

'''the .append and .pop methods make a list usable as a stack or a queue (we get FIFO behaviour
upon using these)'''

from collections import deque
'''the class collections.deque  is a thread-safe double-ended queue designed for last inserting and removing from 
both ends. When a deque is full, adding an item automatically discards an item on the
opposite end. '''

dq = deque(range(10), maxlen=10)
print(dq)
dq.appendleft(-1)
print(dq)
dq.extend([22,66])
print(dq)

