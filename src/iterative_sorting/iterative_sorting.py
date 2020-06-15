# TO-DO: Complete the selection_sort() function below 

def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr)):
        cur_index = i
        smallest_index = cur_index        
        # TO-DO: find next smallest element 
        #Loop through the array     
        for j in range(0, len(arr)):
            #check to see if value is greater than smallest
            if arr[j] > arr[smallest_index]:
                # assign j to smallest_index
                smallest_index = j 
       
        # TO-DO: swap
            arr[smallest_index], arr[cur_index]  =  arr[cur_index], arr[smallest_index]
        
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    #Loop through the array 
    for i in range(0, len(arr)):
        #create a variable j for the right element
        j = i+1
        #loop through the array until j is greater than array's length
        while j< len(arr):
            #checking if left element is greater than right:
            if(arr[i]>arr[j]):
            #do swap    
                arr[i], arr[j] = arr[j], arr[i]
            #iterate to next j
            j += 1

    return arr

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr