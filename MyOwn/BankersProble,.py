import numpy as np

def is_safe(processes, available, max_demand, allocation):
    num_processes = len(processes)
    num_resources = len(available)
    work = available.copy()
    finish = [False] * num_processes
    safe_sequence = []

    need = max_demand - allocation
    
    while len(safe_sequence) < num_processes:
        found = False
        for i in range(num_processes):
            if not finish[i] and all(need[i, j] <= work[j] for j in range(num_resources)):
                work += allocation[i]
                finish[i] = True
                safe_sequence.append(processes[i])
                found = True
                break
        
        if not found:
            return False, []
    
    return True, safe_sequence


def main():
    processes = [0, 1, 2, 3, 4]
    available = np.array([3, 3, 2])
    max_demand = np.array([[7, 5, 3],
                            [3, 2, 2],
                            [9, 0, 2],
                            [2, 2, 2],
                            [4, 3, 3]])
    allocation = np.array([[0, 1, 0],
                            [2, 0, 0],
                            [3, 0, 2],
                            [2, 1, 1],
                            [0, 0, 2]])
    
    safe, sequence = is_safe(processes, available, max_demand, allocation)
    if safe:
        print("System is in a safe state. Safe sequence:", sequence)
    else:
        print("System is in an unsafe state. Deadlock detected.")

if __name__ == "__main__":
    main()
