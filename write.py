import time
from tempfile import mkdtemp
import os

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
    return elapsed

ram_disk_filepath = "/tmp/ramdisk/file.txt"
temp_path = mkdtemp()
disk_filepath = f"{temp_path}/file"

test_count = 10

ramdisk_score = 0
disk_score = 0

for i in range(test_count):
    rmdsk_file = f"{ram_disk_filepath}"
    dsk_file = f"{disk_filepath}"

    rmdsk = write_file(rmdsk_file, "Write to ramdisk     ")
    dsk = write_file(dsk_file, "Write to regular disk")

    os.remove(rmdsk_file)
    os.remove(dsk_file)

    if rmdsk < dsk:
        ramdisk_score += 1
        print("Ramdisk point")
    elif dsk < rmdsk:
        disk_score += 1
        print("Regular disk point")

print("******************************")
if ramdisk_score > disk_score:
    print(f"Ramdisk is faster: {ramdisk_score} - {disk_score}")
elif disk_score > ramdisk_score:
    print(f"Regular disk is faster: {disk_score} - {ramdisk_score}")
else:
    print("Doesn't really matter")
