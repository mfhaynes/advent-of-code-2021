import sys

def read_data (filename):
    with open(filename) as f:
        data = [line.strip() for line in f.readlines()]
    return data

def convert_list_to_ints (data):
    return [int(val) for val in data]

def parse_data (data):
    draws = convert_list_to_ints(data[0].split(','))
    start_row = 2
    boards = []
    pivoted_boards = []
    while start_row + 5 <= len(data):
        new_board = [convert_list_to_ints(row.split()) for row in data[start_row:start_row+5]]
        boards.append(new_board)
        pivoted_boards.append([[row[column] for row in new_board] for column in range(len(new_board[0]))])
        start_row = start_row + 6
    return draws, boards, pivoted_boards
    
def mark_boards (boards, draw):    
    return [[[column for column in row if column != draw] for row in board] for board in boards]
    
def check_victory (boards):    
    winning_boards = [0 for i in range(len(boards))]
    winning_board_details = []
    for boardkey in range(len(boards)):
       for row in boards[boardkey]:
           if row == []:
               winning_board_details.append(boards[boardkey])
               winning_boards[boardkey] = 1
               break 
    return winning_boards, winning_board_details
    
def step_1 (data):
    draws, boards, pivoted_boards = parse_data(data)
    for draw in draws:
        boards = mark_boards(boards, draw)
        pivoted_boards = mark_boards(pivoted_boards, draw)
        winning_boards = check_victory(boards+pivoted_boards)[1]
        if winning_boards != []:
            break                              
    return draw*sum([sum(row) for row in winning_boards[0]])

def step_2 (data):
    draws, boards, pivoted_boards = parse_data(data)
    losing_boards = []
    for draw in draws:
        previous_losing_boards = list(losing_boards)
        boards = mark_boards(boards, draw)
        pivoted_boards = mark_boards(pivoted_boards, draw)
        winning_boards = check_victory(boards)[0]
        winning_pivoted_boards = check_victory(pivoted_boards)[0]
        losing_boards = [boards[counter] for counter in range(len(boards)) if winning_boards[counter] + winning_pivoted_boards[counter] == 0]
        if losing_boards == []:
            break
    return draw*sum([sum([value for value in row if value != draw]) for row in previous_losing_boards[0]])  

if __name__ == '__main__':
    data = read_data(sys.argv[1])
    if sys.argv[2] == '1':
        results = step_1(data)
    else:
        results = step_2(data)
    print(results) 
