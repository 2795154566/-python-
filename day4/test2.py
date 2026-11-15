def extract_errors(logs):
    error_list = []
    for log in logs:
        if log.startswith("ERROR:"):
            tmp = log.split(":",1)[-1].strip()
            if tmp != '':
                error_list.append(tmp)

    return error_list


logs = [
    "INFO: Device connected",
    "ERROR: Camera timeout",
    "ERROR: ",
    "WARNING: Low memory",
    "ERROR: SDK initialization failed",
    "INFO: Test completed"
]
print(extract_errors(logs))