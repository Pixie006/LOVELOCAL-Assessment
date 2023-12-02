#Sliding Window Maximum

from collections import deque

def max_s_window(nums, k):
    result = []
    window = deque()

    for i, num in enumerate(nums):
     
        while window and window[0] < i - k + 1:
            window.popleft()

        while window and nums[window[-1]] < num:
            window.pop()

        window.append(i)

        if i >= k - 1:
            result.append(nums[window[0]])

    return result

def main():
    try:
       
        nums = list(map(int, input("nums=").split()))
        k = int(input("k="))
        result = max_s_window(nums, k)
        print(result)
    except ValueError:
        print("Invalid input")

if __name__ == "__main__":
    main()

