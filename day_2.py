# exercise 1
import re

f = open("day_2_1.txt", "r")
lines = f.readlines()

re_pattern = '(\d+)-(\d+) (\w): (\w+)'
re_compiled = re.compile(pattern=re_pattern)

res = 0
for a in lines:
    result = re_compiled.findall(a)
    min_times = int(result[0][0])
    max_times = int(result[0][1])
    word = result[0][2]
    passw = result[0][3]

    count = passw.count(word)

    if count >= min_times and count <= max_times:
        res += 1

print(res)


# exercise 2
import re

f = open("day_2_1.txt", "r")
lines = f.readlines()

re_pattern = '(\d+)-(\d+) (\w): (\w+)'
re_compiled = re.compile(pattern=re_pattern)

res = 0
for a in lines:
    result = re_compiled.findall(a)
    pos1 = int(result[0][0]) -1
    pos2 = int(result[0][1]) -1
    word = result[0][2]
    passw = result[0][3]

    if passw[pos1] == word:
        if passw[pos2] == word:
            continue
        else:
            res += 1
    else:
        if passw[pos2] == word:
            res += 1

print(res)