__author__ = 'ONicholls'


#Piece of generic code for reading
#in a file into a program.
def read_sudoku(file):
    stream = open(file)
    data = stream.readlines()
    stream.close()
    # some comment for science!
    return eval("".join(data))



#This function converts an array
#of integers into an array of sets.
#0's are converted to a set containing
#values 1-9 and single numbers are
#converted to a set containing that
#one number.
def convertToSets(problem):
    nums_append = list(range(1,10))
    for i in range(len(problem)):
        for j in range(len(problem)):
            if problem[i][j] == 0:
                problem[i][j] = set(nums_append)
            elif problem[i][j] != 0:
                problem[i][j] = {problem[i][j]}
    return problem




#This function converts an array
#of sets into an array of integers.
#Singleton sets are converted to a
#integer containing that element.
#If a position has a set containing
#more than one element, a 0 is
#assigned.
def convertToInts(problem):
    for i in range(len(problem)):
        for j in range(len(problem)):
            if len(problem[i][j]) == 1:
                problem[i][j] = list(problem[i][j])[0]
            elif len(problem[i][j]) != 1:
                problem[i][j] = 0
    return problem




#Given a particular row number, this function
#will return all of the locations in the row in
#(row, column) format.
def getRowLocations(rowNumber):
    empty_rows= list()
    [empty_rows.append((rowNumber,k)) for k in range (9)]
    return empty_rows


#Given a particular column number, this function
#will return all of the locations in the column in
#(row, column) format.
def getColumnLocations(columnNumber):
    empty_cols = list()
    [empty_cols.append((k, columnNumber)) for k in range(9)]
    return empty_cols



#######################################
#Intuition - There are 9 defined boxes#
#in the grid, starting at locations:  #
#       (0,0), (0,3), (0,6)           #
#       (3,0), (3,3), (3,6)           #
#       (6,0), (6,3), (6,6)           #
#######################################
#Given a particular location as a tuple,
#this function
#will return all of the locations in
#the 3x3 box in (row, column) format.
def getBoxLocations(location):
    BOX_SIZE = 3
    loc_box = list()
    for i in range(BOX_SIZE):
        for j in range(BOX_SIZE):
            loc_box.append(((location[0] - location[0]%BOX_SIZE + j) \
                            , (location[1] - location[1]%BOX_SIZE + i)))
    return loc_box




#Calls the custom remove function below
#that goes through all of the locations
#in the puzzle and removes the number
#from all other sets in a given number
#of locations.
def eliminate(problem, location, listOfLocations):
    return remove(list(problem[location[0]][location[1]]).pop(), \
                  problem, listOfLocations, location)


#Initialises a remove count, and cycles through
#the given locations comprising row, column
#and boxes taking out singleton sets from
#all other sets of length greater than 1 in
#the listofLocations.
def remove(number, problem, listOfLocations, location):
    num_remove = 0
    for pos in listOfLocations:
        if pos != location and number in problem[pos[0]][pos[1]]:
            problem[pos[0]][pos[1]].remove(number)
            num_remove = num_remove + 1
    return num_remove




#The condition for a puzzle to be solved
#is that if after looping through all
#of the locations in the puzzle,
#each set in the locations is a set
#of length 1, if not the puzzle isnt
#solved.
def isSolved(problem):
    all_solved = True
    for i in range(len(problem)):
        for j in range(len(problem)):
            if len(problem[i][j]) != 1:
                return not all_solved
    return all_solved





#Sets up a number of removals count, and again
#if a set of length 1 is found, the eliminate
#function is called with row, column and box
#locations for that given location. This process
#is repeated until the problem contains solely sets
#of length 1 as per the isSolved function.
def solve(problem):
    while not isSolved(problem):
        num_removals = 0
        for i in range(len(problem)):
            for j in range(len(problem)):
                if len(problem[i][j]) == 1:
                    num_removals = num_removals + \
                    eliminate(problem,(i, j), listEveryLocation((i,j)))
        if num_removals == 0:
            return not isSolved(problem)
    return isSolved(problem)



#An additional function that takes in a
#location as the parameter and returns all
#of the row, column and box locations in
#that location. It is called by the solve
#function and subsequently by eliminate.
def listEveryLocation(location):
    row_pos = location[0]
    col_pos = location[1]
    rows = getRowLocations(row_pos)
    cols = getColumnLocations(col_pos)
    boxes = getBoxLocations(location)
    locations = rows + cols + boxes
    return locations



#Takes in a problem as the parameter
#and returns a properly formatted sudoku
def print_sudoku(problem):
    print("+-------+-------+-------+")
    for i in range(len(convertDots(problem))):
        for j in range(0, len(convertDots(problem)), 3):
            print("|",convertDots(problem)[i][j], end = " ")
            print(convertDots(problem)[i][j+1], end = " ")
            print(convertDots(problem)[i][j+2], end = " ")
        print("|", end="")
        print("")
        if i==2:
            print("+-------+-------+-------+")
        if i==5:
            print("+-------+-------+-------+")
        if i==8:
            print("+-------+-------+-------+")



#An additional function that takes in
#a sudoku problem as a parameter
#and returns a problem back that
#has all of the 0's changed to
#dots
def convertDots(problem):
    for i in range(len(problem)):
        for j in range(len(problem)):
            if problem[i][j] == 0:
                problem[i][j] = "."
            else:
                problem[i][j]
    return problem


#Asks the user for a puzzle as an input
#and prints out the unsolved puzzle.
#If it can be solved it will be printed
#out, however if not, all of the unsolved
#locations and possible values for each
#will be returned.
#Finally, the user will be asked if they want
#to solve another puzzle, if no is typed,
#the program ends.
def main():
    another_puzzle = True
    yes_set = {"Y", "y", "Yes", "yes"}
    while another_puzzle == True:
        print("")
        input_file = input("Type in a file \
containing the Sudoku: ")
        try:
            inputted_file = read_sudoku(input_file)

        except IOError:
            print("Error, cannot find file.")
            continue
        print("")
        print("Here is the puzzle:")
        print_sudoku(read_sudoku(input_file))
        print("")
        print("Attempting to solve the puzzle...")
        prob_sets = convertToSets(inputted_file)
        isSolv = solve(prob_sets)
        print("")
        if not isSolved(prob_sets):
            print("Could not solve puzzle")
            print("Below are the unsolved \
locations and possible values")
            print("")
            for i in range(len(inputted_file)):
                for j in range(len(inputted_file)):
                    if len(inputted_file[i][j]) != 1:
                        print("Unsolved Location" , " ",  (i,j) ," ",\
                              "could be any of" ," ",\
                              inputted_file[i][j], sep = "")
            print("")
            print("")
            print("Below is the incomplete solution")
            print_sudoku(convertToInts(inputted_file))
        else:
            if isSolved:
                print("Puzzle successfully solved!")
                print_sudoku(convertToInts(inputted_file))
        print("")
        again = input("Would you like to solve \
another puzzle? Type in Yes or No: ")
        if again not in yes_set:
            another_puzzle = False
            print("End of Sudoku game, thanks for playing" )


#main()
