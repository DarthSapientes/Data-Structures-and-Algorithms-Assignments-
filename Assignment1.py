import random

# Generate a random list of integers
data = random.sample(range(1, 100000), 1000)

def lomuto_partition(array, left, right):
    """Partition the array using the Lomuto scheme."""
    pivot_value = array[right]
    boundary = left - 1

    for index in range(left, right):
        if array[index] < pivot_value:
            boundary += 1
            array[boundary], array[index] = array[index], array[boundary]

    array[boundary + 1], array[right] = array[right], array[boundary + 1]
    return boundary + 1


def quicksort(array, start=0, end=None):
    """In-place quicksort implementation."""
    if end is None:
        end = len(array) - 1

    if start < end:
        pivot_index = lomuto_partition(array, start, end)
        quicksort(array, start, pivot_index - 1)
        quicksort(array, pivot_index + 1, end)

    return array


print(quicksort(data))
