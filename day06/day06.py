import sys
from datetime import datetime

def read_data (filename, cast_to_int):
    with open(filename) as f:
        if cast_to_int is True:
            data = [int(line.strip()) for line in f.readlines()]
        else:
            data = [line.strip() for line in f.readlines()]
    return data

def update_fish (days):
    if days == 0:
        return 6
    else:
        return days-1

def step_1 (data):
    max_days = 80
    population = [int(value) for value in data[0].split(',')]
    for day in range(max_days):
        births = len([value for value in population if value == 0])
        population = [update_fish(value) for value in population]
        for birth in range(births):
            population.append(8)
        print('Day {} @ {} - {} fish'.format(day, datetime.now(), len(population)))
    return len(population)

def step_2 (data):
    all_fish = [int(val) for val in data[0].split(',')]
    max_days = 256
    progeny_factors = {}
    population = {0:0, 1: 1, 2: 0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}
    for day in range(max_days):
        new_population = {}
        # new fish
        new_population[8] = population[0]
        # bump counters down by one
        for value in range(8):
            new_population[value] = population[value+1]
        # reset zero-day counters to six            
        new_population[6] += population[0]
        population = new_population
        # set progeny factors with starting counter values 1-5.        
        if max_days - day <= 5:
            progeny_factors[max_days - day] = sum([population[key] for key in population.keys()])
    total_fish = sum([progeny_factors[fish] for fish in all_fish])  
    return total_fish   

if __name__ == '__main__':
    data = read_data(sys.argv[1], sys.argv[3])
    results = ''
    if sys.argv[2] == '1':
        results = step_1(data)
    else:
        results = step_2(data)
    print(results) 
