#Majority Element II

def M_elements(nums):
    if not nums:
        return []

    cand1, cand2 = None, None
    count1, count2 = 0, 0

    for num in nums:
        if num == cand1:
            count1 += 1
        elif num == cand2:
            count2 += 1
        elif count1 == 0:
            cand1, count1 = num, 1
        elif count2 == 0:
            cand2, count2 = num, 1
        else:
            count1 -= 1
            count2 -= 1

    
    count1, count2 = 0, 0

    for num in nums:
        if num == cand1:
            count1 += 1
        elif num == cand2:
            count2 += 1

    result = []
    if count1 > len(nums) // 3:
        result.append(cand1)
    if count2 > len(nums) // 3:
        result.append(cand2)

    return result

def main():
    try:
        nums = list(map(int, input("nums=").split()))
        result = M_elements(nums)
        print(result)
    except ValueError:
        print("Invalid input") #enter input with space in between

if __name__ == "__main__":
    main()

