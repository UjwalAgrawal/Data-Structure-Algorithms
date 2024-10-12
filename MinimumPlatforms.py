# Given arrival and departure times of all trains that reach a railway station.
# Find the minimum number of platforms required for the railway station so that no train is kept waiting.
# Consider that all the trains arrive on the same day and leave on the same day.
# Arrival and departure time can never be the same for a train but
# we can have arrival time of one train equal to departure time of the other.
# At any given instance of time, same platform can not be used for both departure of a train and
# arrival of another train. In such cases, we need different platforms.


def minimumPlatform(n, arr, dep):
    arr.sort()
    dep.sort()
    i, j = 0, 0
    c = 0
    max_count = -1
    while (i < n):
        if (arr[i] <= dep[j]):
            c += 1
            i += 1
        else:
            c -= 1
            j += 1
        max_count = max(max_count, c)
    return max_count


arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]
n = len(arr)
print("Minimum number of platforms required is", minimumPlatform(n, arr, dep))
