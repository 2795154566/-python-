"""
    编写函数 count_status(status_list)，统计 HTTP 状态码出现的次数。
"""
def count_status(status_list):
    status_dict = {}
    for status in status_list:
        status_dict[status] = status_dict.get(status, 0) + 1
    return status_dict


status_list = [200, 404, 200, 500, 404, 200]
result = count_status(status_list)
print(result)