import time
import pandas as pd
def countingSort(array,drawData, timeTick):
    start_time=time.time()
    timelapse=0
    size = len(array)
    output = [0] * size

    # Initialize count array
    count = [0] * 10
    # drawData(count, ['green' for x in range(len(count))] )



    # Store the count of each elements in count array
    for i in range(0, size):
        count[array[i]] += 1
        time.sleep(timeTick)   
        drawData(count, ['green' if x==i else 'red' for x in range(len(count))],str(array)+" Count of each elements in count array")
        timelapse+=timeTick

    
    temp=count
    # Store the cummulative count
    for i in range(1, 10):
        count[i] += count[i - 1]
        time.sleep(timeTick)   
        drawData(count, ['cyan'  if x<=i else 'red' for x in range(len(count))],str(temp)+" Cummulative count in count array")
        timelapse+=timeTick

    # Find the index of each element of the original array in count array
    # place the elements in output array

    i = size - 1
    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        time.sleep(timeTick)   
        drawData(output, ['aquamarine'  if x<=i else 'yellow' for x in range(len(output))],"Place the elements in original array" )
        timelapse+=timeTick
        count[array[i]] -= 1
        i -= 1

    # Copy the sorted elements into original array
    for i in range(0, size):
        array[i] = output[i]
        time.sleep(timeTick)
        timelapse+=timeTick
    end_time=time.time()
    drawData(array, ['yellow' for x in range(len(array))],"Time: "+str(end_time-timelapse-start_time))
    df=pd.DataFrame({'Algorithm': ['Count Sort'],'Inputs':[len(array)],'Time':[(end_time-timelapse-start_time)] })
    df.to_csv('time_data.csv', mode='a', index=False,header=False)


