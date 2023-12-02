#Logic : The provided code takes a user input string, trims leading and trailing whitespaces, tokenizes the string into words, extracts the last word, calculates its length, and finally outputs the original input, the length of the last word, and an explanatory message.
#algorithm :  the code follows a sequence of steps. First, it trims the input string to remove any unnecessary whitespaces. Then, it tokenizes the string by splitting it into words. Subsequently, the algorithm extracts the last word from the list of words. The length of this last word is calculated using the 'len()' function. Finally, the code prints the original input, the length of the last word, and a message explaining the result. This algorithm ensures a clear and concise process for determining and presenting the length of the last word in the provided string.

#CODE

v = input("s = ")
v = v.strip()
words = v.split()
last_word = words[-1]
lenlast_word = len(last_word)
print("Input:", v)
print("Output:", lenlast_word)
print("Explanation: The last word is \"" + last_word + "\" with length", lenlast_word)
