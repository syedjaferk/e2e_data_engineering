def read_lines(path):
    print("  (opening file)")
    with open(path) as f:
        next(f)  # skip the header
        for line in f:
            yield line.rstrip("\n")


lines = read_lines("data/orders.csv")
print(lines)
# print(type(lines).__name__)  # nothing has run yet: no "(opening file)"
# print(next(lines))
# print(next(lines))

for line in lines:
    print(line)
