import time
import matplotlib.pyplot as plt

def binary_search(arr, target):
    start_time = time.time()
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid, time.time() - start_time
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1, time.time() - start_time

def plot_binary_search_time_complexity(input_sizes):
    binary_execution_times = []

    for size in input_sizes:
        arr = list(range(size))
        target = size - 1

        binary_index, binary_time_taken = binary_search(arr, target)
        binary_execution_times.append(round(binary_time_taken, 6))

    plt.plot(input_sizes, binary_execution_times, 'o-', markersize=4)
    plt.xlabel('Input Size')
    plt.ylabel('Time Taken (seconds)')
    plt.title('Binary Search Time Complexity')
    plt.grid(True)
    plt.show()

input_sizes = [10, 50, 100, 500, 1000]
plot_binary_search_time_complexity(input_sizes)
