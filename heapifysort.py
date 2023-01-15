# Python program for implementation of heap Sort

# To heapify subtree rooted at index i.
# n is size of heap

import time
import pandas as pd

def getcolor(arr,e1,e2):
    colors=[]
    for i in range(len(arr)):
        if i==e1:
            colors.append('cyan')
        elif i==e2:
            colors.append('aquamarine')
        else:
            colors.append('red')
    return colors




def heapify(arr, N, i,drawData, timeTick,timelapse):
    largest = i # Initialize largest as root
    l = 2 * i + 1	 # left = 2*i + 1
    r = 2 * i + 2	 # right = 2*i + 2

	# See if left child of root exists and is greater than root
    if l < N and arr[largest] < arr[l]:
        time.sleep(timeTick)
        drawData(arr,getcolor(arr,largest,l),"left Child is Greater than root")
        timelapse+=timeTick
        largest = l
        

	# See if right child of root exists and is
	# greater than root
    if r < N and arr[largest] < arr[r]:
        time.sleep(timeTick)   
        drawData(arr,getcolor(arr,largest,r),"right Child is Greater than root")
        timelapse+=timeTick
        largest = r


	# Change root, if needed
    if largest != i:
        time.sleep(timeTick)   
        drawData(arr,getcolor(arr,largest,i),"Largest Node is not the root")
        timelapse+=timeTick
        arr[i], arr[largest] = arr[largest], arr[i] # swap
		# Heapify the root.
        timelapse=heapify(arr, N, largest,drawData, timeTick,timelapse)

    return timelapse
    
# The main function to sort an array of given size


def heapSort(arr,drawData, timeTick):
    N= len(arr)
    start_time=time.time()
    timelapse=0


	# Build a maxheap.
    for i in range(N//2 - 1, -1, -1):
        timelapse=heapify(arr, N, i,drawData, timeTick,timelapse)

	# One by one extract elements
    for i in range(N-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] # swap
        timelapse=heapify(arr, i, 0,drawData, timeTick,timelapse)
    timelapse+=timeTick
    end_time=time.time()
    drawData(arr, ['yellow' for _ in range(len(arr))],"Time: "+str(end_time-timelapse-start_time))
    df=pd.DataFrame({'Algorithm': ['Heapify Sort'],'Inputs':[len(arr)],'Time':[(end_time-timelapse-start_time)] })
    df.to_csv('time_data.csv', mode='a', index=False,header=False)
