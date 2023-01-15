import time
import pandas as pd
def bubble_sort(data, drawData, timeTick):
    start_time=time.time()
    timelapse=0
    for _ in range(len(data)-1):
        for j in range(len(data)-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                drawData(data, ['green' if x == j or x == j+1 else 'red' for x in range(len(data))] )
                time.sleep(timeTick)
                timelapse+=timeTick
    end_time=time.time()
    drawData(data, ['yellow' for _ in range(len(data))],"Time: "+str(end_time-timelapse-start_time))
    df=pd.DataFrame({'Algorithm': ['Bubble Sort'],'Inputs':[len(data)],'Time':[(end_time-timelapse-start_time)] })
    df.to_csv('time_data.csv', mode='a', index=False,header=False)
    




