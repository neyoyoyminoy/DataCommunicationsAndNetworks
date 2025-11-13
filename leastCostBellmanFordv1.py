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

INF = 10**9

# Node numbering:
# t=1, u=2, v=3, w=4, x=5, y=6, z=7

# Cost matrix C (7x7)
# Index 0 unused for clarity; nodes are 1..7
C = [
    [],  # dummy row so index = nodeID
    [0,   2,   4, INF, INF,   7, INF],   # t=1
    [2,   0,   3,   3, INF, INF, INF],   # u=2
    [4,   3,   0,   4,   3,   8, INF],   # v=3
    [INF, 3,   4,   0,   6, INF, INF],   # w=4
    [INF, INF, 3,   6,   0,   6,   8],   # x=5
    [7, INF, 8, INF, 6,   0,  12],       # y=6
    [INF, INF, INF, INF, 8, 12,   0]     # z=7
]

N = 7  # number of nodes

# initialize distance vector matrix D = C (column form)
D = [[0]*(N+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, N+1):
        D[i][j] = C[i][j]

def print_matrix(M, title):
    print("\n" + title)
    print("-" * len(title))
    for i in range(1, N+1):
        row = []
        for j in range(1, N+1):
            val = M[i][j]
            row.append("∞" if val >= INF else str(val))
        print(" ".join(f"{x:>3}" for x in row))
    print()

print_matrix(D, "Initial Distance Vectors (D = C)")

# Iterate until convergence
iteration = 0
while True:
    iteration += 1
    oldD = copy.deepcopy(D)

    # Bellman–Ford vector update
    for i in range(1, N+1):          # destination
        for j in range(1, N+1):      # this is node j's distance vector column
            best = D[i][j]
            for k in range(1, N+1):  # neighbor k
                best = min(best, C[j][k] + oldD[i][k])
            D[i][j] = best

    print_matrix(D, f"Iteration {iteration} Updated Distance Vectors")

    # Check convergence
    if D == oldD:
        print("Converged.")
        break
