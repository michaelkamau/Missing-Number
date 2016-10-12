def find_missing(list1, list2):
    """
    Finds and returns  the element in either list1 or list2 but not both
    :param list1
    :param list2
    :return: element
    """
    set1 = set(list1)
    set2 = set(list2)
    diff = set1 ^ set2
    if len(diff) != 0:
        return diff.pop()
    else:
        return 0