"""
    合并重叠区间（Merge Intervals）
"""
def merge_intervals(intervals):
    if not intervals:
        return []
    result = []
    sorted_intervals = sorted(intervals, key=lambda x: x[0])
    for start, end in sorted_intervals:
        if result and start <= result[-1][1]:
            result[-1][1] = max(result[-1][1], end)
        else:
            result.append([start, end])
    return result
        


print(merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]))
# [[1, 6], [8, 10], [15, 18]]

# print(merge_intervals([[1, 4], [4, 5]]))
# # [[1, 5]]

# print(merge_intervals([[5, 7], [1, 3], [2, 4]]))
# # [[1, 4], [5, 7]]

# print(merge_intervals([]))
# []