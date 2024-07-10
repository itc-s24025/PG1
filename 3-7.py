with open("sample.txt",'r') as f:
    line = f.readline()
    print(line)

with open("sample.txt",'r') as f:
    lines = f.readlines()
    print(lines)

with open('sample2.txt','w') as f:
    f.write('test')

with open('sample2.txt','a') as f:
    f.write('test2')

with open('sample.txt', 'r') as f:
    for line in f:
        print(line.strip())
'''
with open('number.txt','r') as f:
    sum = 0
    for data in f:
        num = int(data)
        sum += num
    print(sum)
'''    
