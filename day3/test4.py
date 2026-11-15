def summarize_tests(test_results, timeout=2.0):
    pass_count = 0
    count = len(test_results)
    faild_list = []

    for test_result in test_results:
        if test_result.get("status") == 200 and test_result.get("time") != None and test_result.get("time")<= timeout:
            pass_count = pass_count + 1
        else:
            faild_list.append(test_result["api"])
    pass_rate = 0
    if count == 0:
        pass_rate = 0.0
    else:
        pass_rate = round(pass_count / count * 100, 2)
    return {
        "total": count,
        "passed": pass_count,
        "failed": count-pass_count,
        "pass_rate": pass_rate,
        "failed_apis": faild_list
    }




test_results = [
    {"api": "detect_qr", "status": 200, "time": 0.5},
    {"api": "detect_image", "status": 500, "time": 0.8},
    {"api": "get_camera", "status": 200, "time": 2.5},
    {"api": "connect_device", "status": 200, "time": 1.2},
    {"api": "disconnect_device", "status": 404, "time": 0.3}
]

summarize_tests(test_results)