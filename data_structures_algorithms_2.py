import time
#02 rotated list(minimum num of times the sorted list was rotated
test2 = [{'inputs':{'list':[4, 5, 6, 8, 9, 0, 0, 3, 4],'query':0},
         'positions':[5]},
         {'inputs': {'list': [7, 8, 0, 1, 3, 3, 3, 4, 5], 'query': 0},
          'positions': [2]},
         {'inputs': {'list': [9, 2, 4, 4, 4, 8, 9], 'query': 2},
          'positions': [1]},
         {'inputs': {'list': [3, 3, 4, 5, 7, 9, 0, 1, 3], 'query': 0},
          'positions': [6]},
         {'inputs': {'list': list(range(1,1000000,1)), 'query': 1},
          'positions': [0]},
         {'inputs': {'list': [3,3,3,3,3,3,3,3,3], 'query': 3},
          'positions': [0]},
         {'inputs': {'list': [3], 'query': 3},
          'positions': [0]},
         {'inputs': {'list': [], 'query': -1},
          'positions': [-1]}]

#brute force
def count_rotations(list):
    i = 0
    while i < len(list)-1:
        if list[i] > list[i+1]:
            return [i+1]
        i += 1

    if list == []:
        return [-1]
    else:
        return [0]


#binary search
def condition(list, mid, lo, hi):
    mid_num = list[mid]
    status = 'not_found'
    if mid_num < list[mid-1] or mid - 1 < 0:  #mid_num < list[mid+1] or mid + 1 > len(list)-1
        status = 'found'
    elif mid_num <= list[hi]:      #mid_num >= list[hi]
        hi= mid - 1
    elif mid_num > list[hi]:      #mid_num < list[hi]
        lo = mid + 1
    return lo, hi, status


def count_rotations_2(list):
    lo = 0
    hi = len(list)-1
    while lo <= hi:
        mid = (lo + hi) // 2
        lo_cond, hi_cond, status = condition(list, mid, lo, hi)
        lo = lo_cond
        hi = hi_cond
        if status == 'found':
            return [mid]
    return [-1]

#for checking
def check_answer(output, answer):
    for o in output:
        if o in answer:
            return str("PASSED")
    else:
        return str("FAILED")


def run_2():
    for i in range(len(test2)):
        start_time = time.process_time()
        #rotations = count_rotations(test2[i]['inputs']['list'])
        rotations = count_rotations_2(test2[i]['inputs']['list'])
        end_time = time.process_time()
        execution_time = format((end_time - start_time)*1000, '.4f')
        show = check_answer(rotations, test2[i]['positions'])

        print(show, rotations, f'{execution_time}ms')

run_2()