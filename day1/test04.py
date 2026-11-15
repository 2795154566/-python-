"""
    responses = [
        {"api": "/login", "status_code": 200, "time": 0.3},
        {"api": "/register", "status_code": 500, "time": 1.2},
        {"api": "/users", "status_code": 200, "time": 2.5},
        {"api": "/logout", "status_code": 200, "time": 0.4}
]   
    要求：
    1. status_code 必须等于 200。
    2. 响应时间 time 不能大于 timeout。
    3. 每个接口可能存在多项失败原因，需全部记录。
    4. 统计通过和失败的接口数量。
    5. 缺少 status_code 或 time 字段时，记录对应错误，不要导致程序崩溃。
    6. 假设 api 字段始终存在，且响应时间和超时阈值均为有效非负数字。
"""
def check_responses(responses, timeout=2.0):
    errors = []
    passed_count = 0 
    failed_count = 0
    for response in responses:
        flag = True
        if "status_code" not in response:
            tmp = response["api"] + "status_code 字段缺失"
            errors.append(tmp)
        elif response["status_code"] != 200:
            flag = False
            tmp = response["api"] + str(response["status_code"])
            errors.append(tmp)

        if "time" not in response:
            tmp = response["api"] + "time 字段缺失"
            errors.append(tmp)
        elif response["time"] > timeout:
            flag = False
            tmp = response["api"] + str(response["time"])
            errors.append(tmp)
        
        if flag:
            passed_count = passed_count + 1   
        else:
            failed_count = failed_count + 1

    return {
        "passed": passed_count,
        "failed": failed_count,
        "errors": errors
    }




    



