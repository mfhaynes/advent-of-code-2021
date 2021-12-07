import sys

def read_data (filename, cast_to_int):
    with open(filename) as f:
        if cast_to_int is True:
            data = [int(line.strip()) for line in f.readlines()]
        else:
            data = [line.strip() for line in f.readlines()]
    return data

class Coordinate(object):

    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

def step_1 (data):
    danger_zones = 0
    grid_size = 1000
    grid = [[0 for x in range(grid_size)] for y in range(grid_size)]
    for row in data:
        parsed_data = row.split()
        parsed_coord1 = parsed_data[0].split(',')
        parsed_coord2 = parsed_data[2].split(',')
        coord1 = Coordinate(parsed_coord1[0], parsed_coord1[1])
        coord2 = Coordinate(parsed_coord2[0], parsed_coord2[1])
        if coord1.x == coord2.x:
            y_range = [coord1.y, coord2.y]
            y_range.sort()
            for y in range(y_range[0],y_range[1]+1):
                grid[y][coord1.x] += 1
        if coord1.y == coord2.y:
            x_range = [coord1.x, coord2.x]
            x_range.sort()
            for x in range(x_range[0],x_range[1]+1):
                grid[coord1.y][x] += 1                  
    for row in grid:
        danger_zones += len([column for column in row if column > 1])
    return danger_zones

def step_2 (data):
    danger_zones = 0
    grid_size = 1000
    grid = [[0 for x in range(grid_size)] for y in range(grid_size)]
    for row in data:
        parsed_data = row.split()
        parsed_coord1 = parsed_data[0].split(',')
        parsed_coord2 = parsed_data[2].split(',')
        if int(parsed_coord1[0]) < int(parsed_coord2[0]):
            coord1 = Coordinate(parsed_coord1[0], parsed_coord1[1])
            coord2 = Coordinate(parsed_coord2[0], parsed_coord2[1])
        else:
            coord1 = Coordinate(parsed_coord2[0], parsed_coord2[1])
            coord2 = Coordinate(parsed_coord1[0], parsed_coord1[1])       
        if coord1.x == coord2.x:
            y_range = [coord1.y, coord2.y]
            y_range.sort()
            for y in range(y_range[0],y_range[1]+1):
                grid[y][coord1.x] += 1
        elif coord1.y == coord2.y:
            x_range = [coord1.x, coord2.x]
            x_range.sort()
            for x in range(x_range[0],x_range[1]+1):
                grid[coord1.y][x] += 1
        else:
            length = abs(coord2.x - coord1.x)
            if (coord1.x - coord2.x > 0 and coord1.y - coord2.y > 0) or (coord1.x - coord2.x < 0 and coord1.y - coord2.y < 0):
                slope = 1
            else:
                slope = -1
            for offset in range(length+1):
                    #print(coord1.y + (slope * offset))
                    #print(coord1.x + offset)
                    grid[coord1.y + (slope * offset)][coord1.x + offset] += 1               
    for row in grid:
        danger_zones += len([column for column in row if column > 1])
    return danger_zones

if __name__ == '__main__':
    data = read_data(sys.argv[1], sys.argv[3])
    results = ''
    if sys.argv[2] == '1':
        results = step_1(data)
    else:
        results = step_2(data)
    print(results) 
