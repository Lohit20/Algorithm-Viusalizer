import time
import pandas as pd
def merge_sort(data, drawData, timeTick):
    start_time = time.time()
    timelapse=0
    timelapse=merge_sort_alg(data,0, len(data)-1, drawData, timeTick,timelapse)
    end_time=time.time()
    drawData(data, ['green' for x in range(len(data))],"Time: "+str(end_time-timelapse-start_time))
    df=pd.DataFrame({'Algorithm': ['Merge Sort'],'Inputs':[len(data)],'Time':[(end_time-timelapse-start_time)] })
    df.to_csv('time_data.csv', mode='a', index=False,header=False)


def merge_sort_alg(data, left, right, drawData, timeTick,timelapse):
    if left < right:
        middle = (left + right) // 2
        timelapse=merge_sort_alg(data, left, middle, drawData, timeTick,timelapse)
        timelapse=merge_sort_alg(data, middle+1, right, drawData, timeTick,timelapse)
        timelapse=merge(data, left, middle, right, drawData, timeTick,timelapse)
    return timelapse

def merge(data, left, middle, right, drawData, timeTick,timelapse):
    drawData(data, getColorArray(len(data), left, middle, right))
    time.sleep(timeTick)
    timelapse+=timeTick

    leftPart = data[left:middle+1]
    rightPart = data[middle+1: right+1]

    leftIdx = rightIdx = 0

    for dataIdx in range(left, right+1):
        if leftIdx < len(leftPart) and rightIdx < len(rightPart):
            if leftPart[leftIdx] <= rightPart[rightIdx]:
                data[dataIdx] = leftPart[leftIdx]
                leftIdx += 1
            else:
                data[dataIdx] = rightPart[rightIdx]
                rightIdx += 1
        
        elif leftIdx < len(leftPart):
            data[dataIdx] = leftPart[leftIdx]
            leftIdx += 1
        else:
            data[dataIdx] = rightPart[rightIdx]
            rightIdx += 1
    
    drawData(data, ["green" if x >= left and x <= right else "white" for x in range(len(data))])
    time.sleep(timeTick)
    timelapse+=timeTick
    return timelapse

def getColorArray(leght, left, middle, right):
    colorArray = []

    for i in range(leght):
        if i >= left and i <= right:
            if i >= left and i <= middle:
                colorArray.append("yellow")
            else:
                colorArray.append("pink")
        else:
            colorArray.append("white")

    return colorArray
