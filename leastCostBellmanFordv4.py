'''
Brendan Nellis ujf306
this is for my data comms and networks class project

given instructions:
Write a computer program that implements the Bellman-Ford algorithm and produces the
least-cost distance vectors (from any source to any destination) for a given network. Your
code should print the initial distance vectors and the updated distance vectors in every
iteration, until convergence.
The input to your code should be a matrix C with entries c(i,j) = link cost between i and j (if
there is a link between i and j); c(i,j) = ∞ (or very large number) if there is no link between i
and j; and c(i,i) = 0. 
'''

import copy

infinity = 10**9 #using a big number for infintiy

c = [ #matrix c
  [],
  [0, 0, 2, 4, infinity, infinity, 7, infinity], #t = 1 row
  [0, 2, 0, 3, 3, infinity, infinity, infinity], #u = 2 row
  [0, 4, 3, 0, 4, 3, 8, infinity], #v = 3 row
  [0, infinity, 3, 4, 0, 6, infinity, infinity], #w = 4 row
  [0, infinity, infinity, 3, 6, 0, 6, 8], #x = 5 row
  [0, 7, infinity, 8, infinity, 6, 0, 12], #y = 6 row
  [0, infinity, infinity, infinity, infinity, 8, 12, 0], #z = 7 row
]

nodes = 7

distance = [[0] * (nodes + 1) for _ in range (nodes + 1)] #creating a 2d matrix

for i in range (1, nodes + 1):
  for j in range (1, nodes + 1):
    distance[i][j] = c[i][j] #starting with D = C

def matrixPrint(matrix, title):
  print("\n" + title)
  print("-" * len(title))
  
  for i in range(1, nodes + 1):
    row = []
    
    for j in range(1, nodes + 1):
      value = matrix[i][j]
      row.append("infinity" if value >= infinity else str(value))
      
    print(" ".join(f"{x:>3}" for x in row))
  print()

matrixPrint(distance, "initial distance vectors") #for the start point

iteration = 0

while True:
  iteration += 1
  oldDistance = copy.deepcopy(distance) #for comparison

  for i in range(1, nodes + 1): #destination
    for j in range(1, nodes + 1): #node j's vector
      best = distance[i][j] #updates each D(i, j)

      for k in range (1, nodes + 1): #neighbors
        best = min(best, c[i][j] + oldDistance[i][j])

      distance[i][j] = best

matrixPrint(distance, f"iteration: {iteration}") #showing updates

if distance == oldDistance:
  print("converged") #checking convergence
        break #only if nothing happens
