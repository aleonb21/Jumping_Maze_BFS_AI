#****IMPORT YOUR SEARCH FILE HERE*****
import Angel_FP_MMSolver_v5
import BFS

board_name = raw_input("Enter name of board, including file extension: ")

board1 = Angel_FP_MMSolver_v5.createADJList1(board_name)

print "The board selected is:"
for lists in board1[2]:   #for each row in the BOARD
  print lists           #print the row
print("")

#BFS
BFS.BreadthFirstSearch(board1)
