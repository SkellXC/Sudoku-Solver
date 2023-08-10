from time import time

method_of_entry = input("The default method for entering your sudoku board is by submitting a screenshot (not yet done). Would you like to manually it in instead? If so, type 'yes'. Otherwise, press enter.\n")

if method_of_entry.lower() == "yes":

    print("[+] A GUI should have opened by now")
    import gui

    board = gui.getBoard()
else:
    

    board = [
        [7,8,0,4,0,0,1,2,0],
        [6,0,0,0,7,5,0,0,9],
        [0,0,0,6,0,1,0,7,8],
        [0,0,7,0,4,0,2,6,0],
        [0,0,1,0,5,0,9,3,0],
        [9,0,4,0,6,0,0,0,5],
        [0,7,0,3,0,0,0,1,2],
        [1,2,0,0,0,7,4,0,0],
        [0,4,9,2,0,6,0,0,7]
    ]




def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

#find solution, if it works, go to the next, else go back
#log all numbers in areas, then when getting solutions, just check if its in the list. If its not, go to the next one
def solutions(board,pos,attempt):
    xpos = pos[0]
    ypos = pos[1]
    num = []
    #pos is the position of the current item
    for i in range(0,9):#Gets the numbers from column
        if board[xpos][i] != 0:#if not empty
            num.append(board[xpos][i])

    for a in range(0,9):
        if board[a][ypos] != 0:
            num.append(board[a][ypos])
    
    square_pos = xpos//3,ypos//3
    #print(square_pos)#might be y,x instead of x,y
    new_x = square_pos[0]*3
    new_y = square_pos[1]*3

    for i in range(0,3):#times by three and then add one each time
        
        for a in range(0,3):
            #print(f"new_x = {new_x}")
            #print(f"new_y = {new_y}")
            #print(f"{new_x+1},{new_y+1}")
            num.append(board[new_x][new_y])
            new_x+=1
        new_x = square_pos[0]*3#This is here because the x coord keeps getting bigger
        new_y +=1
    num = list(set(num))
    num.remove(0)
    #print(num)
    if attempt in num:
        return False
    else:
        return True
    #return num

def solve(board):
    if not getEmpty(board):
        return True
    else:
        row,col = getEmpty(board)
    for i in range(1,10):#Goes from numbers 1-9 instead of 0-8 (if i entered 0,9)
        if solutions(board,(getEmpty(board)),i):#board,pos,attempt
            #print(f"{temp}=temp")
            board[row][col] = i
            #print(f"Here! {board[row][col]}")
            if solve(board):
                return True
            board[row][col] = 0
    #print_board(board)
    return False


def getEmpty(board):
    for i in range(len(board)):
        for a in range(len(board)):
            if board[i][a] == 0:
                #print(f"I = {i}")
                return (i,a)
    #print("Returning False at getEmpty!")
    #print("Complete!")
    return False

print("Initial board:\n")
print_board(board)
print("Hard grids can take up to 15 seconds to solve.")
#solutions(board,(6,4),5)
start = time()
solve(board)
end = time()
print("Solved board:\n")
print_board(board)
time = end-start

print(f"Solved in {round(end-start,2)} seconds")
