def unique_devices(devices):
    new_devices = []
    for device in devices:
        if device not in new_devices:
            new_devices.append(device)
    return new_devices
    
devices = [
    "Camera_A",
    "Camera_B",
    "Camera_A",
    "Camera_C",
    "Camera_B"
]
print(unique_devices(devices))