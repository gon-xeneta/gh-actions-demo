import time

lines = 100_000_000

file_path = "/tmp/etcd/file.txt"
# file_path = "./file.txt"

start = time.time()
with open(file_path, 'w') as f:
    for i in range(lines):
        f.write('readme')
end = time.time()
elapsed = end - start
print(elapsed)
