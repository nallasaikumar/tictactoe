import random
board = [['_','_','_'], ['_','_','_'], ['_','_','_']]

#First Player  - 'x'
#Second Player  - 'o'

player_one = random.choice(['Player 1', 'Player 2'])    
print(f'{player_one} is going first')
player_two = list({'Player 1', 'Player 2'} - {player_one})[0]

# 1 2 3 4 5 6 7 8 9 turns
# x o x o x o x o x

# first person  - x  odd turn
# second person - o  even turn

index = 1
first_player = 0
second_player = 0
result = []

while index <= 9:
    
    pos = int(input('\nEnter the position 1 to 9 : '))

    count = 0
    
    #To get to the position and insert the symbol
    for list_ in range(len(board)):                           #outer loop        
        for letter in range(len(board[list_])):               #inner loop 
            count = count + 1
            if count == pos:
                if index%2 != 0:  #odd turn
                    sym = 'x'
                else:
                    sym = 'o'
                board[list_][letter] = sym
                index = index + 1
    
    #To check if we won
    #Rows appended
    for i in board:
        result.append(i)

    #Columns 
    j = 0
    while j < 3:
        res = []
        for i in range(0,3):
            res.append(board[i][j])
        j = j + 1
        result.append(res)

    # One diagnol
    res = []
    for i in range(0,3):
        res.append(board[i][i])
    result.append(res)

    #second diagnol
    l = [3,5,7]
    j = 2
    for i in range(0,3):
        if count in l:
            res.append(board[i][j])
            j = j - 1
    result.append(res)
    
#     print('Result ', result)
    
    for i in result:
        if i == ['x', 'x', 'x']:
            first_player = 1
            break
        elif i == ['o', 'o', 'o']:
            second_player = 1
            break
        
    #To print the board            
    for lis in board:
        print(' '*25, end = '')
        for j in lis:
            print(j, end = ' ')
        print()
        
    if first_player == 1 or second_player == 1:
        break
        
if first_player == 1:
    print(f'{player_one} won the match! Congrats!')
elif second_player == 1:
    print(f'{player_two} won the match! Congrats!')
else:
    print('Match Draw!')
          
