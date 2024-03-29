# 1. Biggie Size - Given a list, write a function that 
# changes all positive numbers in the list to "big".
# Example:  returns that same 
# list, but whose values are now [-1, "big", "big", -5]

def biggie_size(list):
    for i in range(0,len(list)):
        if list[i]>0:
            list[i] = "big"
    return list
print(biggie_size([-1, 3, 5, -5]))

# 2. Count Positives - Given a list of numbers, create a 
# function to replace the last value with the number of 
# positive values. (Note that zero is not considered to 
# be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original 
# list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the 
# list to [1,6,-4,-2,-7,2] and returns it

def count_positives(list):
    count = 0
    for i in range(0,len(list)):
        if list[i]>0:
            count += 1
    list[len(list)-1] = count
    return list
print(count_positives([-1,1,1,1]))

# 3. Sum Total - Create a function that takes a list and 
# returns the sum of all the values in the list.
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7

def sum_total(list):
    sum = 0
    for i in range(0,len(list)):
        sum += list[i]
    return sum
print(sum_total([1,2,3,4]))

# 4. Average - Create a function that takes a list and 
# returns the average of all the values.x
# Example: average([1,2,3,4]) should return 2.5

def average(list):
    sum = 0
    for i in range(0,len(list)):
        sum += list[i]
    avg = sum / len(list)
    return avg
print(average([1,2,3,4]))

HELP

# 5. Length - Create a function that takes a list and 
# returns the length of the list.
# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0

def length(list):
    return len(list)
print(length([37,2,1,-9]))

# 6. Minimum - Create a function that takes a list of 
# numbers and returns the minimum value in the list. If 
# the list is empty, have the function return False.
# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False

def minimum(list):
    min = list[0]
    for i in range(0,len(list)):
        if min > list[i]:
            min = list[i]
    return min
    # if len(list)==0:
    #     return "False"
    # return min(list)
print(minimum([37,2,1,-9]))

# 7. Maximum - Create a function that takes a list and 
# returns the maximum value in the list. If the list is 
# empty, have the function return False.
# Example: maximum([37,2,1,-9]) should return 37
# Example: maximum([]) should return False

def maximum(list):
    max = list[0]
    for i in range(0,len(list)):
        if max < list[i]:
            max = list[i]
    return max
    # if len(list)==0:
    #     return "False"
    # return max(list)
print(maximum([37,2,1,-9]))

# 8. Ultimate Analysis - Create a function that takes a 
# list and returns a dictionary that has the sumTotal, 
# average, minimum, maximum and length of the list.
# Example: ultimate_analysis([37,2,1,-9]) should return 
# {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 
# 'maximum': 37, 'length': 4 }

def ultimate_analysis(arr):
    myDict = {
        'sumTotal' : sum_total(arr),
        'average' : average(arr),
        'min' : minimum(arr),
        'max' : maximum(arr),
        'length' : length(arr)
    }
    return myDict
print(ultimate_analysis([37,2,1,-9]))


def ultimate_analysis(list):
    dictionary = {}
    sumTotal = sum(list)
    average = sumTotal / len(list)
    minimum = min(list)
    maximum = max(list)
    length = len(list)
    dictionary['sumTotal'] = sumTotal
    dictionary['average'] = average
    dictionary['minimum'] = minimum
    dictionary['maximum'] = maximum
    dictionary['length'] = length
    return dictionary
print(ultimate_analysis([37,2,1,-9]))

# 9. Reverse List - Create a function that takes a list 
# and return that list with values reversed. Do this 
# without creating a second list. (This challenge is known 
# to appear during basic technical interviews.)
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]

def reverse_list(list):
    for i in range(0, len(list) // 2):
        temp = list[i]
        list[i] = list[len(list)-1-i]
        list[len(list)-1-i] = temp
    return list

print(reverse_list([7,5,-7,2,3,5, 20, 5,1]))


def reverse_list(list):
    list.reverse()
    return list
print(reverse_list([37,2,1,-9]))