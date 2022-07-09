import time
#01 sorted in ascending order
test1 = [{'inputs':{'list':[0, 1, 3, 4, 4, 5, 6, 8, 9],'query':4},
         'positions':[3]},
         {'inputs': {'list': [0, 1, 3, 3, 3, 4, 5, 7, 8], 'query': 3},
          'positions': [2]},
         {'inputs': {'list': [0, 2, 4, 4, 4, 8, 9, 9], 'query': 1},
          'positions': [-1]},
         {'inputs': {'list': [0, 1, 3, 3, 3, 4, 5, 7, 9], 'query': 9},
          'positions': [8]},
         {'inputs': {'list': list(range(1,1000000,1)), 'query': 80},
          'positions': [79]},
         {'inputs': {'list': [], 'query': 8},
          'positions': [-1]},
         {'inputs': {'list': [1,1,1,1,1,1,1,1], 'query': 1},
          'positions': [0]}]

#brute force
def find_position(list, query):
    i = 0
    positions = []
    while i < len(list):
        if list[i] == query:
            positions.append(i)
        i += 1
    if positions == []:
        positions = [-1]
    return [min(positions)] #index on the far left


#binary search
def condition(list, mid, query, lo, hi):
    mid_num = list[mid]
    status = 'not_found'
    if mid_num == query:
        if list[mid - 1] != query or mid - 1 < 0:   #list[mid + 1] != query or mid + 1 > len(list) - 1
            status = 'found'
        else:
            hi = mid - 1       #hi/lo = mid -/+ 1
    elif mid_num < query:      #mid_num > query
        lo = mid + 1
    elif mid_num > query:      #mid_num < query
        hi = mid - 1
    return lo, hi, status


def find_position_2(list, query):
    lo = 0
    hi = len(list)-1
    while lo <= hi:
        mid = (lo + hi) // 2
        lo_cond, hi_cond, status = condition(list, mid, query, lo, hi)
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


def run_1():
    for i in range(len(test1)):
        start_time = time.process_time()
        #positions = find_position(test1[i]['inputs']['list'], test1[i]['inputs']['query'])
        positions = find_position_2(test1[i]['inputs']['list'],test1[i]['inputs']['query'])
        end_time = time.process_time()
        execution_time = format((end_time - start_time)*1000, '.4f')
        show = check_answer(positions, test1[i]['positions'])

        print(show, positions, f'{execution_time}ms')

run_1()


