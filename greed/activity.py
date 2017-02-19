# coding: utf8

def activity_selector(stime, etime, activity_i, activity_j):
    # Note: etime must be sorted.
    activity_m = activity_i + 1
    while activity_m < activity_j and stime[activity_m] < etime[activity_i]:
        activity_m += 1
    if activity_m < activity_j:
        return [activity_m] + activity_selector(stime, etime, activity_m, activity_j)
    else:
        return []

# or non-recursive version:
def activity_selector2(stime, etime):
    # Note: etime must be sorted.
    n = len(stime)
    activity_set = [1]
    activity_i = 1
    for activity_m in range(2, n):
        if stime[activity_m] >= etime[activity_i]:
            activity_set.append(activity_m)
            activity_i = activity_m
    return activity_set


if __name__ == '__main__':
    stime = [0, 1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
    etime = [0, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    print(activity_selector(stime, etime, 0, 12))
    print(activity_selector2(stime, etime))
