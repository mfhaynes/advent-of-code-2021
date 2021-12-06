import sys

def read_data (filename, cast_to_int):
    with open(filename) as f:
        if cast_to_int is True:
            data = [int(line.strip()) for line in f.readlines()]
        else:
            data = [line.strip() for line in f.readlines()]
    return data

def step_1 (data):
    reading_count = len(data)
    all_data = [[int(bitval) for bitval in list(reading)] for reading in data]
    column_sums = [sum([row[column] for row in all_data]) for column in range(len(all_data[0]))]
    gamma = []
    epsilon = []
    for value in column_sums:
        if value > reading_count*.5:
            gamma.append('1')
            epsilon.append('0')
        else:
            gamma.append('0')
            epsilon.append('1')
    gamma_decimal = int(''.join(gamma),2)
    epsilon_decimal = int(''.join(epsilon),2)    
    return gamma_decimal*epsilon_decimal

def step_2_filter(column, data, variant):
    column_sum = sum([row[column] for row in data])
    majority_threshold = len(data)*.5
    if variant == 'CO2':
        if column_sum < majority_threshold:
            filter_value = 1
        else:
            filter_value = 0
    else:        
        if column_sum >= majority_threshold:
            filter_value = 1
        else:
            filter_value = 0
    return [row for row in data if row[column] == filter_value]    

def step_2 (data):
    all_data = [[int(bitval) for bitval in list(reading)] for reading in data]
    filtered_o2_data = list(all_data)
    filtered_co2_data = list(all_data)
    for column in range(len(all_data[0])):
        if len(filtered_o2_data) > 1:    
            filtered_o2_data = step_2_filter(column, filtered_o2_data, 'O2')
        if len(filtered_co2_data) > 1:     
            filtered_co2_data = step_2_filter(column, filtered_co2_data, 'CO2')
    o2_decimal = int(''.join([str(bitval) for bitval in filtered_o2_data[0]]),2)
    co2_decimal = int(''.join([str(bitval) for bitval in filtered_co2_data[0]]),2)          
    return o2_decimal*co2_decimal

if __name__ == '__main__':
    data = read_data(sys.argv[1], sys.argv[3])
    results = ''
    if sys.argv[2] == '1':
        results = step_1(data)
    else:
        results = step_2(data)
    print(results) 
