# STRETCH: implement Linear Search				
def linear_search(arr, target):
  
  # TO-DO: add missing code
  for i in range(len(arr)):
    # iterate thru for loop to find target
    if arr[i] == target:
      return i

  # not found
  return -1   


# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):
  #edge case can't be used on empty arrays
  if len(arr) == 0:
    return -1 # array empty
  # low and high value defaults to 0 and last index
  low = 0
  high = len(arr)-1

  # default found to False
  found = False

  # while low <= and we haven't found the target keep searching!
  while low <= high and not found:
    #find middle using division
    middle = (low + high) // 2

    # if we find the target return it!
    if arr[middle] == target:
      return middle

    # if we haven't found the target decide lower or higher and change low or high for next search
    else:
      if target <arr[middle]:
        # search lower half
        high = middle - 1
      else:
        #search upper half
        low = middle + 1

  return -1 # not found


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  
  middle = (low+high)//2

  if len(arr) == 0:
    return -1 # array empty
  # TO-DO: add missing if/else statements, recursive calls
