# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    # elements = len( arrA ) + len( arrB )
    merged_arr = []
    # TO-DO
    #declare two pointers at the start of each array
    a =  0
    b =  0
    #Loop through both arrays
    while a <len(arrA) and b<len(arrB):
        #check if the element in the left array is smaller than the one in the right array
        if arrA[a] < arrB[b]:
            #add the element at index a to the merged array
            merged_arr.append(arrA[a])
            #move to the next pointer
            a+=1
        #otherwise
        else:
            #add the element at index b to the merged array
            merged_arr.append(arrB[b])
            #move to the next pointer
            b+=1
    #since in the above operation we only added one item, the smaller one 
    # loop through both arrays and ensure all items are added       
    while a < len(arrA):
        merged_arr.append(arrA[a])
        a+=1
    while b < len(arrB):
        merged_arr.append(arrB[b])
        b+=1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    #base case
    if len(arr)<2:
        return arr
    #split the array and call the mergesort function on each array
    arr_left =  merge_sort(arr[:len(arr)//2])
    arr_right = merge_sort(arr[len(arr)//2:])
    #merge the recursive functions above 
    
    arr=  merge(arr_left, arr_right)
    return arr
    


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr

merge_sort([1, 5, 8, 4])