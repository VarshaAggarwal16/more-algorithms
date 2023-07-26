def max_product_subarray(nums):
    if not nums:
        return 0

    max_product = nums[0]
    min_product = nums[0]
    result = nums[0]

    for i, num in enumerate(nums):
        print(f"index : {i}")
        if i == 0:
            continue

        # If num is negative, swap max_product and min_product
        if num < 0:
            max_product, min_product = min_product, max_product
            print("swapping")
            print(f"max_product {max_product}")
            print(f"min_product {min_product}")

        # Update max_product and min_product
        max_product = max(num, max_product * num)
        min_product = min(num, min_product * num)
        print(f"max_product : {max_product}")
        print(f"min_product {min_product}")
        # Update the result with the maximum product found so far
        result = max(result, max_product)
        print(f"result : {result}")

    print(f"final answer : {result}")
    return result

# Example usage:
nums = [2, 3, -2, 4]
result = max_product_subarray(nums)
print(result)  # Output: 6 (the subarray [2, 3] has the largest product)
