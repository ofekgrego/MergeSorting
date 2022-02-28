import random
import time


def merge(arr):
    if(len(arr) == 1):
        return arr
    else:
        arrL = merge(arr[:len(arr)//2])
        arrR = merge(arr[len(arr) // 2:])
        L = 0
        R = 0
        newArr = []
        while((len(arrL) > L) & (len(arrR) > R)):
            if(arrL[L] < arrR[R]):
                newArr.append(arrL[L])
                L += 1
            else:
                newArr.append(arrR[R])
                R += 1

        while(len(arrL) > L):
            newArr.append(arrL[L])
            L += 1

        while(len(arrR) > R):
            newArr.append(arrR[R])
            R += 1

        return newArr

arr = []
count = 1000
for i in range(0,count):
    arr.append(random.randrange(0, 100))

print("Unsorted: " + str(arr))
start_time = time.process_time()
print("Sorted:" + str(merge(arr)))
print(str(time.process_time() - start_time) + " Seconds")
