import math 
MAX, MIN = 1000, -1000
def minimax(depth , nodeindex , maximizingplayer , values , alpha, beta ):
    if depth == 3:
        return values[nodeindex]
    if maximizingplayer:
        best = MIN 
        for i in range (0,2):
            val = minimax (depth +1, nodeindex *2 +i ,False , values ,alpha ,beta)
            best = max (best, val)
            alpha = max (alpha ,best)
            if beta <= alpha:
                break
        return best
    else:
        best =MAX 
        for i in range (0,2):
            val= minimax (depth + 1, nodeindex *2+i, True , values,alpha, beta)
            best = min(best,val)
            alpha = min(alpha , best)
            if beta <= alpha:
                break
        return best 
values = [84,-29,-37,-25,1,-4,-75,49]
alpha =MIN
beta =MAX 
result = minimax(  0,0, True , values, alpha ,beta)
print(f" Optimal Value : {result}")