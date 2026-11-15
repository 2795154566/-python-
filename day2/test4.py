"""
    编写函数 check_devices(response)，实现：
    1. 判断 code 是否等于 200。
    2. 如果状态码异常，返回 {"success": False, "online_devices": []}。
    3. 如果状态码正常，提取所有 online 为 True 的设备名称。
    4. 如果 data 或 devices 字段缺失，按空设备列表处理。
    5. 返回统一格式的字典。
    约束：假设 devices 存在时一定是列表，列表中的元素都是字典；设备的 name、online 字段可能缺失。
         只有 online is True 且存在 name 的设备才加入结果。
    提示：使用 get() 安全读取嵌套字典，并结合 for 循环处理列表。
"""
def check_devices(response):
    online_devices = []
    if response["code"] != 200:
        return {"success": False, "online_devices": []}
    else:
        if "data" not in response or "devices" not in response["data"]:
            return {"success": True, "online_devices": []}
        else:
            for device in response["data"]["devices"]:
                if device["online"] == True and "name" in device:  #修改后：if device.get("online") is True and "name" in device:
                    online_devices.append(device["name"])
            return {"success": True, "online_devices": online_devices}
response = {
    "code": 200,
    "message": "success",
    "data": {
        "devices": [
            {"id": 1, "name": "Camera_A", "online": True},
            {"id": 2, "name": "Camera_B", "online": False},
            {"id": 3, "name": "Camera_C", "online": True}
        ]
    }
}

check_devices(response)