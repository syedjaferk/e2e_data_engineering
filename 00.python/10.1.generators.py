def normal_read_lines(path):
    print("  (opening file)")
    lines = []
    with open(path) as f:
        next(f)  # skip the header
        for line in f:
            lines.append(line.rstrip("\n"))
    return lines


lines = normal_read_lines("data/orders.csv")

print("Lines ", lines)

for line in lines:
    print(line)
