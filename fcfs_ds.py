def fcfs_disk_scheduling(requests, head):
    total_head_movements = 0
    sequence = []

    # Calculate head movements
    for request in requests:
        total_head_movements += abs(head - request)
        head = request
        sequence.append(request)

    return total_head_movements, sequence

# Example usage
if __name__ == "__main__":
    requests = [98, 183, 37, 122, 14, 124, 65, 67]  # Example disk requests
    initial_head_position = 53  # Initial head position

    total_head_movements, sequence = fcfs_disk_scheduling(requests, initial_head_position)

    print("Total head movements:", total_head_movements)
    print("Sequence of disk accesses:", sequence)
