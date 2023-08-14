import platform
import psutil

def get_cpu_info():
    cpu_info = {}
    cpu_info["Brand"] = platform.processor()
    cpu_info["Cores"] = psutil.cpu_count(logical=False)
    cpu_info["Threads"] = psutil.cpu_count(logical=True)
    return cpu_info

def get_memory_info():
    virtual_memory = psutil.virtual_memory()
    memory_info = {
        "Total": virtual_memory.total,
        "Available": virtual_memory.available,
        "Used": virtual_memory.used,
        "Free": virtual_memory.free
    }
    return memory_info

def get_disk_info():
    disk_info = []
    partitions = psutil.disk_partitions()
    for partition in partitions:
        partition_info = {}
        partition_info["Device"] = partition.device
        partition_info["Mount Point"] = partition.mountpoint
        partition_info["File System"] = partition.fstype
        partition_info["Total Size"] = psutil.disk_usage(partition.mountpoint).total
        partition_info["Used Space"] = psutil.disk_usage(partition.mountpoint).used
        partition_info["Free Space"] = psutil.disk_usage(partition.mountpoint).free
        disk_info.append(partition_info)
    return disk_info

def main():
    print("CPU Information:")
    cpu_info = get_cpu_info()
    for key, value in cpu_info.items():
        print(f"{key}: {value}")
    
    print("\nMemory Information:")
    memory_info = get_memory_info()
    for key, value in memory_info.items():
        print(f"{key}: {value} bytes")
    
    print("\nDisk Information:")
    disk_info = get_disk_info()
    for partition in disk_info:
        print("Partition:")
        for key, value in partition.items():
            print(f"  {key}: {value} bytes")

if __name__ == "__main__":
    main()
