##Python 3.7.3 Implementation
import math

###################
#- Collect input -#
###################
def get_input():
    ## Get inputs, and store them in an array
    num_boxes_students = input()
    boxes,students = num_boxes_students.split()
    rawArray = []
    box_contents = input()

    return boxes, students, boxContents

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

############################
#- Search for max candies -#
############################
def max_candy(array, boxes, students, middle):
    print(array[middle])
    addUp = 0
    i = len(array) - 1
    while i in range(0, len(array)):
        addUp = math.floor(addUp + (int(array[i])/int(array[middle])))
        i = i - 1

    if addUp == students:
        return 1

##################################################################
#- Binary Search: Returns the index of the item we searched for -#
##################################################################
def binary_search(array, start, end, searchFor, boxes, students):
    ## Make sure that the start index is less than the end index
    if start <= end:
        ## Find the middle of the start and the end indicies
        middle =int((start + end)/2)

        maxCandy = max_candy(array, boxes, students, middle)

        ## Check if the midpoint is the item we are looking for
        if searchFor == int(array[middle]):
            return middle

        ## Else see if the element is smaller than the midpoint
        elif searchFor < int(array[middle]):
            return binary_search(array, start, middle - 1, searchFor, boxes, students)

        ## If the midpoint item is greate than, search the right side of the list
        # elif searchFor > int(array[middle]):
        else:
            return binary_search(array, middle + 1, end, searchFor, boxes, students)

    else:
        return False

###################
#- Find Answer -#
###################
def find_answer(boxes, students, boxContents):
    contentsArray = boxContents.split()
    quick_sort(contentsArray, 0, len(contentsArray) - 1)
    print(binary_search(contentsArray, 0, len(contentsArray) - 1, 1, boxes, students))


##########
#- Main -#
##########
def main():
    # numTestCases = input()
    numTestCases = 1
    sorted = []
    for i in range(0,int(numTestCases)):
            ## Get Input returns the inputs
            # boxes, studens, box_contents = get_input()
            find_answer(4, 2, "3 2 3 9")
    # print_results(sorted)

main()
