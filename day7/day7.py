from collections import defaultdict

with open("input.in") as f:
    commands = f.readlines()

sizes = defaultdict(int)
stack = []

i = 0
for c in commands:
    if c.startswith("$ ls") or c.startswith("dir"):
        continue
    if c.startswith("$ cd"):
        dest = c.split()[2]
        if dest == "..":
            stack.pop()
        else:
            i += 1
            path = f"{stack[-1]}_{dest}" if stack else dest
            stack.append(path)
    else:
        size, file = c.split()
        for path in stack:
            sizes[path] += int(size)

needed_size = 30000000 - (70000000 - sizes["/"])
for size in sorted(sizes.values()):
    if size > needed_size:
        break

print(sum(n for n in sizes.values() if n <= 100000)) # task 1
print(size) # task 2

# credit to  @silentw0lf silentw0lf 07