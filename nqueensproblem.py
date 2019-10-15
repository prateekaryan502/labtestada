#to put  n queens in n*n chessboard such that no two queens are under attack

def nqueen(board,c,n):
    if c>=n:
        return True

    for i in range(n):
        if queennotunderattack(board,i,c,n):
            board[i][c]=1
            if nqueen(board,c+1,n)==True:
                print(board)
            board[i][c]=0
    return False


def queennotunderattack(board,r,c,n):
    #checck there is no attack in column
    for i in range(c):
        if board[r][i]==1:
            return False
    for i,j in zip(range(r,-1,-1),range(c,-1,-1)):
        if board[i][j]==1:
            return False
    for i, j in zip(range(r, n, 1), range(c, -1, -1)):
        if board[i][j] == 1:
            return False
    return True
n=4
board=[[0 for i in range(n)] for j in range(n)]
print(board)
nqueen(board,0,n)