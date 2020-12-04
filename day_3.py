f = open("day_3.txt", "r")
lines = f.readlines()

hor_pos = 0
ver_pos = 0

land = '.'
tree = '#'

count_trees = 0
for pos_line,_ in enumerate(lines):
    line=lines[ver_pos]
    line=line.replace('\n','')
    if len(line) > hor_pos:
        diff = hor_pos-len(line)
        hor_pos = diff
        ver_pos += 1
    if line[hor_pos] == tree:
        count_trees += 1
    hor_pos += 3

print(count_trees)