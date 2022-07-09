#11 logest common subsequence
import time

t0 = {'input':{'seq1': 'serendipitous', 'seq2': 'precipitation'},
      'output':7}
t1 = {'input':{'seq1': [1,3,5,6,7,2,5,2,3], 'seq2': [6,2,4,7,1,5,6,2,3]},
      'output':5}
t2 = {'input':{'seq1': 'longest', 'seq2': 'stone'},
      'output':3}
t3 = {'input':{'seq1': 'asdfwevad', 'seq2': 'opkpoiklkl'},
      'output':0}
t4 = {'input':{'seq1': 'dense', 'seq2': 'condensed'},
      'output':5}
t5 = {'input':{'seq1': '', 'seq2': 'opkpoiklkl'},
      'output':0}
t6 = {'input':{'seq1': '', 'seq2': ''},
      'output':0}
t7 = {'input':{'seq1': 'abcdef', 'seq2': 'badcfe'},
      'output':3}

tests = [t0,t1,t2,t3,t4,t5,t6,t7]

#recursion
def recursive_lcs(seq1, seq2, idx1=0, idx2=0):
    if idx1 > len(seq1)-1 or idx2 > len(seq2)-1:
        return 0
    elif seq1[idx1] == seq2[idx2]:
        return 1 + recursive_lcs(seq1, seq2, idx1+1, idx2+1)
    else:
        option1 = recursive_lcs(seq1, seq2, idx1+1, idx2)
        option2 = recursive_lcs(seq1, seq2, idx1, idx2+1)
        return max(option1, option2)

for t in tests:
    print(recursive_lcs(t['input']['seq1'], t['input']['seq2']),
          recursive_lcs(t['input']['seq1'], t['input']['seq2']) == t['output'])


#memorization
memo = {}
def memo_lcs(seq1, seq2, idx1=0, idx2=0):
    key = (idx1, idx2)
    if key in memo:
        return memo[key]
    elif idx1 > len(seq1)-1 or idx2 > len(seq2)-1:
        memo[key] = 0
    elif seq1[idx1] == seq2[idx2]:
        memo[key] = 1 + recursive_lcs(seq1, seq2, idx1+1, idx2+1)
    else:
        option1 = recursive_lcs(seq1, seq2, idx1+1, idx2)
        option2 = recursive_lcs(seq1, seq2, idx1, idx2+1)
        memo[key] = max(option1, option2)
    return memo[key]

for t in tests:
    memo = {}
    print(memo_lcs(t['input']['seq1'], t['input']['seq2']),
          memo_lcs(t['input']['seq1'], t['input']['seq2']) == t['output'])

#dynamic programming

def dp_lcs(seq1, seq2):
    matrix = [[0 for _ in range(len(seq2)+1)] for _ in range(len(seq1)+1)]
    for i in range(1,len(seq1)+1):
        for j in range(1,len(seq2)+1):
            if seq1[i-1] == seq2[j-1]:
                matrix[i][j] = 1 + matrix[i - 1][j - 1]
            else:
                matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])
    return matrix[-1][-1]

for t in tests:
    print(dp_lcs(t['input']['seq1'], t['input']['seq2']),
          dp_lcs(t['input']['seq1'], t['input']['seq2']) == t['output'])