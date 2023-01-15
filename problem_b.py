import random
import time
import pandas as pd
def problem(array,a,b,drawData, timeTick):
    start_time=time.time()
    timelapse=0
    ele_count = [0] * (max(array)+1)
    for i in range(0, len(array)):
        ele_count[array[i]] += 1   
        drawData(ele_count, ['green' if x==i else 'red' for x in range(len(ele_count))],str(array)+" Count of each elements in count array")
        time.sleep(timeTick)  
        timelapse+=timeTick
        
    for i in range(1,max(array)+1):
        ele_count[i] += ele_count[i-1] 
        drawData(ele_count, ['cyan'  if x<=i else 'red' for x in range(len(ele_count))]," Cummulative count in count array")
        time.sleep(timeTick)  
        timelapse+=timeTick
    if a == 0:
        res=ele_count[b]
    else:
        res=(ele_count[b]-ele_count[a-1])
    end_time=time.time()
    drawData(array, ['white' for _ in range(len(array))],"Total Number Between "+str(a)+" & "+str(b)+" is "+str(res)+"    Time: "+str(end_time-timelapse-start_time))
    df=pd.DataFrame({'Algorithm': ['Problem 8.2.4'],'Inputs':[len(array)],'Time':[(end_time-timelapse-start_time)] })
    df.to_csv('time_data.csv', mode='a', index=False,header=False)
