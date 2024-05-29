def sjf_scheduling(processes):
    n = len(processes)
    processes.sort(key=lambda x: (x['arrival_time'], x['burst_time']))  
    completed = []
    print(processes)
    time = 0
    while processes:
        available_processes = [p for p in processes if p['arrival_time'] <= time]
        if not available_processes:
            time = processes[0]['arrival_time']
            continue
        current_process = min(available_processes, key=lambda x: x['burst_time'])
        processes.remove(current_process)
        current_process['completion_time'] = time + current_process['burst_time']
        current_process['turnaround_time'] = current_process['completion_time'] - current_process['arrival_time']
        current_process['waiting_time'] = current_process['turnaround_time'] - current_process['burst_time']
        completed.append(current_process)
        time = current_process['completion_time']
    
    avg_tat = sum(p['turnaround_time'] for p in completed)/ n
    avg_wt = sum(p['waiting_time'] for p in completed)/ n
    
    return completed, avg_tat, avg_wt

# Example usage:
processes = [
    {'pid': 'P1', 'arrival_time': 0, 'burst_time': 2},
    {'pid': 'P2', 'arrival_time': 3, 'burst_time': 4},
    {'pid': 'P3', 'arrival_time': 4, 'burst_time': 3},
    {'pid': 'P4', 'arrival_time': 5, 'burst_time': 3},
    {'pid': 'P5', 'arrival_time': 5, 'burst_time': 1}
]

completed, avg_tat, avg_wt = sjf_scheduling(processes)

for process in completed:
    print(f"PID: {process['pid']}, AT: {process['arrival_time']}, BT: {process['burst_time']}, "
          f"CT: {process['completion_time']}, TAT: {process['turnaround_time']}, WT: {process['waiting_time']}")
print(f"Average Turnaround Time: {avg_tat}")
print(f"Average Waiting Time: {avg_wt}")
