def product_except_self(nums):
    n = len(nums)
    answer = [1] * n

    # Calculate prefix products up to each element
    prefix_product = 1
    for i in range(n):
        print(f"i {i}" )
        answer[i] *= prefix_product
        print(f"answer : {answer}")
        prefix_product *= nums[i]
        print(f"prefix-product : {prefix_product}")

    # Calculate suffix products starting from each element
    suffix_product = 1
    for i in range(n - 1, -1, -1):
        print(f"backward traverse {i}")
        answer[i] *= suffix_product
        suffix_product *= nums[i]

    return answer

# Example usage:
nums = [3, 5, 7, 3, 6]
result = product_except_self(nums)
print(result)  # Output: [24, 12, 8, 6]

