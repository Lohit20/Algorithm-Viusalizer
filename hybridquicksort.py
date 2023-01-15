# Python implementation of the above approach
 
# Function to perform the insertion sort
import time 
import pandas as pd
def insertion_sort(arr, low, n,drawData,timeTick,timelapse):
    for i in range(low + 1, n + 1):
        val = arr[i]
        j = i
        drawData(arr, ['yellow' if x == j or x== j +1 else 'green' if x <= i else'cyan'  for x in range(len(arr))] )
        while j>low and arr[j-1]>val:
            arr[j]= arr[j-1]
            drawData(arr, ['pink' if x == j else 'green' if x <= i else'cyan'  for x in range(len(arr))] )

            j-= 1
            time.sleep(timeTick)
            timelapse+=timeTick
        arr[j]= val
    return timelapse

def getColorArray(dataLen, head, tail, border, currIdx, isSwaping = False):
    colorArray = []
    for i in range(dataLen):
        #base coloring
        if i >= head and i <= tail:
            colorArray.append('gray')
        else:
            colorArray.append('white')

        if i == tail:
            colorArray[i] = 'blue'
        elif i == border:
            colorArray[i] = 'red'
        elif i == currIdx:
            colorArray[i] = 'yellow'

        if isSwaping:
            if i == border or i == currIdx:
                colorArray[i] = 'green'

    return colorArray
# The following two functions are used
# to perform quicksort on the array.
 
# Partition function for quicksort
def partition(data, head, tail, drawData, timeTick,timelapse):
    border = head
    pivot = data[tail]

    drawData(data, getColorArray(len(data), head, tail, border, border))
    time.sleep(timeTick)
    timelapse+=timeTick
    

    for j in range(head, tail):
        if data[j] < pivot:
            drawData(data, getColorArray(len(data), head, tail, border, j, True))
            time.sleep(timeTick)
            timelapse+=timeTick

            data[border], data[j] = data[j], data[border]
            border += 1

        drawData(data, getColorArray(len(data), head, tail, border, j))
        time.sleep(timeTick)
        timelapse+=timeTick


    #swap pivot with border value
    drawData(data, getColorArray(len(data), head, tail, border, tail, True))
    time.sleep(timeTick)
    timelapse+=timeTick

    data[border], data[tail] = data[tail], data[border]
    
    return border,timelapse
 
# Function to call the partition function
# and perform quick sort on the array
# def quick_sort(arr, low, high):
#     if low<high:
#         pivot = partition(arr, low, high)
#         quick_sort(arr, low, pivot-1)
#         quick_sort(arr, pivot + 1, high)
#         return arr
 
# Hybrid function -> Quick + Insertion sort
def hybrid_quick_sort_utility(arr, low, high,drawData ,timeTick,timelapse ):
    
    while low<high:
 
        # If the size of the array is less
        # than threshold apply insertion sort
        # and stop recursion
        if high-low + 1<10:
            timelapse=insertion_sort(arr, low, high, drawData ,timeTick ,timelapse)
            break
 
        else:
            pivot,timelapse = partition(arr, low, high,drawData, timeTick,timelapse)
 
            # Optimised quicksort which works on
            # the smaller arrays first
 
            # If the left side of the pivot
            # is less than right, sort left part
            # and move to the right part of the array
            if pivot-low<high-pivot:
                timelapse=hybrid_quick_sort_utility(arr, low, pivot-1, drawData ,timeTick ,timelapse)
                low = pivot + 1
            else:
                # If the right side of pivot is less
                # than left, sort right side and
                # move to the left side
                timelapse=hybrid_quick_sort_utility(arr, pivot + 1, high, drawData ,timeTick ,timelapse)
                high = pivot-1
    
    return timelapse
# Driver code

def hybrid_quick_sort(a,drawData ,timeTick):
    start_time=time.time()
    timelapse=0
    timelapse=hybrid_quick_sort_utility(a, 0, len(a)-1,drawData ,timeTick,timelapse )
    end_time=time.time()
    drawData(a, ['white' for x in range(len(a))],"Time: "+str(end_time-timelapse-start_time))
    df=pd.DataFrame({'Algorithm': ['problem 7.4.5 Sort'],'Inputs':[len(a)],'Time':[(end_time-timelapse-start_time)] })
    df.to_csv('time_data.csv', mode='a', index=False,header=False)
