# -*- coding: utf-8 -*-
import copy

# stupid to simulate my mind

class PointPossibleResult(object):
    def __init__(self):
        self.ary = list("111111111")
    def setOne(self, num):
        self.ary = list("000000000")
        n = int(num)
        self.ary[n-1] = "1"
    def remove(self, num):
        n = int(num)
        self.ary[n-1] = "0"
    def answer(self):
        return str(self.ary.index("1") + 1) if sum(int(num) for num in self.ary) == 1 else None

class Solution(object):
    def SearchPossible(self, maps):
        for y in xrange(0, 9):
            for x in xrange(0, 9):
                id = str(x) + str(y)
                possible = maps[id]
                val = possible.answer()

                if val != None:
                    for z in xrange(0, 9):
                        id2 = str(z) + str(y)
                        if id != id2:
                            maps[id2].remove(val)
                    for z in xrange(0, 9):
                        id2 = str(x) + str(z)
                        if id != id2:
                            maps[id2].remove(val)
                    bx = (x / 3) * 3
                    by = (y / 3) * 3
                    for ax in xrange(bx, bx+3):
                        for ay in xrange(by, by+3):
                            id2 = str(ax)+str(ay)
                            if id != id2:
                                maps[id2].remove(val)
            #break

    def printmaps(self, maps):
        for y in xrange(0, 9):
            ary = ""
            for x in xrange(0, 9):
                id = str(x) + str(y)
                val = maps[id].answer()
                if val == None:
                    val = "."
                ary = ary + val
            print ary

    def sameMaps(self, aMaps, bMaps):
        for y in xrange(0, 9):
            arya = ""
            for x in xrange(0, 9):
                id = str(x) + str(y)
                val = aMaps[id].answer()
                if val == None:
                    val = "."
                arya = arya + val
            aryb = ""
            for x in xrange(0, 9):
                id = str(x) + str(y)
                val = bMaps[id].answer()
                if val == None:
                    val = "."
                aryb = aryb + val
            if arya != aryb:
                #print arya
                #print aryb
                return False
        return True


    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        maps = dict()
        for x in xrange(0, 9):
            for y in xrange(0, 9):
                id = str(x) + str(y)
                maps[id] = PointPossibleResult()

        for idx2,nums in enumerate(board):
            for idx,num in enumerate(list(nums)):
                id = str(idx) + str(idx2)
                if num != '.':
                    maps[id].setOne(int(num))
        print '-----0------'
        self.printmaps(maps)

        cnt = 1
        while True:
            flag = True
            for id in maps:
                if maps[id].answer() == None:
                    flag = False
                    break
            if flag:
                break
            oriMaps = copy.deepcopy(maps)
            #self.printmaps(oriMaps)
            print ''
            print '-----'+str(cnt)+'------'
            self.SearchPossible(maps)
            print ''

            cnt = cnt+1
            #self.printmaps(oriMaps)            
            self.printmaps(maps)

            if self.sameMaps(oriMaps,maps):
                print 'I can''t find more answer, u must make me more clever'
                return
            if cnt > 9999:
                return


        for y in xrange(0, 9):
            ary = ""
            for x in xrange(0, 9):
                id = str(x) + str(y)
                ary = ary + maps[id].answer()
            board[y] = ary


if __name__ == "__main__":
    solution = Solution()
    board = ["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]
    solution.solveSudoku(board)
