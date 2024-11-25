def bubble_sort(data):
    for _ in range(len(data)):
        for indx in range(len(data)-1):
            if data[indx] > data[indx+1]:
                data[indx], data[indx+1] = data[indx+1], data[indx]
    return data

print(bubble_sort([9,3,6,12,63,1]))