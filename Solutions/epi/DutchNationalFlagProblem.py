
def sort(pivot_index: int, A: list) -> None:
    pivot = A[pivot_index]
    smaller, equal, larger = 0,0,len(A)
    iterations=1;
    while equal<larger:
          if A[equal]<pivot:
              A[smaller],A[equal] = A[equal],A[smaller]
              smaller,equal= smaller+1, equal+1
          elif A[equal] == pivot:
               equal +=1
          else:
              larger -=1
              A[equal],A[larger]=A[larger],A[equal]
          print("iteration " + str(iterations))
          print("index of small[" + str(smaller) + "]")
          print("index of equal[" + str(equal) + "]")
          print("index of larger[" + str(larger) + "]")
          print("The list is" + str(A))
          iterations = iterations + 1

    print("iteration" + str(iterations))
    print("index of small[" + str(smaller) + "]")
    print("index of equal[" + str(equal) + "]")
    print("index of larger[" + str(larger) + "]")
    print("The list is" + str(A))




sort(1,[0,1,2,1,0,2,0,1,2])
