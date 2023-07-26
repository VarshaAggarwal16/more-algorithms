def two_sum(nums, target):
    # Create a dictionary to store elements and their corresponding indices
    num_indices = {}

    # Iterate through the array
    for i, num in enumerate(nums):
        print(f"i {i}")
        print(f"num {num}")
        # Calculate the complement needed to achieve the target sum
        complement = target - num
        print(f"complement : {complement}")
        print(f"num_indices : {num_indices}")
        # Check if the complement exists in the dictionary
        if complement in num_indices:
            # Return the indices of the two numbers
            return [num_indices[complement], i]

        # Add the current element and its index to the dictionary
        num_indices[num] = i
        print(f"num_indices after putting: {num_indices}")
        print(f"                          ")

    # If no solution is found, return an empty list or any appropriate value
    return []

# Example usage:
nums = [2, 3, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print(result)  # Output: [0, 1]
