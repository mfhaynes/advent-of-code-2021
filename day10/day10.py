import sys
import statistics

def read_data (filename, cast_to_int):
    with open(filename) as f:
        if cast_to_int is True:
            data = [int(line.strip()) for line in f.readlines()]
        else:
            data = [line.strip() for line in f.readlines()]
    return data

def evaluate_row(row):
    openers = {'(': ')', '[': ']', '{': '}', '<': '>'}
    closers = {')': 3, ']': 57, '}': 1197, '>': 25137}
    score = 0
    open_stack = []
    for char in row:   
        if char in openers.keys():
            open_stack.append(char)
        else:
            if char != openers[open_stack.pop()]:
               score = closers[char]
               break
    return score, open_stack           
                    
def step_1 (data):
    return sum([evaluate_row(row)[0] for row in data])

def step_2 (data):
    openers = {'(': ')', '[': ']', '{': '}', '<': '>'}
    closers = {')': 1, ']': 2, '}': 3, '>': 4}
    scores = []
    for row in data:
        score = 0
        corruption_score, return_stack = evaluate_row(row)
        while len(return_stack) > 0 and corruption_score == 0:
            score *= 5
            score += closers[openers[return_stack.pop()]]
        if score > 0:
            scores.append(score)
    return statistics.median(scores)  

if __name__ == '__main__':
    data = read_data(sys.argv[1], sys.argv[3])
    results = ''
    if sys.argv[2] == '1':
        results = step_1(data)
    else:
        results = step_2(data)
    print(results) 
