__author__ = 'kushlani'

def merge_times(intervals):
    # merges the overlapping intervals and returns new merged_list

    if len(intervals) < 2:
        return intervals

    intervals.sort()  # sorts, so earliest times moves to left

    merged_list = [intervals[0]]  # create new list to add merged intervals

    for i, (j,k) in enumerate(intervals):

        if i == 0:
            continue  # do nothing fo first interval

        (p,q) = merged_list.pop()
        if q >= j:
            merged_list.append((p,k))

        else:
            merged_list.append((p,q))
            merged_list.append((j,k))
    return merged_list


if __name__ == "__main__":
    time_list = [(0,1),(3,5),(4,8),(9,10),(10,12)]
    print ("original list: ", time_list)
    print ("mergerd list: ", merge_times(time_list))