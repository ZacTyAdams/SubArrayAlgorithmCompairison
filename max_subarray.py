#Zac Adams
#An example for the calculation of max subarrays using different algorithms

from optparse import OptionParser

MINIMUM = -9999999999999999999

def max_subarray_bruteforce(array):
    beg = 0
    end = 0
    max_sum_sofar = MINIMUM
    for i in range(0, len(array)):
        s = 0
        for j in range(i, len(array)):
            s += array[j]
            if s > max_sum_sofar:
                beg = i
                end = j
                max_sum_sofar = s
    return (beg, end, max_sum_sofar)

def find_max_crossing_subarray(A, low, mid, high):
    left_sum = MINIMUM
    max_left = MINIMUM
    max_right = MINIMUM
    sum = 0
    for i in range(mid, low-1,-1):
        sum = sum + A[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i
    right_sum = MINIMUM
    sum = 0
    for j in range(mid+1,high+1,1):
        sum = sum + A[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j

    return(max_left,max_right,left_sum+right_sum)
        


def max_subarray_divandconquer(A, low, high):

    if high == low:
        return(low,high,A[low])
    else:
        mid = (low + high)/2
        (left_low,left_high,left_sum) = max_subarray_divandconquer(A,low,mid)
        (right_low,right_high,right_sum) = max_subarray_divandconquer(A,mid+1,high)
        (cross_low,cross_high,cross_sum) = find_max_crossing_subarray(A,low,mid,high)

        if left_sum > right_sum and left_sum > cross_sum: 
            return(left_low,left_high,left_sum)
        elif right_sum > left_sum and right_sum > cross_sum:
            return(right_low,right_high,right_sum)
        else:
            return(cross_low,cross_high,cross_sum)




if __name__ == "__main__":
    usage = "usage: %prog FILE"
    parser = OptionParser(usage=usage)
    parser.add_option("-m", "--mode",
                      choices=['bruteforce', 'divandconquer'],
                      default='bruteforce',
                      help="Mode to calculate the maximum subarray")
    (options, args) = parser.parse_args()
    if len(args) != 1:
        parser.error("Please provide an input file")

    f = open(args[0], 'r')
    array = []
    for l in f.readlines():
        array = map(int, l.split(" "))
        if options.mode == 'bruteforce':
            (i, j, s) = max_subarray_bruteforce(array)
        else:
            (i, j, s) = max_subarray_divandconquer(array, 0, len(array)-1)
        print i, j, s        
    f.close()
    
