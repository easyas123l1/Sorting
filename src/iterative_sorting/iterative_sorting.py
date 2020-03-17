# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        # holds the smallest number index
        smallest_index = cur_index
        for x in range(cur_index + 1, len(arr)):
            # update smallest index and swap its position
            if arr[x] < arr[smallest_index]:
                temp = arr[smallest_index] 
                arr[smallest_index] = arr[x]
                arr[x] = temp

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    # variable for if was a change made thru loop
    changes = True
    # while loop looking for 1 change on a for loop
    while changes == True:
        #default changes to false
        changes = False
        for i in range(0, len(arr)):
            # edge case can't do i+1 on last index
            if i != len(arr) -1:
                # if current index is larger then index + 1 swap.
                if arr[i] > arr[i+1]:
                    temp = arr[i]
                    arr[i] = arr[i+1]
                    arr[i+1] = temp
                    changes = True


    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):
    
    return arr

print(selection_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7]))