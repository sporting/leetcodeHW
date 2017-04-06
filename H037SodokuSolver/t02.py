# -*- coding: utf-8 -*-
import sys

# reference 
# https://discuss.leetcode.com/topic/63534/beats-99-really-really-fast-and-with-explanation-and-chinese-comment/2
class Solution(object):
    def __init__(self):
        self.finded = False
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.solve(board)

    def solve(self,board):
        if ((self.finded) or self.isFull(board)):
            self.finded = True
            return
        index = self.findIndex(board)
        #print index
        if (index != None):
            values = self.findAvaible(index[2],index[3])
            #print values
            for e in values:
                #print e
                board[index[0]] = ''.join(board[index[0]][:index[1]])+str(e)+''.join(board[index[0]][index[1]+1:])

                #board[index[0]][index[1]] = e
                print board
                self.solve(board)
                if (self.finded):
                    return
            board[index[0]] = ''.join(board[index[0]][:index[1]])+'.'+''.join(board[index[0]][index[1]+1:])

    def findIndex(self,board):
        result = []
        r = [None] * 9
        c = [None] * 9
        g = [None] * 9
        mask = 0x01FF
        for i in xrange(len(board)):
            sr, sc = 0, 0
            for j in xrange(len(board)):
                if board[i][j] != '.':
                    sr |= (1 << (int(board[i][j]) - 1))
                    #print sr
                    #print (1 << (int(board[i][j]) - 1))                    
                if board[j][i] != '.':
                    #print board[j][i]
                    sc |= (1 << (int(board[j][i]) - 1))

            sr = (~sr) & mask
            sc = (~sc) & mask
            r[i] = sr
            c[i] = sc

        for i in xrange(0,9,3):
            for j in xrange(0,9,3):
                sg = 0  
                for m in xrange(3):
                    for n in xrange(3):
                        if board[i+m][j+n] != '.':
                            sg |= (1 << (int(board[i+m][j+n]) - 1))
                sg = (~sg) & mask
                g[i+j/3] = sg

        min = sys.maxint
        for i in xrange(len(board)):
            for j in xrange(len(board)):
                if (board[i][j] == '.'):
                    m = r[i] & c[j] & g[((i/3)*3)+(j/3)]
                    if m == 0:
                        return None
                    n = self.countBit(m)
                    if (min > n):
                        min = n
                        result = [i,j,min,m]
                       # print r[i] 
                       # print c[j] 
                      ##  print g[(i/3)*3+j/3]
                      #  print result
        return result

    def countBit(self,x):
        count = 0
        while (x != 0):
            count = count + 1
            x &= (x - 1)
        return count

    def findAvaible(self,n,m):
        r = [None] * n
        i, j = 0, 0
        while (j < n):
            #print i,j,n,m
            if ((m & (1 << i)) != 0):
                #print i,j,m,n
                r[j] = str(i+1)
                #print r[j]
                j = j + 1
            i = i + 1
        #print r
        return r

    def isFull(self,board):
        for i in xrange(len(board)):
            for j in xrange(len(board)):
                if board[i][j] == '.':
                    return False
        return True    


if __name__ == "__main__":
    solution = Solution()
    board =[\
            "8........"  ,\
            "..36....."  ,\
            ".7..9.2.."  ,\
            ".5...7..."  ,\
            "....457.."  ,\
            "...1...3."  ,\
            "..1....68"  ,\
            "..85...1."  ,\
            ".9....4.."  \
            ]

    solution.solveSudoku(board)
'''
    board =[\
            "..9748..."  ,\
            "7........"  ,\
            ".2.1.9..."  ,\
            "..7...24."  ,\
            ".64.1.59."  ,\
            ".98...3.."  ,\
            "...8.3.2."  ,\
            "........6"  ,\
            "...2759.."  \
            ]

    board =[\
            ".4.25...8"  ,\
            ".3.4.917."  ,\
            "....812.."  ,\
            "..6...72."  ,\
            "...6.4..."  ,\
            ".12...3.."  ,\
            "..381...."  ,\
            ".649.2.1."  ,\
            "7...45.9."  \
            ]        
'''
    
