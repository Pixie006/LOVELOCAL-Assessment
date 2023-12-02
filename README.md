# LOVELOCAL-Assessment

## Easy Question(Easy3-Pascal's Triangle)

### Logic:

* Generate Pascal's triangle up to the given number of rows.
* Each element is the sum of the two elements directly above it.

### Algorithm:

* Initialize an empty list triangle.
* Iterate from 0 to numRows - 1 to represent each row:
  * Create a new list row with 1 as the initial value.
  * Update the values of row based on the sum of elements from the previous row.
  * Append row to triangle.
* Return the generated triangle.

## Medium Question(Medium2-Majority Element)

### Logic:

* Use Boyer-Moore Majority Vote algorithm to find candidates.
* Check if candidates appear more than ⌊ n/3 ⌋ times in the array.

### Algorithm:

* Initialize counters and candidates.
* Iterate through the array:
  * If a candidate matches the current element, increment the counter.
  * If a counter becomes zero, update the candidate.
  * If neither candidate matches, decrement both counters.
* Check if candidates appear more than ⌊ n/3 ⌋ times.

## Hard Question(Hard1-Sliding Window Maximum)

### Logic:

* Use a deque to efficiently maintain the maximum elements in a sliding window.
* Process each element in the array and maintain a deque with indices of elements in the current window.

### Algorithm:

* Initialize an empty deque window to store indices.
* Iterate through the array:
  * Remove indices from the front of the deque that are outside the current window.
  * Remove indices from the back of the deque if the corresponding elements are smaller than the current element.
  * Add the current index to the deque.
  * If the window size is reached, add the maximum element (front of deque) to the result.
* Return the list of maximum elements in each sliding window.
