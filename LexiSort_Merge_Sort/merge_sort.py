###################
#- Collect input -#
###################
def get_input():
    print("Please enter the test cases. The first line should be the number of test cases, followed by the cases you want to test.")
    num_testcases = raw_input()
    raw_array = []
    for i in range(0,int(num_testcases)):
        raw_array.append(raw_input())
    return raw_array

##############################
#- Divide and array in half -#
##############################
def divide(array):
    middle = len(array)/2
    rightArray = array[middle:]
    leftArray = array[:middle]
    return leftArray, rightArray


######################
#- Merge Two Arrays -#
######################
def merge(first_array, second_array):
    for i in second_array:
        first_array.append(i)
    return first_array

#####################
#- Sort two arrays -#
#####################
def sort(array, leftArray, rightArray):
    rightArrayIndex = 0
    mainArrayIndex = 0
    ## Set left array index in the for loop
    for leftArrayIndex in range(0,len(leftArray)):
        if leftArray[leftArrayIndex] < rightArray[rightArrayIndex]:
            array[mainArrayIndex] = leftArray[leftArrayIndex]
            leftArrayIndex = leftArrayIndex + 1
        else:
            array[mainArrayIndex] = rightArray[rightArrayIndex]
            rightArrayIndex = rightArrayIndex + 1
        mainArrayIndex = mainArrayIndex + 1

    ## Print the remaining entries in the array
    while rightArrayIndex < len(rightArray):
        array[mainArrayIndex] = rightArray[rightArrayIndex]
        rightArrayIndex = rightArrayIndex + 1
        mainArrayIndex = mainArrayIndex + 1

    while leftArrayIndex < len(leftArray):
        array[mainArrayIndex] = leftArray[leftArrayIndex]
        leftArrayIndex = leftArrayIndex + 1
        mainArrayIndex = mainArrayIndex + 1
    return array

################
#- Merge Sort -#
################
def merge_sort(array):

    if len(array) != 1:
        left,right = divide(array)
        merge_sort(left)
        merge_sort(right)

        sort(array,left,right)



##########
#- MAIN -#
##########
def main():
    #first_array = get_input()
    #second_array = get_input()


    first_array = ['worldhello','helloworld','otterslide','Stanley']
    second_array = ['aaaaaaaaaa','Aaaaaaaaaa','slowpoke']



    merge_sort(first_array)
    merge_sort(second_array)
    final  = merge(first_array, second_array)
    merge_sort(final)
    print(final)


main()
