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

######################
#- Merge Two Arrays -#
######################
def merge(first_array, second_array):
    for i in second_array:
        first_array.append(i)
    return first_array

#################################
#- Swap two items in the array -#
#################################
def swap(first,second):
    first, second = second, first

#######################
#- Quick Sort Arrays -#
#######################
def partition(array,pivot,end):
    # array_pivot = array[pivot]
    # index = pivot
    # past_index = end - 1
    # while(True):
    #     while(array[index] <= array_pivot):
    #         index += 1
    #     while(array[past_index] >= array_pivot):
    #         past_index-= 1
    #         print(past_index)
    #     if index == past_index:
    #         #first, second = second, first
    #         array[index],array[past_index] = array[past_index],array[index]
    #     else:
    #         break
    #     print(index)
    # #swap(array[pivot],array[past_index])
    # array[pivot],array[past_index] = array[past_index],array[pivot]
    pivot_value = array[pivot]
    pivot_index = pivot
    for i in range(0,end-1):
        if array[i] < pivot_value:
            pivot_index = pivot_index + 1
            array[i],array[pivot_index] = array[pivot_index],array[i]
    array[pivot], array[pivot_index] = array[pivot_index], array[pivot]
    return pivot_index


################
#- Quick Sort -#
################
def quick_sort(array, low_num, high_num):
    if (low_num < high_num):
        pivot_index = partition(array,low_num,high_num)
        quick_sort(array,low_num,high_num-1)
        quick_sort(array,low_num+1,high_num)


##########
#- MAIN -#
##########
def main():
    #first_array = get_input()
    #second_array = get_input()

    first_array = ['worldhello','helloworld','otterslide','Stanley']
    second_array = ['aaaaaaaaaa','Aaaaaaaaaa','slowpoke']

    unsorted = merge(first_array, second_array)

    quick_sort(unsorted,1,len(unsorted))

    print(unsorted)


main()
