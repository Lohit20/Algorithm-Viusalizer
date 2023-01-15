import time
import pandas as pd

def insertionSort(array,bucket,drawData, timeTick,timelapse):
    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
        drawData(array, ['yellow' if l == j or l== j +1 else 'green' if l <= step else'cyan'  for l in range(len(array))],"Sorting Elements in Bucket: "+str(bucket) )
        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].        
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            drawData(array, ['pink' if l == j else 'green' if l <= step else'cyan'  for l in range(len(array))],"Sorting Elements in Bucket: "+str(bucket) )
            j = j - 1 
            time.sleep(timeTick)
            timelapse+=timeTick
        
        # Place key at after the element just smaller than it.
        array[j + 1] = key
    return array,timelapse


			
def bucketSort(x,drawData,timeTick):
	start_time=time.time()
	timelapse=0
	arr = []
	slot_num = 10 # 10 means 10 slots, each
				# slot's size is 0.1
	for i in range(slot_num):
		arr.append([])
		
	# Put array elements in different buckets
	for j in x:
		index_b = int(slot_num * j)
		arr[index_b].append(j)
		time.sleep(timeTick)
		drawData(arr[index_b], ['green' if l==len(arr[index_b])-1 else 'red' for l in range(len(arr[index_b]))],"Elements in bucket: "+str(index_b))
		timelapse+=timeTick
	
	# Sort individual buckets
	for i in range(slot_num):
		arr[i],timelapse = insertionSort(arr[i],i,drawData, timeTick,timelapse)
		
	# concatenate the result
	k = 0
	for i in range(slot_num):
		for j in range(len(arr[i])):
			x[k] = arr[i][j]
			time.sleep(timeTick)
			drawData(arr[i], ['green' if l==j else 'red' for l in range(len(arr[i]))],"Element Chosen from the bucket: "+str(i))
			timelapse+=timeTick
			time.sleep(timeTick)
			drawData(x, ['yellow' if l<k else 'green' if l==k  else 'red' for l in range(len(x))],"Putting Back the Elements in sorted form in Original Array")
			timelapse+=timeTick
			k += 1
	end_time=time.time()
	drawData(x, ['yellow' for _ in range(len(x))],"Time: "+str(end_time-timelapse-start_time))
	df=pd.DataFrame({'Algorithm': ['Bucket Sort'],'Inputs':[len(x)],'Time':[(end_time-timelapse-start_time)]})
	df.to_csv('time_data.csv', mode='a', index=False,header=False)
