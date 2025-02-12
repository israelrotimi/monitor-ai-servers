def monitor_temperatures(
    temp_readings: list[list[float]],  # Each sublist represents 24 hours of hourly readings for one server
    warning_threshold: float,           # Temperature that indicates concern
    consecutive_hours: int             # Number of consecutive hours above threshold to trigger alert
) -> list[dict]:
    """
    Analyze temperature readings from multiple AI training servers and return alerts.
    
    Returns a list of dictionaries containing:
    - server_id: index of the server
    - start_hour: hour when concerning pattern started
    - max_temp: highest temperature in the sequence
    - duration: how many hours the pattern lasted
    """
    info_list = []
    duration = 0
    start_hour = 0
    server_id = 0
    dangerous_temperatures = []

    for i in range(len(temp_readings)):
        server = temp_readings[i]
        for j in range(len(server)):
            if server[j] >= warning_threshold:
                duration = 1
                start_hour = j + 1
                dangerous_temperatures.append(server[j])
                # print(server[j])
                # print(duration)
                overheating = True
                print('test')
                while overheating:
                    current_index = j + 1
                    print('overheating')
                    # overheating = False
                    if server[current_index] >= warning_threshold:
                        duration = duration + 1
                        dangerous_temperatures.append(server[current_index])
                        print(duration)
                        # overheating = False
                    else:
                        break
                        overheating = False
                        print(duration)
                        server_info = {}
                        server_info['server_id'] = i
                        server_info['start_hour'] = start_hour
                        server_info['max_temp'] = max(dangerous_temperatures)
                        server_info['duration'] = duration
                        
                        info_list.append(server_info)
                        print(server_info)
               
            
    return info_list                                    
            
    

# sample input    
temperatures = [
    [25.0, 24.8, 24.9, 25.1, 27.5, 28.9, 29.8, 30.1, 30.0, 29.7, 29.2, 28.1, 27.0, 26.5],  # Server 1
    [24.5, 24.6, 24.8, 24.9, 25.0, 25.1, 25.2, 25.1, 25.0, 24.9, 24.8, 24.7, 24.6, 24.5],  # Server 2
]
warning_threshold = 29.5
consecutive_hours = 3

test = monitor_temperatures(temperatures, warning_threshold, consecutive_hours)
print(test)
# sample output
[{
    'server_id': 0,
    'start_hour': 6,
    'max_temp': 30.1,
    'duration': 4
}]