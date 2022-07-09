#12 Knapsack

t0 = {'input':{'capacity': 165,
               'weights': [23,31,29,44,53,38,63,85,89,82],
               'profits': [92,57,49,68,60,43,67,84,87,72]},
      'output':309}

t1 = {'input':{'capacity': 3,
               'weights': [4,5,1],
               'profits': [1,2,3]},
      'output':3}

t2 = {'input':{'capacity': 4,
               'weights': [4,5,6],
               'profits': [1,2,3]},
      'output':1}

t3 = {'input':{'capacity': 170,
               'weights': [41,50,49,59,55,57,60],
               'profits': [442,525,511,593,546,564,617]},
      'output':1735}

t4 = {'input':{'capacity': 15,
               'weights': [4,5,6],
               'profits': [1,2,3]},
      'output':6}

t5 = {'input':{'capacity': 15,
               'weights': [4,5,1,3,2,5],
               'profits': [2,3,1,5,4,7]},
      'output':19}

tests = [t0,t1,t2,t3,t4,t5]

#recursion
def recursive_knapsack(capacity, weights, profits, idx=0):
    if idx > len(weights)-1:
        return 0
    elif weights[idx] > capacity:
        return recursive_knapsack(capacity, weights, profits, idx + 1)
    elif weights[idx] <= capacity:
        option1 = recursive_knapsack(capacity, weights, profits, idx + 1)
        option2 = profits[idx] + recursive_knapsack(capacity - weights[idx], weights, profits, idx + 1)
        return max(option1, option2)

for t in tests:
    print(recursive_knapsack(**t['input']), recursive_knapsack(**t['input']) == t['output'])

#memorization
def memo_knapsack(capacity, weights, profits, idx=0):
    key = (capacity, idx)
    if key in memo:
        pass
        #return memo[key]
    elif idx > len(weights)-1:
        memo[key] = 0
    elif weights[idx] > capacity:
        memo[key] = recursive_knapsack(capacity, weights, profits, idx + 1)
    elif weights[idx] <= capacity:
        option1 = recursive_knapsack(capacity, weights, profits, idx + 1)
        option2 = profits[idx] + recursive_knapsack(capacity - weights[idx], weights, profits, idx + 1)
        memo[key] = max(option1, option2)
    return memo[key]

for t in tests:
    memo = {}
    print(memo_knapsack(**t['input']), memo_knapsack(**t['input']) == t['output'])

#dynamic programming
def dp_knapsack(capacity, weights, profits):
    matrix = [[0 for _ in range(capacity + 1)] for _ in range(len(weights) + 1)]
    for i in range(1, len(weights) + 1):    #skip the first row
        for j in range(1, capacity + 1):    #skip the first column
            if weights[i-1] <= j:
                matrix[i][j] = max((profits[i-1] + matrix[i-1][j-weights[i-1]]), matrix[i - 1][j])
            else:
                matrix[i][j] = matrix[i - 1][j]
    return matrix[-1][-1]

for t in tests:
    print(dp_knapsack(**t['input']), dp_knapsack(**t['input']) == t['output'])