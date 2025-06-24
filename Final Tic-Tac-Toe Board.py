board = [
    [".", ".","."], 
    [".", ".","."],
    [".", ".","."]
]

def printBoard(grid): 
    for row in grid: 
        print("|", end = "")
        for number in row: 
            print(number, end = "|")
        print() 

def checkWinner(current_player, grid): 
    #Row Victory 
    for i in range(len(grid)):  
        if grid[i][0] == grid[i][1] == grid[i][2] == current_player: 
            print(f"Player {current_player} wins!") 
            return True 

    #Left Diagonal Victory 
    if grid[0][0] == grid[1][1] == grid[2][2] == current_player: 
        print(f"Player {current_player} wins!") 
        return True 

    #Right Diagonal Victory 
    if grid[0][2] == grid[1][1] == grid[2][0] == current_player: 
        print(f"Player {current_player} wins!")
        return True 

    #Column Victory 
    for i in range(len(board)): 
        if grid[0][i] == grid[1][i] == grid[2][i] == current_player: 
            print(f"Player {current_player} wins!") 
            return True 
        
def switchPlayer(current_player): 
    if current_player == "X": 
        return "O"
    if current_player == "O": 
        return "X"

def main(): 
    board = [
    [".", ".","."], 
    [".", ".","."],
    [".", ".","."]
    ] 
    player = "O"
    check = True 

    while check == True: 
        print(f"{player}'s turn")
        printBoard(board)
        row = int(input("Enter the row you want to place your piece: "))
        col = int(input("Enter the column you want to place your piece:"))
        board[row][col] = player 
        if checkWinner(player, board) == True: 
            printBoard(board)
            check = False 
        player = switchPlayer(player)     
main()  