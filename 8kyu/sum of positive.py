def positive_sum(arr):
    positives = 0
    for i in range(len(arr)):
        if arr[i]>0:
            positives += arr[i]
        else:
            pass
    return positives