import time

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

# List of jobs with (Job ID, Burst Time)
jobs = [(1, 6), (2, 8), (3, 7), (4, 3)]

job_first_scheduling(jobs)
