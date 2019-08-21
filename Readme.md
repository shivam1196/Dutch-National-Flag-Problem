# PROBLEM 10
## Dutch National Flag Problem
The problem states that we have an array of 0 1 and 2s and we need to sort in a single Traversal and time complexity of O(n) where n doesnt
means a single traversal

<br>

### Algorithm:
1. Traverse the Array till mid is less than end
2. if element is 0 place it in the beginning and update start and middle by 1
3. if element is 1 update middle by 1
4. if element is 2 place it in the end and update end by -1
5. return sorted array


### Time Complexity Analysis:
Sorting : O(N) where N is exactly number of elements (single Traversal)



### Space Complexity Analysis:
• Array : O(N) where N is size of array
