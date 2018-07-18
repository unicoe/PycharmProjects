l = []

file = open('/home/user/Downloads/save_file.txt')

while 1:
    line = file.readline()
    if line != '\n':
        print line.replace("\n", "")
        l.append(line.replace("\n",""))
    if not line:
        break

print l
