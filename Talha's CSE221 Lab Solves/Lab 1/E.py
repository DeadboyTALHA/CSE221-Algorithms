def bubbleSort(arr):                                                    
    for i in range(len(arr)-1):
        flag = False
        for j in range(len(arr)-i-1): 
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flag = True
        if flag == False:
            break
    for j in arr:
        print(j, end = ' ')
N = int(input())
a = input()
arr = list(map(int, a.split(' ')))
bubbleSort(arr)