#!/usr/bin/env python3

def join_lists(l1, l2):
    s1 = set(l1)
    s2 = set(l2)
    s3 = s1 | s2
    return list(s3)
def match_lists(l1, l2):
    s1 = set(l1)
    s2 = set(l2)
    s3 = s1 & s2
    return list(s3)
def diff_lists(l1, l2):
    s1 = set(l1)
    s2 = set(l2)
    s3 = s1 ^ s2
    return list(s3)

if __name__ == '__main__':
    list1 = list(range(1,10))
    list2 = list(range(5,15))
    print('list1: ', list1)
    print('list2: ', list2)
    print('join: ', join_lists(list1, list2))
    print('match: ', match_lists(list1, list2))
    print('diff: ', diff_lists(list1, list2))