#09 sort
import time
import random

test0 = {'input' : { 'nums' : [2,4,7,4,9,3,6,1]},
         'output' : sorted([2,4,7,4,9,3,6,1])}

test1 = {'input' : { 'nums' : [1,2,3,4,5,6,7,8]},
         'output' : sorted([1,2,3,4,5,6,7,8])}

test2 = {'input' : { 'nums' : [3,3,3,3,3,3,3,3]},
         'output' : sorted([3,3,3,3,3,3,3,3])}

test3 = {'input' : { 'nums' : [8,7,6,5,4,3,2,1]},
         'output' : sorted([8,7,6,5,4,3,2,1])}

test4 = {'input' : { 'nums' : []},
         'output' : sorted([])}

test5 = {'input' : { 'nums' : [3]},
         'output' : sorted([3])}

sl = list(range(1000, 0, -1))
random.shuffle(sl)
test6 = {'input' : { 'nums' : sl},
         'output' : sorted(list(sl))}

test_list = [test0, test1, test2, test3, test4, test5, test6]

#bubble_sort
def sort(nums):
    nums = list(nums)
    for j in range(len(nums)-1):
        for i in range(len(nums)-1-j):
            if nums[i] > nums[i+1]:
                nums[i+1], nums[i] = nums[i], nums[i+1]
    return nums

for test in test_list:
    start = time.process_time()
    ans = sort(test['input']['nums'])
    end = time.process_time()
    execution_time = f'{(end - start)*1000}ms'
    print(ans, ans == test['output'], execution_time)

#insertion_sort
def insertion_sort(nums):
    nums = list(nums)
    for i in range(len(nums)):
        curr = nums.pop(i)
        j = i -1
        while j >= 0 and curr < nums[j]:
            j -= 1
        j += 1
        nums.insert(j, curr)
        #print(nums)
    return nums

for test in test_list:
    start = time.process_time()
    ans = insertion_sort(test['input']['nums'])
    end = time.process_time()
    execution_time = f'{(end - start)*1000}ms'
    print(ans, ans == test['output'], execution_time)

#merge_sort
def merge(left_nums, right_nums):
    merge_nums = []
    i, j = 0, 0
    while i < len(left_nums) and j < len(right_nums):
        if left_nums[i] <= right_nums[j]:
            merge_nums.append(left_nums[i])
            i += 1
        elif right_nums[j] <= left_nums[i]:
            merge_nums.append(right_nums[j])
            j += 1

    if i < len(left_nums):
        return merge_nums + left_nums[i:]
    if j < len(right_nums):
        return merge_nums + right_nums[j:]

#print(merge([2,4,6,6], [2,2,4,8,10,12]))

def merge_sort(nums):
    if len(nums) <= 1:
        return nums

    mid = len(nums)//2
    left_nums = nums[:mid]
    right_nums = nums[mid:]

    sorted_left_nums = merge_sort(left_nums)
    sorted_right_nums = merge_sort(right_nums)

    sorted_nums = merge(sorted_left_nums, sorted_right_nums)

    return sorted_nums

for test in test_list:
    start = time.process_time()
    ans = merge_sort(test['input']['nums'])
    end = time.process_time()
    execution_time = f'{(end - start)*1000}ms'
    print(ans, ans == test['output'], execution_time)

#quick_sort
def partition(nums, start=0, end=None):
    if end is None:
       end = len(nums)-1

    left = start
    right = end-1
    while left < right:
        if nums[left] <= nums[end]:
            left += 1
        elif nums[right] > nums[end]:
            right -= 1
        else:
            nums[left], nums[right] = nums[right], nums[left]
    if nums[end] < nums[left]:
        nums[end], nums[left] = nums[left], nums[end]
        return left
    else:
        return end    #or left + 1    #important


def quick_sort(nums, start=0, end=None):
    if end is None:
        nums = list(nums)
        end = len(nums)-1

    if start < end:    #important
        pivot = partition(nums, start, end)
        quick_sort(nums, start, pivot - 1)
        quick_sort(nums, pivot+1, end)

    return nums
print(quick_sort([2,7,9,3,1,8,10,2,5,7,9,5]))


for test in test_list:
    start = time.process_time()
    ans = quick_sort(test['input']['nums'])
    end = time.process_time()
    execution_time = f'{(end - start)*1000}ms'
    print(ans, ans == test['output'], execution_time)


