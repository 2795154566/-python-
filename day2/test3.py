"""
    编写函数 analyze_scores(scores)，完成两项任务：
    1. 找出所有成绩大于等于 60 分的学生，保存为新字典。
    2. 计算及格学生的平均分，保留两位小数。
"""

def analyze_scores(scores):
    new_dict = {}
    sum = 0
    count = 0
    for name,score in scores.items():
        if score >= 60:
            new_dict[name] = score
            sum += score
            count = count + 1
    if count == 0:
        return {
                    "passed": {
                        },
                    "average": 0.0
                }
    else:
        return{
            "passed": new_dict,
            "average": round(total, 2) # sum / count,需要保留两位小数
        }

scores = {
    "Tom": 85,
    "Jack": 55,
    "Lucy": 92,
    "Mike": 40,
    "Anna": 78
}
analyze_scores(scores)
