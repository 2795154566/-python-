def test_login():
    return True

def test_camera():
    return False

def test_robot():
    raise RuntimeError("设备连接失败")


def run_tests(test_cases):
    total = 0
    passed = 0
    failed = 0
    errors = 0
    results = {} 
    for test_name, test_func in test_cases.items():
        total += 1
        try:
            result = test_func()
            if result is True:
                passed += 1
                results[test_name] = "PASS"
            else:
                failed += 1
                results[test_name] = "FAIL"
        except Exception as e:
            errors += 1
            results[test_name] = "ERROR"
    return {
        "total": total,
        "passed": passed,
        "failed": failed,
        "errors": errors,
        "results": results
    }

print(run_tests(test_cases = {
    "login": test_login,
    "camera": test_camera,
    "robot": test_robot
}))