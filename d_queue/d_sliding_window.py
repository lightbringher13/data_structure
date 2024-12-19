from collections import deque


def sliding_window_max(n, k):
    max_values = []
    dq = deque()


if __name__ == "__main__":
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print("Sliding window maximums:", sliding_window_max(nums, k))
