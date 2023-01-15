import time
import pandas as pd
def insertionSort(array,drawData, timeTick):
    start_time=time.time()
    timelapse=0
    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
        drawData(array, ['yellow' if x == j or x== j +1 else 'green' if x <= step else'cyan'  for x in range(len(array))] )
        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].        
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            drawData(array, ['pink' if x == j else 'green' if x <= step else'cyan'  for x in range(len(array))] )
            j = j - 1
            
            time.sleep(timeTick)
            timelapse+=timeTick
        
        # Place key at after the element just smaller than it.
        array[j + 1] = key
    end_time=time.time()
    drawData(array, ['yellow' for x in range(len(array))],"Time: "+str(end_time-timelapse-start_time))
    df=pd.DataFrame({'Algorithm': ['Insertion Sort'],'Inputs':[len(array)],'Time':[(end_time-timelapse-start_time)] })
    df.to_csv('time_data.csv', mode='a', index=False,header=False)