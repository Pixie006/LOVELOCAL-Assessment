#Logic : The given Python code defines a function s_palindrome that takes a string s as input and aims to find the shortest palindrome by adding characters in front of it. The logic involves iterating through the characters of the input string, identifying the longest palindrome substring that starts from the beginning of the string. The algorithm employs two pointers, one at the beginning 'i' and the other at the end 'j', comparing characters and incrementing the pointer accordingly.
#Algorithm : The function then returns the original string concatenated with the reversed remaining part of the string. The result is then printed.In essence, the algorithm efficiently determines the shortest palindrome by identifying the longest matching prefix and appending the reversed remaining portion.For example, if the user inputs "aacecaaa", the output will be "aaacecaaa," as it represents the shortest palindrome obtainable by adding characters in front of the original string. 


#CODE
def s_palindrome(s):
    i = 0
    for j in range(len(s) - 1, -1, -1):
        if s[i] == s[j]:
            i += 1

    return s[i:][::-1] + s

s = input("s = ")

result = s_palindrome(s)
print("Output:", result)
