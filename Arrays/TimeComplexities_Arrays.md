# Time Complexities of Array Operations

| **Operation**            | **Big-O**         | **Explanation**                                                                                                      |
|---------------------------|-------------------|----------------------------------------------------------------------------------------------------------------------|
| **Access**               | O(1)             | Accessing an element by its index takes constant time because array indexing is direct using memory offsets.         |
| **Search**               | O(n)             | Searching requires comparing each element in the worst case (linear search).                                         |
| **Search (sorted array)**| O(log(n))        | Binary search can be applied to sorted arrays, reducing the search space logarithmically.                            |
| **Insert**               | O(n)             | Inserting at any position other than the end requires shifting all subsequent elements to the right.                 |
| **Insert (at the end)**  | O(1)             | Adding an element to the end is constant time if the array has sufficient allocated capacity.                        |
| **Remove**               | O(n)             | Removing an element requires shifting all subsequent elements to the left to fill the gap.                          |
| **Remove (at the end)**  | O(1)             | Removing the last element is constant time as no shifting of elements is required.                                   |

## Notes

### 1. Access (O(1))
- Arrays are stored in contiguous memory locations, allowing direct computation of the address for any index.
- Example: Accessing `arr[i]` is O(1).

### 2. Search (O(n))
- For an unsorted array, we need to iterate through all elements in the worst case.
- Example: Searching for a specific value that is not present in the array.

### 3. Search in Sorted Array (O(log(n)))
- Binary search divides the search space by half at every step.
- Requires the array to be sorted in ascending or descending order.
- Example: Searching for a value in a sorted array of integers.

### 4. Insert (O(n))
- Inserting an element at any position other than the end requires shifting all subsequent elements one position to the right.
- Example: Inserting at the beginning of the array.

### 5. Insert at the End (O(1))
- If the array has enough space, appending an element to the end takes constant time.
- Example: Adding an element to the end of a dynamically sized array.

### 6. Remove (O(n))
- Removing an element from any position requires shifting all subsequent elements to the left.
- Example: Removing the first element in the array.

### 7. Remove at the End (O(1))
- Removing the last element involves simply reducing the size of the array.
- Example: Popping the last element of an array.

## Example Scenarios

### Access Example:
```python
arr = [1, 2, 3, 4, 5]
element = arr[2]  # O(1)
```

### Search Example:
```python
arr = [4, 2, 5, 1, 3]
for element in arr:
    if element == 5:
        print("Found")
```

### Insert Example:
```python
arr = [1, 2, 3, 4]
arr.insert(2, 99)  # O(n) because elements 3 and 4 are shifted
```

### Remove Example:
```python
arr = [1, 2, 3, 4]
arr.pop(2)  # O(n) because elements 3 and 4 are shifted left
```

