import shutil

def check_disk_usage():
    total, used, free = shutil.disk_usage("/")
    print(f"Total: {total // (2**30)} GB")
    print(f"Used: {used // (2**30)} GB")
    print(f"Free: {free // (2**30)} GB")
    print(f"Usage: {used / total * 100:.2f}%")

if __name__ == "__main__":
    check_disk_usage()
