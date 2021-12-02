import sys

def read_data (filename, cast_to_int):
    with open(filename) as f:
        if cast_to_int is True:
            data = [int(line.strip()) for line in f.readlines()]
        else:
            data = [line.strip() for line in f.readlines()]
    return data

def step_1 (data):
    place = 1
    down_counter = 0
    for reading in data[1:]:
        if reading > data[place-1]:
            down_counter = down_counter + 1
        place = place + 1
    return down_counter

def step_2 (data):
    place = 3
    down_counter = 0
    for reading in data[3:]:
        if sum(data[place-2:place+1]) > sum(data[place-3:place]):
            down_counter = down_counter + 1
        place = place + 1    
    return down_counter     

if __name__ == '__main__':
    data = read_data(sys.argv[1], True)
    results = ''
    if sys.argv[2] == '1':
        results = step_1(data)
    else:
        results = step_2(data)
    print(results) 
