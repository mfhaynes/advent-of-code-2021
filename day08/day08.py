import sys

def read_data (filename, cast_to_int):
    with open(filename) as f:
        if cast_to_int is True:
            data = [int(line.strip()) for line in f.readlines()]
        else:
            data = [line.strip() for line in f.readlines()]
    return data

def step_1 (data):
    characters = ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']
    counter = 0
    translated_output = []
    for row in data:
        output = row.split(' | ')[1].split()
        translated_output.append(['X', 'X', 'X', 'X'])
        digit_counter = 0
        for digit in output:
            possibles = [unknown for unknown in range(len(characters)) if len(characters[unknown]) == len(digit)]
            if len(possibles) == 1:
                translated_output[counter][digit_counter] = possibles[0]
            digit_counter = digit_counter + 1
        counter = counter + 1
    print(translated_output)
    digit_count = sum([len([character for character in reading if isinstance(character,int)]) for reading in translated_output])
    return digit_count

def step_2 (data):
    characters = ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']
    mappings = {}
    total_values = 0
    for row in data:
        output = row.split(' | ')[0].split()
        twosig = [list(reading) for reading in output if len(reading) == 2]
        mappings['c'] = twosig[0]
        mappings['f'] = twosig[0]
        threesig = [list(reading) for reading in output if len(reading) == 3]
        mappings['a'] = [signal for signal in threesig[0] if signal not in twosig[0]]
        foursig = [list(reading) for reading in output if len(reading) == 4]
        mappings['b'] = [signal for signal in foursig[0] if signal not in twosig[0]]
        mappings['d'] = [signal for signal in foursig[0] if signal not in twosig[0]]
        fivesig = [list(reading) for reading in output if len(reading) == 5]
        newchars = [[value for value in signal if value not in twosig[0] and value not in threesig[0] and value not in foursig[0]] for signal in fivesig]
        mappings['g'] = list(set.intersection(*map(set, newchars)))
        mappings['e'] = [result for result in [[value for value in valuelist if value not in mappings['g']] for valuelist in newchars] if len(result) > 0][0]
        for value in [signal for signal in fivesig if mappings['e'][0] in signal][0]:
            if value in mappings['c']:
                mappings['c'] = value
        mappings['f'] = [char for char in mappings['f'] if char != mappings['c']][0]
        allfives = list(set.intersection(*map(set, fivesig)))
        mappings['d'] = [char for char in mappings['d'] if char in allfives][0]
        mappings['b'] = [char for char in mappings['b'] if char != mappings['d']][0]
        mappings['a'] = mappings['a'][0]
        mappings['g'] = mappings['g'][0]
        mappings['e'] = mappings['e'][0]
        inverted_mappings = {}
        for key in mappings.keys():
            inverted_mappings[mappings[key]] = key        
        readings = row.split(' | ')[1].split()
        power = 1000
        value = 0
        for reading in readings:
            translated_char = ''.join(sorted([inverted_mappings[char] for char in reading]))
            pos = [unknown for unknown in range(len(characters)) if characters[unknown] == translated_char]
            value = value + (pos[0]*power)
            power = power/10
        total_values = total_values + value   
    return total_values 

if __name__ == '__main__':
    data = read_data(sys.argv[1], sys.argv[3])
    results = ''
    if sys.argv[2] == '1':
        results = step_1(data)
    else:
        results = step_2(data)
    print(results) 
