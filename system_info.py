import psutil


def cpu_usage():
    return psutil.cpu_percent(interval=1)


def ram_usage():
    memory = psutil.virtual_memory()
    return memory.percent


def battery():
    battery = psutil.sensors_battery()

    if battery:
        return battery.percent

    return None


def disk_usage():
    disk = psutil.disk_usage("/")
    return disk.percent