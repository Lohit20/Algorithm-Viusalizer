import time
import pandas as pd

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

def quick_sort_utility(data, head, tail, drawData, timeTick,timelapse):
    if head < tail:
        partitionIdx,timelapse = partition(data, head, tail, drawData, timeTick,timelapse)

        #LEFT PARTITION
        timelapse=quick_sort_utility(data, head, partitionIdx-1, drawData, timeTick,timelapse)

        #RIGHT PARTITION
        timelapse=quick_sort_utility(data, partitionIdx+1, tail, drawData, timeTick,timelapse)
    return timelapse

def quick_sort(data, head, tail, drawData, timeTick):
    start_time=time.time()
    timelapse=0
    timelapse=quick_sort_utility(data, head, tail, drawData, timeTick,timelapse)
    end_time=time.time()
    drawData(data, ['white' for x in range(len(data))],"Time: "+str(end_time-timelapse-start_time))
    df=pd.DataFrame({'Algorithm': ['Quick Sort'],'Inputs':[len(data)],'Time':[(end_time-timelapse-start_time)] })
    df.to_csv('time_data.csv', mode='a', index=False,header=False)


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