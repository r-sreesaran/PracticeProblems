


def quickSort(alist):
    return quickSortHelper(alist, 0, len(alist) - 1)


def quickSortHelper(alist,first,last):
     if first<last:
         splitpoint = partition(alist,first,last)

     quickSortHelper(alist,first,splitpoint+1)
     quickSortHelper(alist,splitpoint,last-1)

def partition():



alist = [54, 26, 78, 17, 77, 48, 55, 31, 20]
quickSort(alist)
print(alist)
