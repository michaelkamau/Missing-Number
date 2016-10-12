
def find_missing(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    diff = set1 ^ set2
    if len(diff) != 0:
        return diff.pop()
    else:
        return 0