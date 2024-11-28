from itertools import permutations

def bubble_sort(data):
    for _ in range(len(data)):
        for indx in range(len(data)-1):
            if data[indx] > data[indx+1]:
                data[indx], data[indx+1] = data[indx+1], data[indx]
    return data

def is_sorted(a_list):
    for i in range(len(a_list)-1):
        if not a_list[i] <= a_list[i+1]:
            return False
    return True

def permutation_sort(data):
    permutes = list(permutations(data))
    for permute in permutes:
        if is_sorted(permute):
            return permute




print(permutation_sort([1,6,2,6,3,6,12,63,46,124]))