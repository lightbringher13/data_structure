from collections import deque


def sliding_window_max(nums, k):
    dq = deque()  # This will store indices of the array
    max_values = []  # This will store the maximums for each window

    for i in range(len(nums)):
        # Remove elements from the front of deque if they are out of the current window
        if dq and dq[0] < i - k + 1:
            dq.popleft()

        # Remove elements from the back if they are smaller than the current element
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()

        # Add the current element index to the deque
        dq.append(i)

        # Start adding to max_values once we have the first valid window
        if i >= k - 1:
            # The element at the front is the max in the window
            max_values.append(nums[dq[0]])

    return max_values


# Test the function
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(sliding_window_max(nums, k))  # Output: [3, 3, 5, 5, 6, 7]
