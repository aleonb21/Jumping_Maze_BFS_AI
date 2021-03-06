#!/usr/bin/python

#CIS4930: AI, Final Project
#Group Members:
#__Angel Leon

#Access file to retrieve Number Maze board
#---first, get the file's name from the user
#board_name = raw_input("Enter name of desired board, including file extension: ")

def createADJList1(board_name):

   #---open the file
   #---*below is the same as ~Board_file = open(board_name, "r")~ but ensures
   #---*the file is closed regardless of any errors
   with open(board_name, "r") as Board_file:

      #get the information to create the board
      BOARD = [] #container for holding the board, initialize to an empty list
      i = 0      #index into list, initialized to 0
      for lines in Board_file:              #for each row of the baord in the file
         line = lines.strip().split()        #get rid of the spaces and make into list
         BOARD.append([])                  #append a new empty list
         for squares in line:               #for each number in the row
            BOARD[i].append(int(squares))  #append int version of number to BOARD's row
         i = i + 1                         #increment the index

   sizeOfRowCol = len(BOARD)           #holds size of row or column

   #-------------------------------------------------------------------#
   #----Creating Adjacency List for EXCLUSIVELY POSITIVE BOARD---------#
   #-------------------------------------------------------------------#
   #Creates a List of lists called adjList. The first value of adjList will
   #be the value of the cell of the board being examined. The subsequent values
   #will be the possible cells where we can move

   i = 0
   j = 0
   index = 0
   horVerList = []                     #holds temp list of possible places to move to
   diagList = []                       #not needed for now
   zeroList = [0]                      #holds goal state
   adjList = []
   sizeOfBoard = sizeOfRowCol * sizeOfRowCol
   sizeOfDoubleBoard = sizeOfBoard * 2

   for i in range(0, sizeOfRowCol):
      for j in range(0, sizeOfRowCol):
         horVerList = []
         diagList = []                #not needed for now
         cellValue = BOARD[i][j]
         column = index % sizeOfRowCol
         row = index / sizeOfRowCol
         
         if cellValue < 0:
            absCellValue = cellValue * -1
         else:
            absCellValue = cellValue
         
         horVerList.append(cellValue)

         diagList.append(cellValue)
      
         #check if we can go up
         if row - absCellValue >= 0:
            horVerList.append(index - absCellValue * sizeOfRowCol)
         
         #check if we can go left
         if column - absCellValue >= 0:
            horVerList.append(index - absCellValue)
         
         #check if we can go down
         if row + absCellValue < sizeOfRowCol:
            horVerList.append(index + absCellValue * sizeOfRowCol)
         
         #check if we can go right
         if column + absCellValue < sizeOfRowCol:
            horVerList.append(index + absCellValue)
            
         #check if we can go northwest
         if row - absCellValue >= 0 and column - absCellValue >= 0:
            if index - absCellValue * sizeOfRowCol - absCellValue + sizeOfBoard != sizeOfDoubleBoard - 1:
               diagList.append(index - absCellValue * sizeOfRowCol - absCellValue + sizeOfBoard)
            else:
               diagList.append(sizeOfBoard - 1)
         
         #check if we can go southwest
         if row + absCellValue < sizeOfRowCol and column - absCellValue >= 0:
            if index + absCellValue * sizeOfRowCol - absCellValue + sizeOfBoard != sizeOfDoubleBoard - 1:
               diagList.append(index + absCellValue * sizeOfRowCol - absCellValue + sizeOfBoard)
            else:
               diagList.append(sizeOfBoard - 1)
               
         #check if we can go northeast
         if row - absCellValue >= 0 and column + absCellValue < sizeOfRowCol:
            if index - absCellValue * sizeOfRowCol + absCellValue + sizeOfBoard != sizeOfDoubleBoard - 1:
               diagList.append(index - absCellValue * sizeOfRowCol + absCellValue + sizeOfBoard)
            else:
               diagList.append(sizeOfBoard - 1)
         
         #check if we can go southeast
         if row + absCellValue < sizeOfRowCol and column + absCellValue < sizeOfRowCol:
            if index + absCellValue * sizeOfRowCol + absCellValue + sizeOfBoard != sizeOfDoubleBoard - 1:
               diagList.append(index + absCellValue * sizeOfRowCol + absCellValue + sizeOfBoard)
            else:
               diagList.append(sizeOfBoard - 1)
         
         #if our value is positive, add list compiled to adjlist
         if cellValue > 0:
            adjList.append(diagList)
            adjList.insert(index, horVerList)
         elif cellValue < 0:
            adjList.append(horVerList)
            adjList.insert(index, diagList)
         #if its 0, then add the zero list to adjList
         elif cellValue == 0:
            adjList.insert(index, zeroList)
            adjList.append(zeroList)             #account for the diagonal version of end square
         
         j += 1               #increments neccesary
         index += 1
      i += 1

   #If the file has not already been closed, close it
   if not Board_file.closed:
      Board_file.close()

   return [adjList, sizeOfRowCol, BOARD]
