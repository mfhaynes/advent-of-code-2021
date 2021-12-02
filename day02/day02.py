import sys

def read_data (filename, cast_to_int):
    with open(filename) as f:
        if cast_to_int is True:
            data = [int(line.strip()) for line in f.readlines()]
        else:
            data = [line.strip() for line in f.readlines()]
    return data

def step_1 (data):
    directions = {'forward': 0, 'down': 0, 'up': 0}
    for instruction in data:
        details = instruction.split(' ')
        directions[details[0]] += int(details[1])
    result = directions['forward'] * (directions['down'] - directions['up'])    
    return result

def step_2 (data):
    aim = 0
    forward = 0
    depth = 0
    for instruction in data:
         details = instruction.split(' ')
         if details[0] == 'up':
             aim = aim - int(details[1])
         elif details[0] == 'down':
             aim = aim + int(details[1])
         else:
             forward = forward + int(details[1])
             depth = depth + (aim * int(details[1]))
    result = forward * depth             
    return result   

if __name__ == '__main__':
    data = read_data(sys.argv[1], sys.argv[3])
    results = ''
    if sys.argv[2] == '1':
        results = step_1(data)
    else:
        results = step_2(data)
    print(results) 
