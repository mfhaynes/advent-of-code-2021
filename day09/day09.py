import sys

def read_data (filename, cast_to_int):
    with open(filename) as f:
        if cast_to_int is True:
            data = [int(line.strip()) for line in f.readlines()]
        else:
            data = [line.strip() for line in f.readlines()]
    return data

def step_1 (data):
    dataheight = len(data)
    datawidth = len(data[0])
    lowpoints = []
    for rownum in range(dataheight):
        for colnum in range(datawidth):
            if ((colnum > 0 and data[rownum][colnum] < data[rownum][colnum-1]) or colnum == 0) \
            and ((colnum < datawidth-1 and data[rownum][colnum] < data[rownum][colnum+1]) or colnum == datawidth-1) \
            and ((rownum > 0 and data[rownum][colnum] < data[rownum-1][colnum]) or rownum == 0) \
            and ((rownum < dataheight-1 and data[rownum][colnum] < data[rownum+1][colnum]) or rownum == dataheight-1):
               lowpoints.append(int(data[rownum][colnum]))
    return sum(lowpoints)+len(lowpoints)

def find_basin_neighbors(data, basin, current_point):
    dataheight = len(data)
    datawidth = len(data[0])
    rownum, colnum = current_point
    neighbors = [point for point in [(rownum-1, colnum), (rownum, colnum-1), (rownum, colnum+1), (rownum+1, colnum)] if point[0] >= 0 and point[0] <= dataheight-1 and point[1] >= 0 and point[1] <= datawidth-1]
    basin_adds = [neighbor for neighbor in neighbors if neighbor not in basin and data[neighbor[0]][neighbor[1]] != '9']
    return basin_adds

def find_basin(data, current_point):
    basin = []
    basin_adds = [current_point]
    while len(basin_adds) > 0:
        new_basin_adds = []
        for point in basin_adds:
            basin.append(point)
            new_basin_adds += find_basin_neighbors(data, basin, point)
            basin_adds = new_basin_adds
    return basin    
        
def step_2 (data):
    dataheight = len(data)
    datawidth = len(data[0])
    lowpoints = []
    for rownum in range(dataheight):
        for colnum in range(datawidth):
            if ((colnum > 0 and data[rownum][colnum] < data[rownum][colnum-1]) or colnum == 0) \
            and ((colnum < datawidth-1 and data[rownum][colnum] < data[rownum][colnum+1]) or colnum == datawidth-1) \
            and ((rownum > 0 and data[rownum][colnum] < data[rownum-1][colnum]) or rownum == 0) \
            and ((rownum < dataheight-1 and data[rownum][colnum] < data[rownum+1][colnum]) or rownum == dataheight-1):
               lowpoints.append((rownum,colnum))
    basin_sizes = []        
    for lowpoint in lowpoints:
        basin = find_basin(data, lowpoint)
        basin_sizes.append(len(set(basin)))
    overall = 1
    for basin_size in sorted(basin_sizes, reverse=True)[0:3]:
        overall = overall * basin_size
    return overall   

if __name__ == '__main__':
    data = read_data(sys.argv[1], sys.argv[3])
    results = ''
    if sys.argv[2] == '1':
        results = step_1(data)
    else:
        results = step_2(data)
    print(results) 
