# LOVELOCAL-Assessment

## Easy Question

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
