def contains_duplicate(nums):
    # Create an empty set to store elements
    seen = set()

    for num in nums:
        # Check if the element is already in the set
        if num in seen:
            return True

        # Add the element to the set
        seen.add(num)

    # If no duplicate is found, return False
    return False

# Example usage:
nums = [1, 2, 3, 4, 5]
result = contains_duplicate(nums)
print(result)  # Output: False

nums = [1, 2, 3, 1, 4]
result = contains_duplicate(nums)
print(result)  # Output: True
