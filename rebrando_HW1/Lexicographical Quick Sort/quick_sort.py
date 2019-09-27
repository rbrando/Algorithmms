##Python 3.7.3 Implementation
import math

###################
#- Collect input -#
###################
def get_input():
    ## Get inputs, and store them in an array
    numWordsInCase = input()
    rawArray = []
    for i in range(0,int(numWordsInCase)):
        rawArray.append(input())
    return rawArray

###################
#- Print Results -#
###################
def print_results(array):
    ## Print out the entire array
    for i in range(0,len(array)):
        for j in range(0,len(array[i])):
            print(array[i][j])

####################################
#- Quick Sort: Partition and sort -#
####################################
def quick_sort(array, start, end):
    ## Recusive loop break check -
    ## Make sure the indexes for starting point and end are consistent
    if start < end:
        ## Find the partition point, and sort out the middle.
        part = partition(array, start, end)

        ## Recursivley sort the function again.
        ## Sort the right side of the partition.
        quick_sort(array, part + 1, end)
        ## Sort the left side of the partition
        quick_sort(array, start, part - 1)

    return array

################
#- Partition -#
###############
def partition(array, start, end):
    ## Set pivot point at the beginning of the array
    pivotPoint = array[end]
    index = start - 1
    loopIndex = start

    while loopIndex in range(start, end):
        if array[loopIndex] < pivotPoint:
            index = index + 1
            #Swap the two values of the array at loopIndex and index
            array[index], array[loopIndex] = array[loopIndex], array[index]
        loopIndex = loopIndex + 1
        nextPointer = index + 1

    ## Swap the index for the item at the end of the array
    array[nextPointer], array[end] = array[end],array[nextPointer]
    ## Increment the pointer by one and return
    return nextPointer

##########
#- Main -#
##########
def main():
    numTestCases = input()

    sorted = []
    for i in range(0,int(numTestCases)):
        ## Get Input returns the input as an array
        array = get_input()
        sorted.append(quick_sort(array, 0, len(array) - 1))
    print_results(sorted)

main()
