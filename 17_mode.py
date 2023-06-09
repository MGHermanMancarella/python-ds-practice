def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of items.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """

    num_counts = {num:nums.count(num) for num in nums}
    print(num_counts)
    max = -10000
    max_count = 0

    for num in num_counts:
        if num_counts[num] > max_count:
            max_count = num_counts[num]
            max = num

    return max

