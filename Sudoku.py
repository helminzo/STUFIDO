GRID_SIZE = 9

def load_sudoku_board(filename):
    f = open(f"{filename}")
    sudoku_board = []
    ctr = 0
    for line in f:
        sudoku_board.append([])
        for c in line:
            if(c != '.' and c != '\n'):
                sudoku_board[ctr].append(int(c))
            elif(c != '\n'):
                sudoku_board[ctr].append(None)
        ctr += 1
    return sudoku_board

def sudoku_solve(board):
    # SET THE CONSTRAINTS
    constraints = set() # set of constraints, where each contstraint is a set of two cells that are not equal to each other

    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            # Add column constraint
            for x in range(i+1, GRID_SIZE):
                constraints.add(((i, j), (x, j)))

                # Add row constraint
            for x in range(j+1, GRID_SIZE):
                constraints.add(((i, j), (i, x)))
            
            # add square constraint
            for x in range(3*(i//3), 3*(i//3+1)):
                for y in range(3*(j//3), 3*(j//3+1)):
                    if (x, y) != (i, j) and ((x, y),(i, j)) not in constraints:
                        constraints.add(((i, j), (x, y)))

    def backtrack_solve(assignment, constraints):
        if len(assignment) == 81:
            return assignment

        (x,y) = (-1,-1)
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                if (i,j) not in assignment and board[i][j] is None:
                    (x,y) = (i,j)
                    break
            if (x,y) != (-1,-1):
                break
        
        for k in range(1, 10):
            assignment[(x, y)] = k
            # Check for consistency with constraints
            constraintFit = True
            for constraint in constraints:
                if((x, y) in constraint):
                    otherIndex = 1 - constraint.index((x, y))
                    if constraint[otherIndex] in assignment:
                        if assignment[(x, y)] == assignment[constraint[otherIndex]]:
                            constraintFit = False
                            break
                
            if not constraintFit:
                del assignment[(x, y)]
                continue
            result = backtrack_solve(assignment, constraints)
            if result is not None:
                return result
            del assignment[(x, y)]
        return None
    
    initial_assignment = dict()
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if board[i][j] is not None:
                initial_assignment[(i,j)] = board[i][j]

    solved_assignment = backtrack_solve(initial_assignment, constraints)

    if(solved_assignment is None):
        print("UNSOLVABLE!")
        return None

    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if board[i][j] is None:
                board[i][j] = solved_assignment[(i, j)]
    return board
                    
def main():
    board = load_sudoku_board("sudoku.txt")
    sudoku_solve(board)
    
    #Print out solution
    for line in board:
        for cell in line:
            if cell is None:
                print(end=' ')
            else:
                print(cell, end=' ')
        print("")

main()