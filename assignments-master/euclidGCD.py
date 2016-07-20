import time
from matplotlib import pyplot #as plt

def GCD(m,n):
    counter = 0
    while n != 0:
        counter = counter + 1
        r = m % n
        m = n
        n = r
    return [counter, m]

def gcdizer(gcd_to_number=10):
    print 'starting to calculate GCD from all pairs of integers from 2 to {}'.format(gcd_to_number)
    counter = 0
    for m in range(2, gcd_to_number + 1): # outer loop, m will be slow
        for n in range(2, gcd_to_number + 1): # inner loop, n will be fast
            # combinations of n < m have already been calculated
            if n >=m:
                # I expect there is another way to speed this up by tracking multiples
                counter = counter + 1
                print 'GCD of {0} and {1} is {3} and took {2}'.format(m,n,*GCD(m,n))

    print 'finished in {} loops to find all combinations from 2 to {}'.format(counter, gcd_to_number)

def better_gcdizer(gcd_to_num=10):
#    print 'starting to calculate GCD from all pairs of integers between 2 and {}'.format(gcd_to_num)
    counter = 0
    m=gcd_to_num
    output ={}
    start_time = time.time()

    # count from high to low, seems to be 1 fewer eval per execution for GCD(m,n) when n > m
    while m > 1:
        n = gcd_to_num
        while n > 1:
            counter = counter + 1
            val = GCD(m,n)
            if 'loop_count' not in output or val[0] >= output['loop_count']:
                output['loop_count'], output['GCD'] = val # 0: number of loops, 1: the GCD
                output['m_value'] = m # .append(m) # 2: outer value being processed
                output['n_value'] = n # .append(n) # 3: inner value being processed
                # 4: amount of time it took to get to the answer
                now_time = time.time()
                print '----N={}----\nnumLoops={}\nn,m={},{}\nseconds to run:{}\nreal time: {}'.format(gcd_to_num,val[0], n, m, now_time-start_time, time.ctime())
                output['time_for_answer'] = now_time - start_time
            n = n - 1
            if n < m: break # avoid duplicating effort since 3,5 is the same as 5,3
        m = m - 1

    output['time_to_run'] = time.time() - start_time

    return output


def gdc_looper( max_n=1000, n_step=100 ):
    all_results = []
    for val in range(0,max_n,n_step)[1:]:
        all_results.append( better_gcdizer(val) )
        all_results[-1]['N'] = val


    for x in all_results: print x
    return all_results


def plot_timing(list_of_dicts):
    plt = pyplot

    plt.plot([a['N'] for a in list_of_dicts],[a['time_for_answer'] for a in list_of_dicts],[a['N'] for a in list_of_dicts],[a['time_to_run'] for a in list_of_dicts])
    plt.xlabel('N')
    plt.ylabel('time')
    plt.legend(['time taken to get answers','time taken to finish running','number of loops to find answer'])
    plt.show()

def plot_numbers(list_of_dicts):
    plt = pyplot

    plt.plot([a['N'] for a in list_of_dicts],[a['m_value'] for a in list_of_dicts],[a['N'] for a in list_of_dicts],[a['n_value'] for a in list_of_dicts])
    plt.xlabel('N')
    plt.ylabel('GCDs')
    plt.legend(['m values','n value'])
    plt.show()

if __name__ == '__main__':
    starter = time.ctime()
    results = gdc_looper(30000,100)
    ender = time.ctime()

    plot_timing( results )
    plot_numbers( results )

    for x in results:
        print 'For an N of {}: GCD of {} and {} is {} found in {} seconds in {} loops that ran a for {} seconds'.format(
            x['N'],
            x['m_value'],
            x['n_value'],
            x['GCD'],
            x['time_for_answer'],
            x['loop_count'],
            x['time_to_run']
        )

    print "start: {}\nend: {}".format(starter, ender)
