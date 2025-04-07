def is_safe(board, row, col, N): 

   # Check for queens in the same row (left side) 

   for i in range(col): 

       if board[i] == row: 

           return False 

     

   # Check upper diagonal (left side) 

   for i, j in zip(range(col - 1, -1, -1), range(row - 1, -1, -1)): 

       if board[i] == j: 

           return False 

 

   # Check lower diagonal (left side) 

   for i, j in zip(range(col - 1, -1, -1), range(row + 1, N)): 

       if board[i] == j: 

           return False 

     

   return True 

 

def solve_n_queens(board, col, N): 

   if col >= N: 

       return True # All queens are placed 

 

   for row in range(N): 

       if is_safe(board, row, col, N): 

           board[col] = row # Place queen 

           if solve_n_queens(board, col + 1, N): 

               return True # Proceed to the next column 

           board[col] = -1 # Backtrack 

 

   return False # No valid position found 

 

def print_solution(board, N): 

   for row in range(N): 

       line = "" 

       for col in range(N): 

           if board[col] == row: 

               line += "Q " 

           else: 

               line += ". " 

       print(line) 

   print("\n") 

 

# Driver function 

def n_queens(N): 

   board = [-1] * N # Initialize board 

   if solve_n_queens(board, 0, N): 

       print_solution(board, N) 

   else: 

       print("No solution exists for N =", N) 

 

# Example: Solve for 8 queens 

N = 8 

n_queens(N) 