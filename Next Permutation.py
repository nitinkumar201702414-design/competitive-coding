def nextPermutation(nums):
    n = len(nums)
    i = n - 2
    # 1. Find the first decreasing element from the right
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1
    # 2. Swap it with the next larger element to its right
    if i >= 0:
        j = n - 1
        while nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
    # 3. Reverse the suffix (this also handles the last-permutation case)
    nums[i + 1:] = reversed(nums[i + 1:])