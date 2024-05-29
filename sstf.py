def sstf_disk_scheduling(requests, initial_position):
    total_head_movement = 0
    current_position = initial_position

    while requests:
        nearest_request = min(requests, key=lambda x: abs(x - current_position))
        
        head_movement = abs(nearest_request - current_position)
        
        total_head_movement += head_movement
        
        current_position = nearest_request
        
        requests.remove(nearest_request)

    return total_head_movement


disk_requests = [26, 86, 45, 99, 132, 80, 61, 39]

initial_head_position = 52

total_movement = sstf_disk_scheduling(disk_requests, initial_head_position)

print("Total head movement using SSTF algorithm:", total_movement)
