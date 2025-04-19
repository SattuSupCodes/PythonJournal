def is_safe_state(processes, avail, max_need, alloc):
    n = len(processes)
    m = len(avail)

    # Calculate the Need matrix
    need = [[max_need[i][j] - alloc[i][j] for j in range(m)] for i in range(n)]

    finish = [False] * n
    safe_sequence = []
    work = avail.copy()

    while len(safe_sequence) < n:
        progress = False
        for i in range(n):
            if not finish[i] and all(need[i][j] <= work[j] for j in range(m)):
                for j in range(m):
                    work[j] += alloc[i][j]
                finish[i] = True
                safe_sequence.append(processes[i])
                progress = True
        if not progress:
            return False, []

    return True, safe_sequence


# Example input
processes = [0, 1, 2, 3, 4]
available = [3, 3, 2]  # Available resources

allocation = [
    [0, 1, 0],  # P0
    [2, 0, 0],  # P1
    [3, 0, 2],  # P2
    [2, 1, 1],  # P3
    [0, 0, 2]   # P4
]

maximum = [
    [7, 5, 3],  # P0
    [3, 2, 2],  # P1
    [9, 0, 2],  # P2
    [2, 2, 2],  # P3
    [4, 3, 3]   # P4
]

# Run the algorithm
is_safe, sequence = is_safe_state(processes, available, maximum, allocation)

# Output
if is_safe:
    print("System is in a SAFE state.")
    print("Safe sequence:", ' -> '.join(f"P{p}" for p in sequence))
else:
    print("System is in a DEADLOCK state.")
#  cheat code jajajajajaajaj