


def quickSort(alist):
    return quickSortHelper(alist, 0, len(alist) - 1)


def quickSortHelper(alist,first: int,last: int) -> None:
     if first<last:
         splitpoint = partition(alist,first,last)
         quickSortHelper(alist,first,splitpoint-1)
         quickSortHelper(alist,splitpoint+1,last)

def partition(alist,first: int,last: int) -> None:
    partitionValue = alist[first]

    done=False
    leftmark = first + 1
    rightmark = last

    while not done:
        while leftmark<=rightmark and alist[leftmark]<=partitionValue:
            leftmark = leftmark +1
        while rightmark>=leftmark and alist[rightmark]>=partitionValue:
            rightmark=rightmark-1
        if leftmark>rightmark:
            done=True
        else:
          alist[rightmark],alist[leftmark] = alist[leftmark],alist[rightmark]
          
    alist[first],alist[rightmark]=alist[rightmark],alist[first]
    return rightmark

alist = [54, 26, 78, 17, 77, 48, 55, 31, 20]
quickSort(alist)
print(alist)
