
def merge_sort(unsorted_list):
    l = len(unsorted_list)
    inversion_count = 0
    # here's our base case
    if l <= 2:
        # make sure our pair is ordered
        if l==2 and unsorted_list[0] > unsorted_list[1]:
            holder = unsorted_list[0]
            unsorted_list[0] = unsorted_list[1]
            unsorted_list[1] = holder
            inversion_count = 1
        return (unsorted_list, inversion_count)

    # RECURSE!!
    split_idx = l/2
    a,a_inversion_count = merge_sort(unsorted_list[:split_idx])
    b,b_inversion_count = merge_sort(unsorted_list[split_idx:])
    inversion_count = a_inversion_count + b_inversion_count

    while b: # we're putting b into a, so we don't want to stop while there's b
        for idx, a_val in enumerate(a):
            if b:
                # when we get to a value in 'a' bigger than b[0]
                if a_val > b[0]:
                    inversion_count = inversion_count + len(a[idx:])
                    a[idx:idx] = [b.pop(0)]
                # b now contains larger values than a
                if len(a) == idx + 1:
                    a.extend(b)
                    b = None # we want out of this while loop
    return (a, inversion_count)

def get_inversion_count(unsorted_list):
    i = 0
    for idx, elem in enumerate(unsorted_list,1):
        for x in unsorted_list[idx:]:
            if elem > x: i = i + 1

    return i

if __name__ == '__main__':
    # import random
    # sorter = [int(1000 * random.random()) for i in xrange(1000)]
    # print 'before: {}'.format((sorter, get_inversion_count(sorter)))
    # print 'result: {}'.format(merge_sort(sorter))

    nums = []
    with open('IntegerArray.txt', 'r') as f:
        nums = [int(x) for x in f.read().split("\r\n") if x ]

    print "brute: {}".format(get_inversion_count(nums))
    print "merge: {}".format(merge_sort(nums)[1])
#    print get_inversion_count(nums)
#    print merge_sort(nums)[1]


