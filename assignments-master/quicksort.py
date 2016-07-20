
def quicksorter(unsorted_list, pivot_method=0):

    running = True
    # we're going to track the split with this
    pivot_index = 0
    # leftmost item as pivot
    pivot = unsorted_list[pivot_index]
    # skip the leftmost element (it's the pivot)
    counter = 1
    comparison_counter = 0


    print "usorted: {}".format(unsorted_list)

    while running:
        # if examined element is less than pivot, move it to the beginning of the list
        comparison_counter = comparison_counter + 1
        if pivot > unsorted_list[counter]:
            unsorted_list.insert(0, unsorted_list.pop(counter))
            pivot_index = pivot_index + 1
        counter = counter + 1
        if counter == len(unsorted_list): running = False

    print "comparisons: {}\nsemi_sorted: {}".format(comparison_counter, unsorted_list)

    left = unsorted_list[:pivot_index]
    if len(left) > 1:  # BASE CASE
        left = quicksorter(left)

    # we want to exclude all elems equal to pivot, hence list comp
    right = [x for x in unsorted_list[pivot_index + 1:] if x > unsorted_list[pivot_index]]
    if len(right) > 1: # BASE CASE
        right = quicksorter(right)

    # we want all elems equal to pivot, hence list comp
    mid = [x for x in unsorted_list[pivot_index:] if x == unsorted_list[pivot_index]]

    sorted_list = []
    sorted_list.extend(left)
    sorted_list.extend(mid)
    sorted_list.extend(right)

    print "sorted: {}".format(sorted_list)

    return sorted_list
# A Array, L: left bound index, R: right bound index

def parter(A, L, R):
    print A
    pivot = A[L] # leftmost elem in bounds
    K = L # + 1
    for J in range(L+1,R):
        if A[J] < pivot:
            A = swap(A, K,J)
            K = K + 1
            print A
    # why?  no idea
    swap(A,L, K-1) # return pivot to original position...  for some reason
    return K-1

def swap(swap_list, swap1, swap2):
    holder = swap_list[swap1]
    swap_list[swap1] = swap_list[swap2]
    swap_list[swap2] = holder
    return swap_list

if __name__ == '__main__':
    import random
    unsorted = [3,8,5,2,7,6,9,10,1,4]# [int(100 * random.random()) for i in xrange(10)]
    print "Here's a sorted list:\n{}".format(quicksorter( unsorted ))#[int(100 * random.random()) for i in xrange(10)]))
