"""
编写函数 merge_config(default_config, user_config)，将用户配置合并到默认配置中。

要求：
- 以 default_config 为基础。
- 如果两个字典存在相同的键，使用 user_config 中的值。
- 不允许修改传入的两个原始字典。
- 返回合并后的新字典。
"""

def merge_config(default_config, user_config):
    result_config = user_config.copy()
    for d_key, d_value in default_config.items():
        if d_key not in user_config:
            result_config[d_key] = d_value
    return result_config

default_config = {
    "timeout": 2,
    "retry": 3,
    "debug": False
}

user_config = {
    "timeout": 5,
    "debug": True
}

print(merge_config(default_config, user_config))