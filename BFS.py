#importing things necessary
import collections
import timeit

#used for determining the root node's parent
ROOT_PARENT = -999

#function for printing the path once the parents array is created
def path(goalNode, parents):
   x = goalNode
   myPathList = [x]
   #while we havent reached the root, iterate
   while parents[x] != ROOT_PARENT:
      if parents[x] > goalNode:
        modNode = parents[x] % (goalNode+1)
        myPathList.append(modNode)
      else:
        myPathList.append(parents[x])
      x = parents[x]
   #reverse path for printing in order
   myPathList.reverse()
   print "----------BFS Path----------"
   print myPathList

#Clone of actual BFS function used for determining Execution Time
def BreadthFirstSearchExc(AdjListAndSize):
   board = AdjListAndSize[0]
   rowSize = AdjListAndSize[1]
   size = (rowSize * rowSize) * 2
   visited = [[None]] * size
   parents = [[None]] * size
   queue = collections.deque([])

   i = 0
   for i in range(0, size):
      visited[i] = False
      parents[i] = -1
   
   visited[0] = True
   queue.append(0)
   parents[0] =  ROOT_PARENT
   currentNode = 0
   
   while queue:
      currentNode = queue[0]
      queue.popleft()
      i = 0
      j = 0
      for node in board:
         if i == currentNode:
            for values in node:
               if j == 0:
                  if not visited[currentNode]:
                     visited[currentNode] = True
                     queue.append(values)
               elif not visited[values]:
                  visited[values] = True
                  queue.append(values)
                  parents[values] = currentNode
               j = j + 1
         i = i + 1
         j = 0
      i = 0
      if currentNode == rowSize * rowSize - 1:
        break

#function for determining the exectuion time of the BFS search
#runs 100 times and prints the exc. time
def excTime(board):
   iterations = 100
   #start the timer
   start_time = timeit.default_timer()

   for rep in range(iterations):
      BreadthFirstSearchExc(board)
   #stop the timer
   elapsed = timeit.default_timer() - start_time
        
   #print the shotest path
   print "Exection time:", elapsed, "seconds for", iterations, "times"

#actual BFS function
#takes an adjacency list and traverses through it
def BreadthFirstSearch(AdjListAndSize):
   board = AdjListAndSize[0]
   rowSize = AdjListAndSize[1]
   size = (rowSize * rowSize) * 2
   visited = [[None]] * size
   parents = [[None]] * size
   queue = collections.deque([])

   #initialize the visited and parents arrays
   i = 0
   for i in range(0, size):
      visited[i] = False
      parents[i] = -1
   
   visited[0] = True
   queue.append(0)
   parents[0] =  ROOT_PARENT
   currentNode = 0
   
   #with queue containing the starting node
   #iterate through it while there are nodes in queue
   while queue:
      #access the leftmost node, and pop it
      currentNode = queue[0]
      queue.popleft()
      i = 0
      j = 0
      #loop for determining whether we've visited a node or not,
      #if we have, we move on
      #if not, we write its parent in the parents array insert
      #it in the queue for further examination
      for node in board:
         if i == currentNode:
            for values in node:
               if j == 0:
                  if not visited[currentNode]:
                     visited[currentNode] = True
                     queue.append(values)
               elif not visited[values]:
                  visited[values] = True
                  queue.append(values)
                  parents[values] = currentNode
               j = j + 1
         i = i + 1
         j = 0
      i = 0
      #if we located the goal node, we terminate the function
      if currentNode == rowSize * rowSize - 1:
        break
   #print the path found and stored in the parents array
   path(rowSize*rowSize-1, parents)
   #figure out how long it took to find such path
   excTime(AdjListAndSize)
