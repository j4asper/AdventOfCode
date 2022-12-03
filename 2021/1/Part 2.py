def get_sliding_window_measrements(measurements:list):
    new_measurements = list()
    
    three_last_measurements = list()
    for measurement in measurements:
        three_last_measurements.append(measurement)
        if len(three_last_measurements) == 3:
            new_measurements.append(sum(three_last_measurements))
            three_last_measurements.pop(0)
            
    return new_measurements
        

def count_measurement_increases(measurements:list):
    """Counts the number of measurement increases in the given list of depths

    Args:
        input (list): List of depth measurements
    """
    measurements = get_sliding_window_measrements(measurements)
    previous_measurement = None
    increases = 0
    for measurement in measurements:
        if previous_measurement != None:
            if measurement > previous_measurement:
                increases += 1
                
        previous_measurement = measurement
    
    return increases


if __name__ == "__main__":
    # First convert the input data to a list of measurements.
    with open("2021\\1\\input.txt", "r") as f:
        measurements = [int(measurement) for measurement in f.readlines()]
    
    print("Consider sums of a three-measurement sliding window. How many sums are larger than the previous sum?")
    print("Puzzle answer: ", count_measurement_increases(measurements))