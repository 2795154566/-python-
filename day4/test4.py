"""
要求：
1. 如果 code 不等于 200 或缺失，返回 {"success": False, "valid_codes": []}。
2. 状态码正常时，从 data.qr_codes 中提取符合条件的二维码内容。
3. 只有 text 非空字符串，且 confidence >= min_confidence 时才算有效。
4. data 或 qr_codes 缺失时，按空列表处理。
5. confidence 缺失或为 None 时，忽略该条记录。
6. 返回统一格式，success 只表示接口状态码是否正常，不表示是否识别到了二维码。
"""

def validate_qr_response(response, min_confidence=0.8):
    result_list = []
    if "code" not in response or response.get("code") != 200 :
        return {"success": False, "valid_codes": []} 
    else:
        if "data" not in response or "qr_codes" not in response["data"]:
            return {"success": True, "valid_codes": []} 
        else:
            tmp_list = response["data"]["qr_codes"]
            for qr_code in tmp_list:
                if "confidence" not in qr_code or qr_code["confidence"] == None:
                    continue
                if qr_code["text"] != "" and qr_code["confidence"] >= min_confidence:
                    result_list.append(qr_code["text"])
    return {
        "success": True,
        "valid_codes": result_list
    }




response = {
    "code": 200,
    "data": {
        "qr_codes": [
            {"text": "ABC123", "confidence": 0.95},
            {"text": "XYZ789", "confidence": 0.72},
            {"text": "TEST001", "confidence": 0.88}
        ]
    }
}
print(validate_qr_response(response))