# LOVELOCAL-Assessment

## Easy Question(Easy3-Pascal's Triangle)

### Logic:

* The goal is to generate Pascal's triangle with the specified number of rows (num_rows).
* Pascal's triangle is a triangular array of binomial coefficients where each number is the sum of the two numbers directly above it.

### Algorithm:

* Initialize an empty list tri to store the rows of Pascal's triangle.
* Iterate over the range from 0 to num_rows - 1 to generate each row:
* Create a new list row with 1 as the initial value.
* For each position in the row (excluding the first and last positions):
  * Update the value at the current position based on the sum of the two elements directly above it in the previous row.
  * Append the generated row to the tri list.
* Return the generated Pascal's triangle as a list of lists (tri).

## Medium Question(Medium2-Majority Element)

### Logic:

* The goal is to find elements in the array that appear more than[n/3]times, where n is the length of the array.
* Check if candidates appear more than [n/3] times in the array.
* The code uses the Boyer-Moore Majority Vote algorithm to efficiently find the potential candidates for majority elements.

### Algorithm:

* Initialize two candidate variables (cand1 and cand2) and their corresponding counters (count1 and count2) to keep track of potential majority elements.
* Iterate through the array:
  * If the current element is equal to cand1, increment count1.
  * If the current element is equal to cand2, increment count2.
  * If count1 is 0, update cand1 to the current element and set count1 to 1.
  * If count2 is 0, update cand2 to the current element and set count2 to 1.
  * If none of the above conditions is met, decrement both count1 and count2.
* Reset the counters and iterate through the array again to count the occurrences of the potential candidates.
* Check if the counts of cand1 and cand2 are greater than [n/3].
* If yes, add the candidates to the result list.
* Return the result list containing the elements that appear more than [n/3] times.

## Hard Question(Hard1-Sliding Window Maximum)

### Logic:

* The code finds the maximum element in each sliding window of size k in a given array. It uses a deque to efficiently maintain the relevant indices within the current window.

### Algorithm:

* Initialize an empty deque window to store indices.
* Initialize an empty list (result) to store the maximum values in each sliding window.
* Initialize a deque (window) to store indices of elements in the current window.
* Sliding Window Iteration:
   * Iterate through the array with the help of the enumerate function to get both the index (i) and element (num).
* Maintaining the Deque:
  * In the first while loop, remove indices from the front of the deque that are outside the current window (indices that are too old).
  * In the second while loop, remove indices from the back of the deque if the corresponding elements are smaller than the current element (num). This ensures the deque only contains potential maximum elements.
* Adding Current Index to Deque:
  * Add the current index (i) to the deque.
* Adding Maximum to Result:
  * If the window size is reached (i.e., i >= k - 1), add the maximum element (front of the deque) to the result.
* Result:
  * The result is a list containing maximum values in each sliding window.

