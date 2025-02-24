import time
from collections import deque

# Function to implement Job First Scheduling
def job_first_scheduling(jobs):
    # Sorting jobs based on burst time (Shortest Job First)
    jobs.sort(key=lambda x: x[1])
    
    total_time = 0
    waiting_time = 0
    print("Job Execution Order:")
    
    for job in jobs:
        print(f"Job {job[0]} (Burst Time: {job[1]})")
        waiting_time += total_time
        total_time += job[1]
        time.sleep(0.5)  # Simulating job execution
    
    avg_waiting_time = waiting_time / len(jobs)
    print(f"\nAverage Waiting Time: {avg_waiting_time:.2f} units")

# Function to implement Round Robin Scheduling
def round_robin_scheduling(jobs, quantum):
    queue = deque(jobs)
    total_time = 0
    waiting_times = {job[0]: 0 for job in jobs}
    remaining_times = {job[0]: job[1] for job in jobs}
    
    print("Round Robin Execution Order:")
    while queue:
        job_id, _ = queue.popleft()
        execution_time = min(quantum, remaining_times[job_id])
        print(f"Job {job_id} executed for {execution_time} units")
        remaining_times[job_id] -= execution_time
        total_time += execution_time
        
        for job in queue:
            waiting_times[job[0]] += execution_time
        
        if remaining_times[job_id] > 0:
            queue.append((job_id, remaining_times[job_id]))
    
    avg_waiting_time = sum(waiting_times.values()) / len(jobs)
    print(f"\nAverage Waiting Time: {avg_waiting_time:.2f} units")

# List of jobs with (Job ID, Burst Time)
jobs = [(1, 6), (2, 8), (3, 7), (4, 3)]

time_quantum = 3
print("\n--- Job First Scheduling ---")
job_first_scheduling(jobs)

print("\n--- Round Robin Scheduling ---")
round_robin_scheduling(jobs, time_quantum)