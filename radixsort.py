import time 
import pandas as pd
# Radix sort in Python


# Using counting sort to sort the elements in the basis of significant places
def countingSort(array, place,drawData, timeTick,timelapse,digit):
    
    size = len(array)
    output = [0] * size
    count = [0] * 10

    # Calculate count of elements
    for i in range(0, size):
        index = array[i] // place
        count[index % 10] += 1
        time.sleep(timeTick)   
        drawData(count, ['green' if x==i else 'red' for x in range(len(count))],str(digit)+" Digit Count of each elements in count array")
        timelapse+=timeTick

    # Calculate cumulative count
    for i in range(1, 10):
        count[i] += count[i - 1]
        time.sleep(timeTick)   
        drawData(count, ['cyan'  if x<=i else 'red' for x in range(len(count))],str(digit)+" Digit Cummulative count in count array")
        timelapse+=timeTick

    # Place the elements in sorted order
    i = size - 1
    while i >= 0:
        index = array[i] // place
        output[count[index % 10] - 1] = array[i]
        time.sleep(timeTick)   
        drawData(output, ['aquamarine'  if x<=i else 'yellow' for x in range(len(output))],str(digit)+" Digit Place the elements in original array" )
        timelapse+=timeTick
        count[index % 10] -= 1
        i -= 1

    for i in range(0, size):
        array[i] = output[i]
    
    return timelapse


# Main function to implement radix sort
def radixSort(array,drawData, timeTick):
    start_time=time.time()
    timelapse=0
    # Get maximum element
    max_element = max(array)

    # Apply counting sort to sort elements based on place value.
    place = 1
    digit=1
    while max_element // place > 0:
        timelapse=countingSort(array,place,drawData, timeTick,timelapse,digit)
        place *= 10
        digit+=1
    timelapse+=timeTick
    end_time=time.time()
    drawData(array, ['yellow' for x in range(len(array))],"Time: "+str(end_time-timelapse-start_time))
    df=pd.DataFrame({'Algorithm': ['Radix Sort'],'Inputs':[len(array)],'Time':[(end_time-timelapse-start_time)] })
    df.to_csv('time_data.csv', mode='a', index=False,header=False)


