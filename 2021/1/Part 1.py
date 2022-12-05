def count_measurement_increases(measurements:list):
    """Counts the number of measurement increases in the given list of depths

    Args:
        input (list): List of depth measurements
    """
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
    from pathlib import Path
    with open(Path(__file__).parent.resolve() / "input.txt", "r") as f:
        measurements = [int(measurement) for measurement in f.readlines()]
    
    print("How many measurements are larger than the previous measurement?")
    print("Puzzle answer: ", count_measurement_increases(measurements))