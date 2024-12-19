import time
import random


def naive_prefix_sum(nums, queries):
    """
    Naive approach: Calculate range sums for each query by iterating over the range.
    """
    result = []
    for start, end in queries:
        range_sum = 0
        for i in range(start, end + 1):
            range_sum += nums[i]
        result.append(range_sum)
    return result


def optimized_prefix_sum(nums, queries):
    """
    Optimized approach: Use a prefix sum array to calculate range sums in O(1) for each query.
    """
    # Step 1: Build prefix sum array
    prefix_sums = [0] * (len(nums) + 1)
    for i in range(1, len(nums) + 1):
        prefix_sums[i] = prefix_sums[i - 1] + nums[i - 1]

    # Step 2: Answer each query using the prefix sum array
    result = []
    for start, end in queries:
        range_sum = prefix_sums[end + 1] - prefix_sums[start]
        result.append(range_sum)
    return result


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    queries = [[1, 3], [0, 2], [2, 4]]

    print("Naive Approach:", naive_prefix_sum(nums, queries))
    print("Optimized Prefix Sum Approach:",
          optimized_prefix_sum(nums, queries))

# time complexity
#  between brute force vs optimization
# def naive_prefix_sum(nums, queries):
#     result = []
#     for start, end in queries:
#         range_sum = 0
#         for i in range(start, end + 1):
#             range_sum += nums[i]
#         result.append(range_sum)
#     return result


# def optimized_prefix_sum(nums, queries):
#     # Step 1: Build prefix sum array
#     prefix_sums = [0] * (len(nums) + 1)
#     for i in range(1, len(nums) + 1):
#         prefix_sums[i] = prefix_sums[i - 1] + nums[i - 1]

#     # Step 2: Answer each query using the prefix sum array
#     result = []
#     for start, end in queries:
#         range_sum = prefix_sums[end + 1] - prefix_sums[start]
#         result.append(range_sum)
#     return result


# # Performance Testing
# if __name__ == "__main__":
#     # Generate a large random array and random queries
#     n = 10**5  # Size of the array
#     q = 10**4  # Number of queries
#     nums = [random.randint(1, 100)
#             for _ in range(n)]  # Array with random integers
#     queries = [[random.randint(0, n - 1), random.randint(0, n - 1)]
#                for _ in range(q)]

#     # Ensure queries are in valid range (start <= end)
#     queries = [[min(start, end), max(start, end)] for start, end in queries]

#     # Measure time for naive_prefix_sum
#     start_time = time.time()
#     naive_result = naive_prefix_sum(nums, queries)
#     naive_time = time.time() - start_time

#     # Measure time for optimized_prefix_sum
#     start_time = time.time()
#     optimized_result = optimized_prefix_sum(nums, queries)
#     optimized_time = time.time() - start_time

#     # Compare results and timings
#     assert naive_result == optimized_result, "Results do not match!"
#     print(f"Naive Approach Time: {naive_time:.6f} seconds")
#     print(f"Optimized Prefix Sum Approach Time: {optimized_time:.6f} seconds")
