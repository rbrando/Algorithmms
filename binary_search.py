##Python 3.7.3 Implementation
import math

###################
#- Collect input -#
###################
def get_input():
    ## Get inputs, and store them in an array
    num_stall_cows = input()
    stalls, cows = num_stall_cows.split()
    locations = []
    for i in range(0, int(stalls), 1):
        locations.append(input())

    return stalls, cows, locations

###################
#- Print Results -#
###################
def print_results(array):
    ## Print out the entire array
    for i in range(0,len(array)):
        print(array[i])
    print()

def heap_sort(array):
    build_max_heap(array)

    length = len(array) - 1
    for i in range(length, 0, -1):
        array[i],array[0] = array[0], array[i]
        heapify(array, i, 0)

## Create a max heap from an unsorted array
def build_max_heap(array):
    # Build Up the Max Heap
    floor = math.floor(len(array)/2)
    for i in range(floor, -1, -1):
        heapify(array,len(array), i)

## Similar to buil-max-heap, but assumes partof array is already sorted
def heapify(array, length, index):
    left = (2 * index) + 1 ## Gives the left side of the parent node
    right = (2 * index) + 2 ## Gives the right side of the parent node

    maxNum = index

    # Check left side of the heap for the max number
    if (left < length) and (array[left] > array[index]):
        maxNum = left

    # Check right side of the heap for the max number
    if (right < length) and (array[right] > array[maxNum]):
        maxNum = right

    if (maxNum != index):
        array[index], array[maxNum] = array[maxNum], array[index]
        heapify(array, length, maxNum)

#########################
#- Find the difference -#
#########################
def check_correct(array, find, cows):
    num_placed = 1
    lastChecked = int(array[0])
    for i in range(1, len(array) - 1, 1):
        diff = int(array[i]) - int(lastChecked)
        # print("Find: " + str(find) + " Checking: " + str(int(array[i]) - int(lastChecked)))
        if diff >= find:
            lastChecked = int(array[i])
            num_placed = num_placed + 1
            if num_placed == cows:
                return 1
    return 0


##################################################################
#- Binary Search: Returns the index of the item we searched for -#
##################################################################
def binary_search(array, cows):
    start = 0
    end = len(array) - 1
    max_min_value = 0
    while (end > start):
        middle = int((start + end)//2)
        answer = check_correct(array, middle, cows)
        ## If value was found to be incorrect check left of the mid point
        if answer == 1:
            if (middle > max_min_value):
                max_min_value = middle
            start = middle + 1

        ## Else if value was found set max value and search to the right of the midpoint
        else:
            end = middle
    return max_min_value

##########
#- Main -#
##########
def main():
    numTestCases = input()
    # numTestCases = 1
    sorted = []
    for i in range(0,int(numTestCases)):
            ## Get Input returns the inputs
            stalls, cows, locations = get_input()
            # stalls = '5'
            # cows = '3'
            # locations = ['1','2','8','4']
            # heap_sort(locations)
            locations.sort()
            sorted.append(binary_search(locations, int(cows)))
            # print("Answer: " + str(binary_search(locations, int(cows))))
    print_results(sorted)

main()
