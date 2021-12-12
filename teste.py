lines = ['Readme', 'aaa']

with open('readme.txt', 'a') as f:
        for line in lines:
                f.write(line)
                f.write('\n')
        f.close()
