
def selection_sort(list):
    for i in range(len(list)):
        x = list[i]
        for j in range(len(list)):
            if x < list[j]:
                list[i], list[j] = list[j], list [i]
                x= list [j]
    return list
print(selection_sort([-1, 3, 5, 0, 23,-23, 40, -10, -5]))















# # Eric's Version (on GitHub):

import random
arr = random.sample(xrange(1,100),10)

def selectionsort(list):
	for i in range(0, len(list)):
		min = i
		for x in range (i+1, len(list)):
			if list[x] < list[min]:
				min = x
		list[min], list[i] = list[i], list[min]
	print list

selectionsort(arr)
