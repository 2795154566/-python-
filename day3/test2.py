def group_scores(scores):
    excellent_list = []
    passed_list = []
    failed_list = []

    for name, grade in scores.items():
        if grade >= 90 and grade <= 100:
            excellent_list.append(name)
        elif grade >= 60 and grade < 90:
            passed_list.append(name)
        else:
            failed_list.append(name)
    return {
        "excellent": excellent_list,
        "passed": passed_list,
        "failed": failed_list
    }

scores = {"Tom": 95, "Jack": 72, "Lucy": 88, "Mike": 45, "Anna": 91}
print(group_scores(scores))