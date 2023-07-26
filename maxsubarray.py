def max_subarray_sum(nums):
    max_sum = float('-inf')  # Initialize max_sum to negative infinity
    current_sum = 0  # Initialize current_sum to 0

    for num in nums:
        # If current_sum becomes negative, reset it to the current element
        current_sum = max(num, current_sum + num)
        print(f"current_sum {current_sum}")
        
        # Update max_sum if needed
        max_sum = max(max_sum, current_sum)
        print(f"max sum : {max_sum}" )

    return max_sum

# Example usage:
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result = max_subarray_sum(nums)
print(result)   