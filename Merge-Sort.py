import multiprocessing


def merge_sort(array):
    # Base case: if the array has 1 or no elements, it's already sorted
    if len(array) <= 1:
        return array

    # Split the array into two halves
    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]

    # Recursively sort both halves
    left = merge_sort(left)
    right = merge_sort(right)

    # Merge the two sorted halves
    return merge(left, right)


def merge_sort_parallel(array):
    # Base case: if the array has 1 or no elements, it's already sorted
    if len(array) <= 1:
        return array

    # Split the array into two halves
    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]

    # Use multiprocessing only at the top level
    with multiprocessing.Pool(2) as pool:
        sorted_sublists = pool.map(merge_sort, [left, right])

    # Merge the two sorted halves
    return merge(*sorted_sublists)


def merge(left, right):
    result = []  # Resultant merged list
    i = j = 0  # Pointers for left and right lists

    # Merge elements from both lists in sorted order
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add remaining elements from the left list
    result.extend(left[i:])
    # Add remaining elements from the right list
    result.extend(right[j:])

    return result


if __name__ == "__main__":
    # Input array to be sorted
    data = [38, 27, 43, 3, 9, 82, 10, 34, 56, 73, 91, 2]

    print("Original Array:", data)

    # Sort the array using parallel merge sort
    sorted_data = merge_sort_parallel(data)

    print("Sorted Array:", sorted_data)
