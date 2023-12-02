#Logic : The task at hand is to count the occurrences of the digit '1' in all non-negative integers less than or equal to a given integer n. The algorithm iterates through each number from 1 to n, converts each number to a string, and counts the occurrences of the digit '1' in that string representation. The total count is then calculated and returned as the result.
#Algorithm : The algorithm for counting the occurrences of the digit '1' in all non-negative integers up to a given value n follows a straightforward process. Starting with an initial count of zero, the algorithm iterates through each number from 1 to n. For each number, it converts the integer to its string representation and counts how many times the digit '1' appears in the string. The counts for each number are accumulated, resulting in the total count of occurrences of the digit '1' in the specified range. This algorithm effectively addresses the problem by considering each number individually and tallying the occurrences of the target digit.

def count_ones(n):
    count = 0
    for i in range(1, n + 1):
        count += str(i).count('1')
    return count

n = int(input("n = "))
result = count_ones(n) if n > 0 else 0
print("Output:", result)
