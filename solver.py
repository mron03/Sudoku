from xmlrpc.client import Boolean

def solve(bo):  
    #Checks if there are still empty positions, 
    # then return back inside for loop
    if findEmpty(bo) == None: return True 

    emPos = findEmpty(bo)  

    isValid = False

    for i in range(1, 10):

        isValid = False

        if valid(bo, i, emPos):

            bo[emPos[0]][emPos[1]] = i
            isValid = True

            solve(bo)
            #If the sudoku is done it should keep returning, check empty position
            if findEmpty(bo) == None: return True

    # Checks if the for loop worked, 
    # if it did not it empties current position 
    # and goes back to previous position
    if not isValid:
        bo[emPos[0]][emPos[1]] = 0
        return False
    return True
    

    


def valid(bo, num, pos) -> Boolean:

    x = pos[0]
    y = pos[1]
    
    #Check column
    for i in range(len(bo)):
        
        if i != x and bo[i][y] == num:
            return False

    #Check column
    for i in range(len(bo)):

        if i != y and bo[x][i] == num:
            return False
   
    
    #Check quadrant
    #Find the most left-up position of the relevant quadrant
    a = x - (x % 3) 
    b = y - (y % 3)   

    for i in range(a, a + 3):                       
        for j in range(b, b + 3):
            if (i, j) != (x, y) and bo[i][j] == num:
                return False
            

    return True


def printBoard(bo):
    for i in range(len(bo)):
        
        if i % 3 == 0 and i != 0:
            print('- - - - - - - - - - - ')
            
            
        for j in range(len(bo[i])):

            if j % 3 == 0 and j != 0:
                print('|', end=' ')

            print(bo[i][j], end=' ')

        
        print()

        
def findEmpty(bo):

    for i in range(len(bo)):
        for j in range(len(bo[i])):
            if bo[i][j] == 0: 
                
                return (i, j)  
    return None
    
