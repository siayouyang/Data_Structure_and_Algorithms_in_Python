#10 sort notebook

class Notebook:
    def __init__(self, title, username, likes):
        self.title, self.username, self.likes = title, username, likes

    def __repr__(self):
        return '\nNotebook<"{}/{}">, {} likes'.format(self.title, self.username, self.likes)

nb0 = Notebook('pytorch-basics', 'aakashns', 373)
nb1 = Notebook('linear-regression', 'siddhant', 532)
nb2 = Notebook('logistic-regression', 'vikas', 31)
nb3 = Notebook('feedfoward-nn', 'sonaksh', 94)
nb4 = Notebook('cifar10-cnn', 'biraj', 2)
nb5 = Notebook('cifar10-resnet', 'tanya', 29)
nb6 = Notebook('anime-gans', 'hemanth', 80)
nb7 = Notebook('python-fundamentals', 'vishal', 136)
nb8 = Notebook('python-functions', 'aakashns', 74)
nb9 = Notebook('python-numpy', 'siddhant', 92)

nb_list = [nb0, nb1, nb2, nb3, nb4, nb5, nb6, nb7, nb8, nb9]
print(nb_list)

def username_compare(left, right):
    if left.username < right.username:
        return 'lesser'
    elif left.username == right.username:
        return 'equal'
    elif left.username > right.username:
        return 'greater'

def likes_compare(left, right):
    if left.likes < right.likes:
        return 'lesser'
    elif left.likes == right.likes:
        return 'equal'
    elif left.likes > right.likes:
        return 'greater'


def merge(left, right, compare_model):
    i, j, merge_list = 0, 0, []
    while i < len(left) and j < len(right):
        result = compare_model(left[i], right[j])
        if result == 'lesser' or result == 'equal':
            merge_list.append(left[i])
            i += 1
        elif result == 'greater':
            merge_list.append(right[j])
            j += 1

    return merge_list + left[i:] + right[j:]


def merge_sort(list, compare_model):
    if len(list) < 2:
        return list

    mid = len(list)//2
    left_list = merge_sort(list[:mid], compare_model)
    right_list = merge_sort(list[mid:], compare_model)

    sorted_list = merge(left_list, right_list, compare_model)

    return sorted_list

print(merge_sort(nb_list, username_compare))
print(merge_sort(nb_list, likes_compare))