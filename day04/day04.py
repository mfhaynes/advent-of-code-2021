import sys

def read_data (filename, cast_to_int):
    with open(filename) as f:
        if cast_to_int is True:
            data = [int(line.strip()) for line in f.readlines()]
        else:
            data = [line.strip() for line in f.readlines()]
    return data

def convert_list_to_ints (data):
    return [int(val) for val in data]

def parse_data (data):
    draws = convert_list_to_ints(data[0].split(','))
    start_row = 2
    boards = []
    pivoted_boards = []
    winning_board = []
    while start_row + 5 <= len(data):
        new_board = [convert_list_to_ints(row.split()) for row in data[start_row:start_row+5]]
        boards.append(new_board)
        pivoted_boards.append([[row[column] for row in new_board] for column in range(len(new_board[0]))])
        start_row = start_row + 6
    return draws, boards, pivoted_boards
    
def check_victory (boards):    
    winning_boards = []
    winning_board_details = []
    counter = 0
    for board in boards:
       winning_boards.append(0)
       for row in board:
           if row == []:
               winning_board_details.append(board)
               winning_boards[counter] = 1
               break
       counter = counter + 1       
    return winning_boards, winning_board_details
    
def mark_boards (boards, draw):    
    return [[[column for column in row if column != draw] for row in board] for board in boards]
    
def step_1 (data):
    draws, boards, pivoted_boards = parse_data(data)
    for draw in draws:
        boards = mark_boards(boards, draw)
        pivoted_boards = mark_boards(pivoted_boards, draw)
        winning_boards = check_victory(boards)[1]
        if winning_boards != []:
            break
        else:
            winning_boards = check_victory(pivoted_boards)[1]
        if winning_boards != []:
            break                                   
    return draw*sum([sum(row) for row in (winning_boards)[0]])

def step_2 (data):
    draws, boards, pivoted_boards = parse_data(data)
    board_count = len(boards)
    losing_boards = []
    for draw in draws:
        previous_losing_boards = list(losing_boards)
        boards = mark_boards(boards, draw)
        pivoted_boards = mark_boards(pivoted_boards, draw)
        winning_boards, winning_board_details = check_victory(boards)
        winning_pivoted_boards, winning_pivoted_board_details = check_victory(pivoted_boards)
        losing_boards = [boards[counter] for counter in range(len(boards)) if winning_boards[counter] + winning_pivoted_boards[counter] == 0]
        if losing_boards == []:
            break
    return draw*sum([sum([value for value in row if value != draw]) for row in previous_losing_boards[0]])  

if __name__ == '__main__':
    data = read_data(sys.argv[1], sys.argv[3])
    results = ''
    if sys.argv[2] == '1':
        results = step_1(data)
    else:
        results = step_2(data)
    print(results) 
