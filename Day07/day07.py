import sys

def read_data (filename, cast_to_int):
    with open(filename) as f:
        if cast_to_int is True:
            data = [int(line.strip()) for line in f.readlines()]
        else:
            data = [line.strip() for line in f.readlines()]
    return data

def step_1 (data):
    poslist = [int(val) for val in data[0].split(',')]
    mincost = 999999999999
    mincostposition = -1
    for pos in range(max(poslist)+1):
        poscost = 0
        for crab in poslist:
            poscost += abs(crab-pos)
        if poscost < mincost:
            mincostposition = pos
            mincost = poscost            
    return '{} @ {}'.format(mincost, mincostposition)

def step_2 (data):
    poslist = [int(val) for val in data[0].split(',')]
    mincost = 999999999999
    mincostposition = -1
    for pos in range(max(poslist)+1):
        poscost = 0
        for crab in poslist:
            distance = abs(crab-pos)
            poscost += (distance + 1) * (distance * .5)
        if poscost < mincost:
            mincostposition = pos
            mincost = poscost            
    return '{} @ {}'.format(mincost, mincostposition)  

if __name__ == '__main__':
    data = read_data(sys.argv[1], sys.argv[3])
    results = ''
    if sys.argv[2] == '1':
        results = step_1(data)
    else:
        results = step_2(data)
    print(results) 
