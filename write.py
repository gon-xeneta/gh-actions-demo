import time


def write_file(filepath, additional_message=None):
    lines = 100_000_000

    start = time.time()
    with open(filepath, 'w') as f:
        for i in range(lines):
            f.write('readme')
    end = time.time()
    elapsed = end - start
    if additional_message is not None:
        additional_message += " "
    print(f"{additional_message}{elapsed}")

ram_disk_filepath = "/tmp/etcd/file.txt"
disk_filepath = "./file.txt"

write_file(ram_disk_filepath, "Write to ramdisk")
write_file(disk_filepath, "Write to regular disk")
