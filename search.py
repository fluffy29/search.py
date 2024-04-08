import sys
import random
import time

N = int(sys.argv[1])

random_values = []

for _ in range(N):
    random_value = random.randint(0, 2*N - 1)
    random_values.append(random_value)

random_values.sort()

def binary_search(lst, target):
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


start_time = time.monotonic_ns()
target = random_values[5]  
index = binary_search(random_values, target)

if index != -1:
    print(f"Found {target} at index {index}")
else:
    print(f"Not found {target}")

print(random_values)

end_time = time.monotonic_ns()
print(f"Time taken: {end_time - start_time} nanoseconds")