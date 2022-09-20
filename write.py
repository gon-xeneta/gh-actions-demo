import time

lines = 10_000_000

file_path = "/tmp/etcd/file.txt"

start = time.time()
with open(file_path, 'w') as f:
    for i in range(lines):
        f.write('readme')
end = time.time()
elapsed = end - start
print(elapsed)
