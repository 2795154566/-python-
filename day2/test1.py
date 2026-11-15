"""
编写函数 update_user(user)，接收一个用户信息字典，完成以下操作：
1. 将 age 增加 1。
2. 新增 status 字段，值为 "active"。
3. 删除 password 字段（如果不存在，不允许报错）。
4. 返回修改后的字典。
"""

def update_user(user):
    user["age"] = user.get("age", 0) + 1
    user["status"] = "active"
    if "password" in user:
        del user["password"]
    else:
        pass
    return user

user = {
    "name": "Tom",
    "age": 22,
    "password": "123456"
}
result = update_user(user)
print(result)