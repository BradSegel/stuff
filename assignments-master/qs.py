from random import random, randint
from time import time

# global space is evil, but this lets the functions act as though it
# were pass-by-reference
A = [int(100 * random()) for i in range(30)]
# with open("QuickSort.txt", 'r') as f:
#     A = [int(x) for x in f.read().split("\r\n") if x ]

def partition(A,L,R):
    pivot = A[L] # a random element
    K = L + 1
    for J in range(L+1,R+1): # stops at R

        if A[J] < pivot:
            swap(A, K,J)
            K = K + 1
    swap(A,L, K-1) # swap the pivot with the last lower value, so everything left of pivot is less than pivot
    return K-1

def swap(A,from_idx, to_idx):
    temp = A[to_idx]
#    print "swapping: {} with {}".format(A[from_idx],A[to_idx])
    A[to_idx] = A[from_idx]
    A[from_idx]= temp

def quicksort(A,L,R):
#    print 'L: {}, R: {}, part_idx: {}'.format(L,R,part_idx)
    if L < R:
        part_idx = partition(A,L,R)
        quicksort(A,0,part_idx-1)
        quicksort(A,part_idx+1,R)

def time_passed(time_from):
    return time() - time_from


if __name__ == '__main__':
    starting = time()
    print A
    quicksort(A,0,len(A)-1)
    print A
    print 'time: {}'.format(time_passed(starting))
