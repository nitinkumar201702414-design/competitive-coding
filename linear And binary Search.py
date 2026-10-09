def compare_search_algorithms(arr, target):
    n = len(arr)

    # Linear Search
    linear_index = -1
    linear_comparisons = 0

    for i in range(n):
        linear_comparisons += 1

        if arr[i] == target:
            linear_index = i
            break

    # Binary Search
    binary_index = -1
    binary_comparisons = 0
    left = 0
    right = n - 1

    while left <= right:
        mid = (left + right) // 2
        binary_comparisons += 1

        if arr[mid] == target:
            binary_index = mid
            right = mid - 1  # Continue searching for first occurrence

        elif arr[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    # Compare performance
    if linear_comparisons < binary_comparisons:
        better_algorithm = "Linear Search"
    elif binary_comparisons < linear_comparisons:
        better_algorithm = "Binary Search"
    else:
        better_algorithm = "Both Equal"

    # Return report
    return [
        "Search Comparison Report",
        "Linear Search",
        f"Index: {linear_index}",
        f"Comparisons: {linear_comparisons}",
        "Binary Search",
        f"Index: {binary_index}",
        f"Comparisons: {binary_comparisons}",
        f"Better Algorithm: {better_algorithm}"
    ]