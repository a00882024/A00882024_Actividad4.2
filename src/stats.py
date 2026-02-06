"""Statistics functions implementation."""

def count(data):
    """Return the number of elements in the data."""
    return len(data)

def mean(data):
    """Calculate the arithmetic mean."""
    total = 0
    samples = count(data)

    for i in range(samples):
        total += data[i]

    return total / samples


def median(data):
    """Calculate the median."""
    middle_index = int(count(data) / 2)
    sorted_data = sorted(data)
    middle_element = sorted_data[middle_index]

    if len(data) % 2 == 0:
        first_middle_element = sorted_data[middle_index - 1]
        return mean([first_middle_element, middle_element])

    return middle_element


def mode(data):
    """Calculate the mode."""
    counts = {}
    max_key = None
    max_count = 0

    for value in data:
        counts[value] = counts.get(value, 0) + 1
        if counts[value] > max_count:
            max_count = counts[value]
            max_key = value

    return max_key


def variance(data):
    """
    Calculate the population variance.

    The formula to calculate the population variance:

    var = Sum(xi - avg)^2 / N

    xi = each value in the population
    avg = the mean
    N = number of samples
    """
    avg = mean(data)
    squared_diffs = 0

    for value in data:
        squared_diffs += (value - avg) ** 2

    return squared_diffs / count(data)


def standard_deviation(data):
    """
    Calculate the population standard deviation.

    std_dev = square root of variance
    """
    return variance(data) ** 0.5
