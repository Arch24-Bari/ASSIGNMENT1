lines = []
while True:
    line = input()
    if line == ' ':
        break
    lines.append(line)
print(lines)

butFirst = lines[0:]
print(butFirst)
eachInASeparateLine = "\n".join(butFirst)

print(eachInASeparateLine)
