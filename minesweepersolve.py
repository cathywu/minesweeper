import numpy as np

def checker(board):
    print board
    ms = (board == -100)
    qs = (board == -1000)
    (checkx,checky) = np.nonzero(board > 0)

    for (i,j) in zip(checkx,checky):
        mask = np.zeros((12,12))

        width = 3
        height = 3
        if i == 0:
            xstart = i
            width -= 1
        else:
            xstart = i-1

        if i == 11:
            xend = i+1
            width -= 1
        else:
            xend = i+2

        if j == 0:
            ystart = j
            height -= 1
        else:
            ystart = j-1

        if j == 11:
            yend = j+1
            height -= 1
        else:
            yend = j+2

        mask[xstart:xend,ystart:yend] = np.ones((width,height))
        nms = len(np.nonzero(np.logical_and(ms,mask))[0])
        nqs = len(np.nonzero(np.logical_and(qs,mask))[0])
        if board[i][j] < nms or board[i][j] > nms + nqs:
            print '(%s,%s) wants [%s] but has [%s] mines with [%s] qs' % (i,j,board[i][j],nms,nqs)
            return False
    return True

m = '-100'
q = '-1000'

board = [[q for x in xrange(12)] for x in xrange(12)]
board = np.array(board, np.int32)

pieces = [[[m,8],
           [m,m]],
          [[7,m],
           [m,m]],
          [[m,m],
           [m,3]],
          [[1,0],
           [1,0]],
          [[m,3],
           [5,3]],
          [[0,0],
           [1,1]],
          [[6,m],
           [m,m]],
          [[1,m],
           [3,6]],
          [[m,2],
           [1,2]],
          [[4,m],
           [4,m]],
          [[1,0],
           [0,0]],
          [[m,2],
           [2,1]],
          [[1,3],
           [2,m]],
          [[2,1],
           [m,1]],
          [[2,3],
           [m,m]],
          [[m,6],
           [m,m]],
          [[m,7],
           [m,m]],
          [[3,m],
           [m,2]],
          [[2,2],
           [m,2]],
          [[0,1],
           [1,2]],
          [[2,1],
           [m,2]],
          [[3,m],
           [1,3]],
          [[m,4],
           [m,3]],
          [[1,2],
           [m,4]],
          [[2,2],
           [2,m]],
          [[2,2],
           [2,m]],
          [[m,m],
           [2,4]],
          [[3,3],
           [m,m]],
          [[m,m],
           [4,3]],
          [[4,1],
           [2,0]],
          [[1,m],
           [1,2]],
          [[m,m],
           [3,2]]]


board[2:4,2:4]   = [[2,3],[3,m]]
board[2:4,8:10]  = [[m,3],[5,m]]
board[8:10,8:10] = [[2,m],[2,2]]
board[8:10,2:4]  = [[3,4],[3,3]]
print "Starting Board:"
print board


# Populate Board
def populateBoard(board,piecesAvailable,(x,y),i):
    print (x,y,len(piecesAvailable),i)
    if i == len(piecesAvailable):
        return False
    piece = piecesAvailable[i]
    bcopy = board.copy()
    bcopy[2*y:2*y+2,2*x:2*x+2] = piece
    works = checker(bcopy)
    if len(piecesAvailable) == 1: # last piece
        print "Len 1 result: %s" % works
        return works
    elif works:
        (x_new,y_new) = ((x + 1 + int((x==0 or x==3) and (y==1 or y==4)))%6,y+int(x==5))
        pcopy = list(piecesAvailable)
        pcopy.remove(piece)
        return populateBoard(bcopy,pcopy,(x_new,y_new),0) or \
                populateBoard(board.copy(),list(piecesAvailable),(x,y),i+1)  
    else: 
        return populateBoard(board.copy(),list(piecesAvailable),(x,y),i+1)

print len(pieces)

print populateBoard(board,pieces,(0,0),0) 
