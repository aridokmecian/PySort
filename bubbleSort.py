def bubbleSort(arr):
    #Iterate backwards through elements from index at len(arr) to 0
    for iteration in range (len(arr) - 1, 0, -1):
        #iterates through elements up to specificed iteration in previous line
        for i in range(iteration):
            #swaps elements if the current element is larger then the following element
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr