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

################################
#- Divide the array into half -#
################################
def divide(array):
    midpoint = math.floor(len(array)/2)
    leftSide = array[:midpoint]
    rightSide = array[midpoint:]
    return leftSide,rightSide

#####################################
#- Merge an array into another one -#
#####################################
def merge(mainIndex, copyIndex, mainArray, copyArray):
    while copyIndex < len(copyArray):
        mainArray[mainIndex] = copyArray[copyIndex]
        mainIndex = mainIndex + 1
        copyIndex = copyIndex + 1
    return mainArray, mainIndex

#####################
#- Sort two arrays -#
#####################
def sort(left,right,array):
    ##Copy sorted information from left and right arrays into main array
    rightIndex = 0
    leftIndex = 0
    sortedIndex = 0
    while rightIndex < len(right) and leftIndex < len(left):
        ## Python automatically compares strings in lexicographical order
        if left[leftIndex] < right[rightIndex]:
            array[sortedIndex] = left[leftIndex]
            leftIndex = leftIndex + 1
        else:
            array[sortedIndex] = right[rightIndex]
            rightIndex = rightIndex + 1
        sortedIndex = sortedIndex + 1

    ## Print remaining items in each array
    merge(sortedIndex, leftIndex, array, left)
    merge(sortedIndex, rightIndex, array, right)

    return array

#########################################
#- Merge Sort: Divide, Sort, Merge -#
#########################################
def merge_sort(array):
    if len(array) != 1:
        left,right = divide(array)

        ## Recursivley call merge sort to get the array size equal to 1
        merge_sort(left)
        merge_sort(right)

        ## Merge function called within sort function
        sort(left,right,array)
        return array

###################
#- Print Results -#
###################
def print_results(array):
    ## Print out the entire array
    for i in range(0,len(array)):
        for j in range(0,len(array[i])):
            print(array[i][j])

##########
#- Main -#
##########
def main():
    numTestCases = input()
    sorted = []
    for i in range(0,int(numTestCases)):
        ## Get Input returns the input as an array
        sorted.append(merge_sort(get_input()))
    print_results(sorted)

main()
