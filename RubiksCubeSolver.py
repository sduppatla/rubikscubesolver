import math, copy, random
from cmu_112_graphics import *
from tkinter import *

# Method to solve cube from:
# https://ruwix.com/the-rubiks-cube/how-to-solve-the-rubiks-cube-beginners-method/
def solveWhiteCrossOnYellow(self):
    rCount = 0
    if self.whiteCrossIsNotSolved:
        #checking upper face
        if (self.app.upperFace[2][1] == 'white' and self.app.bottomFace[0][1] != 'white'):
            self.moves = 'F2'
            self.whiteCrossSolve += 'FF'
            self.rotateF()
            self.rotateF()
        elif (self.app.upperFace[1][0] == 'white' and self.app.bottomFace[1][0] != 'white'):
            self.moves = 'L2'
            self.whiteCrossSolve += 'LL'
            self.rotateL()
            self.rotateL()
        elif (self.app.upperFace[1][2] == 'white' and self.app.bottomFace[1][2] != 'white'):
            self.moves = 'R2'
            self.whiteCrossSolve += 'RR'
            self.rotateR()
            self.rotateR()
        elif (self.app.upperFace[0][1] == 'white' and self.app.bottomFace[2][1] != 'white'):
            self.moves = 'B2'
            self.whiteCrossSolve += 'BB'
            self.rotateB()
            self.rotateB()
        #checking middle row to move onto yellow cross
        elif self.app.rightFace[1][0] == 'white' and self.app.bottomFace[0][1] != 'white':
            self.moves = 'F'
            self.whiteCrossSolve += 'F'
            self.rotateF()
        elif self.app.leftFace[1][2] == 'white' and self.app.bottomFace[0][1] != 'white':
            self.moves = "F'"
            self.whiteCrossSolve += "F'"
            self.rotateFP()
        elif self.app.frontFace[1][0] == 'white' and self.app.bottomFace[1][0] != 'white':
            self.moves = 'L'
            self.whiteCrossSolve += 'L'
            self.rotateL()
        elif self.app.backFace[1][2] == 'white' and self.app.bottomFace[1][0] != 'white':
            self.moves = "L'"
            self.whiteCrossSolve += "L'"
            self.rotateLP()
        elif self.app.leftFace[1][0] == 'white' and self.app.bottomFace[2][1] != 'white':
            self.moves = "B"
            self.whiteCrossSolve += 'B'
            self.rotateB()
        elif self.app.rightFace[1][2] == 'white' and self.app.bottomFace[2][1] != 'white':
            self.moves = "B'"
            self.whiteCrossSolve += "B'"
            self.rotateBP()
        elif self.app.backFace[1][0] == 'white' and self.app.bottomFace[1][2] != 'white':
            rCount += 1
            if rCount % 4 == 0:
                self.moves = 'D'
                self.rotateD()
            else:
                self.moves = 'R'
                self.whiteCrossSolve += 'R'
                self.rotateR()
        elif self.app.frontFace[1][2] == 'white' and self.app.bottomFace[1][2] != 'white':
            self.moves = "R'"
            self.whiteCrossSolve += "R'"
            self.rotateRP()

        #checking bottom row to move into middle row
        elif (self.app.frontFace[2][1] == 'white' and self.app.bottomFace[0][1] != 'white'):
            self.moves = 'F'
            self.whiteCrossSolve += 'F'
            self.rotateF()
        elif (self.app.rightFace[2][1] == 'white' and self.app.bottomFace[1][2] != 'white'):
            self.moves = 'R'
            self.whiteCrossSolve += 'R'
            self.rotateR()
        elif (self.app.backFace[2][1] == 'white' and self.app.bottomFace[2][1] != 'white'):
            self.moves = 'B'
            self.whiteCrossSolve += 'B'
            self.rotateB()
        elif (self.app.leftFace[2][1] == 'white' and self.app.bottomFace[1][0] != 'white'):
            self.moves = 'L'
            self.whiteCrossSolve += 'L'
            self.rotateL()
        #checking upper row to move into middle row
        elif (self.app.frontFace[0][1] == 'white' and self.app.bottomFace[0][1] != 'white'):
            self.moves = 'F'
            self.whiteCrossSolve += 'F'
            self.rotateF()
        elif (self.app.rightFace[0][1] == 'white' and self.app.bottomFace[1][2] != 'white'):
            self.moves = 'R'
            self.whiteCrossSolve += 'R'
            self.rotateR()
        elif (self.app.backFace[0][1] == 'white' and self.app.bottomFace[2][1] != 'white'):
            self.moves = 'B'
            self.whiteCrossSolve += 'B'
            self.rotateB()
        elif (self.app.leftFace[0][1] == 'white' and self.app.bottomFace[1][0] != 'white'):
            self.moves = 'L'
            self.whiteCrossSolve += 'L'
            self.rotateL()
        else:
            self.moves = 'D'
            self.whiteCrossSolve += 'D'
            self.rotateD()
    if (self.app.bottomFace[0][1] == 'white' and self.app.bottomFace[1][2] == 'white' and
        self.app.bottomFace[1][0] == 'white' and self.app.bottomFace[2][1] == 'white'):
        self.whiteCrossIsNotSolved = False

def flipWhiteCross(self):
    if self.wcFront == False:
        flipWhiteCrossFront(self)
    elif self.wcRight == False:
        flipWhiteCrossRight(self)
    elif self.wcBack == False:
        flipWhiteCrossBack(self)
    elif self.wcLeft == False:
        flipWhiteCrossLeft(self)
    else:
        self.whiteCrossNotFlipped = False

def flipWhiteCrossFront(self):
    if self.app.frontFace[1][1] == self.app.frontFace[2][1] and self.app.bottomFace[0][1] == 'white':
        self.moves = 'F2'
        self.whiteCrossSolve += 'FF'
        self.rotateF()
        self.rotateF()
        self.wcFront = True
    else:
        self.whiteCrossSolve += 'D'
        self.moves = 'D'
        self.rotateD()

def flipWhiteCrossRight(self):
    if self.app.rightFace[1][1] == self.app.rightFace[2][1] and self.app.bottomFace[1][2] == 'white':
        self.moves = 'R2'
        self.whiteCrossSolve += 'RR'
        self.rotateR()
        self.rotateR()
        self.wcRight = True
    else:
        self.moves = 'D'
        self.whiteCrossSolve += 'D'
        self.rotateD()

def flipWhiteCrossBack(self):
    if self.app.backFace[1][1] == self.app.backFace[2][1] and self.app.bottomFace[2][1] == 'white':
        self.whiteCrossSolve += 'BB'
        self.moves = 'B2'
        self.rotateB()
        self.rotateB()
        self.wcBack = True
    else:
        self.moves = 'D'
        self.whiteCrossSolve += 'D'
        self.rotateD()

def flipWhiteCrossLeft(self):
    if self.app.leftFace[1][1] == self.app.leftFace[2][1] and self.app.bottomFace[1][0] == 'white':
        self.moves = 'L2'
        self.whiteCrossSolve += "LL"
        self.rotateL()
        self.rotateL()
        self.wcLeft = True
    else:
        self.moves = 'D'
        self.whiteCrossSolve += "D"
        self.rotateD()

def solveWhiteCorner(self):
    if not self.bcLeft:
        whiteCorner(self)


    # cases based on the location of the piece
def whiteCorner(self):
    cornerNotAdjusted = [self.fcrNotAdjusted, self.fclNotAdjusted,
                         self.bcrNotAdjusted, self.bclNotAdjusted,
                         False]
    if self.fcrNotAdjusted: 
        i = 0 
    elif self.fclNotAdjusted: 
        fixFCRPosition(self)
        i = 1
    elif self.bcrNotAdjusted: 
        fixFCLPosition(self)
        i = 2
    elif self.bclNotAdjusted:
        fixBCRPosition(self)
        i = 3
    else:
        i = 4
        fixBCLPosition(self) 
        self.whiteFaceIsNotSolved = False
    findCornerPosition(self)
    if cornerNotAdjusted[i]:
        adjustCornerPosition(self)

def fixFCRPosition(self):
    if self.fcRightPosition == 5:
        if self.app.frontFace[2][2] == 'white':
            self.moves = "F D F'"
            self.whiteFaceSolve += "FDF'"
            self.rotateF()
            self.rotateD()
            self.rotateFP()
        elif self.app.bottomFace[0][2] == 'white':
            self.moves = "F L D D L' F'"
            self.whiteFaceSolve += "FLDDL'F'"
            self.rotateF()
            self.rotateL()
            self.rotateD()
            self.rotateD()
            self.rotateLP()
            self.rotateFP()
        elif self.app.rightFace[2][0] == 'white':
            self.moves = "R 'D' R"
            self.whiteFaceSolve = "R'D'R"
            self.rotateRP()
            self.rotateDP()
            self.rotateR()
        self.fcRight = True

def fixFCLPosition(self):
    if self.fcLeftPosition == 6: 
        if self.app.frontFace[2][0] == 'white':
            self.moves = "F' D' F"
            self.whiteFaceSolve += "F'D'F"
            self.rotateFP()
            self.rotateDP()
            self.rotateF()
        elif self.app.bottomFace[0][0] == 'white':
            self.moves = "L B D D B' L'"
            self.whiteFaceSolve += "LBDDB'L'"
            self.rotateL()
            self.rotateB()
            self.rotateD()
            self.rotateD()
            self.rotateBP()
            self.rotateLP()
        elif self.app.leftFace[2][2] == 'white':
            self.moves = "L D L'"
            self.whiteFaceSolve += "LDL'"
            self.rotateL()
            self.rotateD()
            self.rotateLP()
        self.fcLeft = True

def fixBCRPosition(self):
    if self.bcRightPosition == 7:
        if self.app.backFace[2][0] == 'white':
            self.moves = "B' D' B"
            self.whiteFaceSolve += "B'D'B"
            self.rotateBP()
            self.rotateDP()
            self.rotateB()
        elif self.app.bottomFace[2][2] == 'white':
            self.moves = "B' L' D D L B"
            self.whiteFaceSolve += "B'L'DDLB"
            self.rotateBP()
            self.rotateLP()
            self.rotateD()
            self.rotateD()
            self.rotateL()
            self.rotateB()
        elif self.app.rightFace[2][2] == 'white':
            self.moves = "R D R'"
            self.whiteFaceSolve += "RDR'"
            self.rotateR()
            self.rotateD()
            self.rotateRP()
        self.bcRight = True

def fixBCLPosition(self):
    if self.bcLeftPosition == 8:
        if self.app.backFace[2][2] == 'white':
            self.moves = "B D B'"
            self.whiteFaceSolve += "BDB'"
            self.rotateB()
            self.rotateD()
            self.rotateBP()
        elif self.app.bottomFace[2][0] == 'white':
            self.moves = "B R D D R' B'"
            self.whiteFaceSolve += "BRDDR'B'"
            self.rotateB()
            self.rotateR()
            self.rotateD()
            self.rotateD()
            self.rotateRP()
            self.rotateBP()
        elif self.app.leftFace[2][0] == 'white':
            self.moves = "L' D' L"
            self.whiteFaceSolve += "L'D'L"
            self.rotateLP()
            self.rotateDP()
            self.rotateL()
        self.bcLeft = True

    # adjusts corner piece to correct position prior to insertion
def adjustCornerPosition(self):
    positionMap = [self.fcRightPosition, self.fcLeftPosition,
                   self.bcRightPosition, self.bcLeftPosition]
    positionPlace = [5, 6, 7, 8]

    if self.fcrNotAdjusted: i = 0
    elif self.fclNotAdjusted: i = 1
    elif self.bcrNotAdjusted: i = 2
    elif self.bclNotAdjusted: i = 3

    positionToCheck = positionMap[i]
    if positionToCheck == positionPlace[i]:
        if i == 0: self.fcrNotAdjusted = False
        elif i == 1: self.fclNotAdjusted = False
        elif i == 2: self.bcrNotAdjusted = False
        elif i == 3: self.bclNotAdjusted = False
    elif positionToCheck > 4:
        self.moves = 'D'
        self.whiteFaceSolve += "D"
        self.rotateD()
    elif positionToCheck == 1:
        self.moves += "R' D' R"
        self.whiteFaceSolve += "R'D'R"
        self.rotateRP()
        self.rotateDP()
        self.rotateR()
    elif positionToCheck == 2:
        self.moves += "L D L'"
        self.whiteFaceSolve += "LDL'"
        self.rotateL()
        self.rotateD()
        self.rotateLP()
    elif positionToCheck == 3:
        self.moves += "R D R'"
        self.whiteFaceSolve += "RDR'"
        self.rotateR()
        self.rotateD()
        self.rotateRP()
    elif positionToCheck == 4:
        self.moves += "L' D' L"
        self.whiteFaceSolve += "L'D'L"
        self.rotateLP()
        self.rotateDP()
        self.rotateL()
        
        # locates the corner piece
def findCornerPosition(self):
    # faceColor: fcr, fcl, bcr, bcl
    faceColor = [ ['green', 'white', 'red'],
                  ['green', 'white', 'orange'],
                  ['blue', 'white', 'red'],
                  ['blue', 'white', 'orange'],
                  [] ]
    i = 4
    if self.fcRight == False: i = 0
    elif self.fcLeft == False: i = 1
    elif self.bcRight == False: i = 2
    elif self.bcLeft == False: i = 3

    if ((self.app.frontFace[0][2] in faceColor[i]) and
        (self.app.rightFace[0][0] in faceColor[i]) and
        (self.app.upperFace[2][2] in faceColor[i])):
        cornerPosition = 1
    elif ((self.app.frontFace[0][0] in faceColor[i]) and
        (self.app.leftFace[0][2] in faceColor[i]) and
        (self.app.upperFace[2][0] in faceColor[i])):
        cornerPosition = 2
    elif ((self.app.backFace[0][0] in faceColor[i]) and
        (self.app.rightFace[0][2] in faceColor[i]) and
        (self.app.upperFace[0][2] in faceColor[i])):
        cornerPosition = 3
    elif ((self.app.backFace[0][2] in faceColor[i]) and
        (self.app.leftFace[0][0] in faceColor[i]) and
        (self.app.upperFace[0][0] in faceColor[i])):
        cornerPosition = 4
    elif ((self.app.frontFace[2][2] in faceColor[i]) and
        (self.app.rightFace[2][0] in faceColor[i]) and
        (self.app.bottomFace[0][2] in faceColor[i])):
        cornerPosition = 5
    elif ((self.app.frontFace[2][0] in faceColor[i]) and
        (self.app.leftFace[2][2] in faceColor[i]) and
        (self.app.bottomFace[0][0] in faceColor[i])):
        cornerPosition = 6
    elif ((self.app.backFace[2][0] in faceColor[i]) and
        (self.app.rightFace[2][2] in faceColor[i]) and
        (self.app.bottomFace[2][2] in faceColor[i])):
        cornerPosition = 7
    elif ((self.app.backFace[2][2] in faceColor[i]) and
        (self.app.leftFace[2][0] in faceColor[i]) and
        (self.app.bottomFace[2][0] in faceColor[i])):
        cornerPosition = 8
    if self.fcRight == False: 
        self.fcRightPosition = cornerPosition
    elif self.fcLeft == False: 
        self.fcRightPosition = 0
        self.fcLeftPosition = cornerPosition 
    elif self.bcRight == False: 
        self.fcLeftPosition = 0
        self.bcRightPosition = cornerPosition
    elif self.bcLeft == False: 
        self.bcRightPosition = 0
        self.bcLeftPosition = cornerPosition
    else:
        self.bcLeftPosition = 0

def solveSecondLayer(self):
    if not self.beLeft:
        self.moves = ''
        secondLayer(self)
    else:
        self.secondLayerNotSolved = False

    # cases for second layer edges based on pieces
def secondLayer(self):
    edgeNotAdjusted = [self.ferNotAdjusted, self.felNotAdjusted,
                       self.berNotAdjusted, self.belNotAdjusted,
                       False]
    if self.ferNotAdjusted: 
        i = 0 
    elif self.felNotAdjusted: 
        fixFERPosition(self)
        i = 1
    elif self.berNotAdjusted: 
        fixFELPosition(self)
        i = 2
    elif self.belNotAdjusted:
        fixBERPosition(self)
        i = 3
    else:
        i = 4
        fixBELPosition(self) 
    findEdgePosition(self)
    if edgeNotAdjusted[i]:
        adjustEdgePosition(self)

def fixFERPosition(self):
    if self.feRightPosition == 5:
        if self.app.frontFace[2][1] == 'green':
            self.moves = "D' R' D R F' R F R'"
            self.secondLayerSolve += "D'R'DRF'RFR'"
            self.rotateDP()
            self.rotateRP()
            self.rotateD()
            self.rotateR()
            self.rotateFP()
            self.rotateR()
            self.rotateF()
            self.rotateRP()
        else:
            self.moves = "D D F D' F' R F' R' F"
            self.secondLayerSolve += "DDFD'F'RF'R'F"
            self.rotateD()
            self.rotateD()
            self.rotateF()
            self.rotateDP()
            self.rotateFP()
            self.rotateR()
            self.rotateFP()
            self.rotateRP()
            self.rotateF()
        self.feRight = True

def fixFELPosition(self):
    if self.feLeftPosition == 5:
        if self.app.frontFace[2][1] == 'green':
            self.moves = "D L D' L' F L' F' L"
            self.secondLayerSolve += "DLD'L'FL'F'L"
            self.rotateD()
            self.rotateL()
            self.rotateDP()
            self.rotateLP()
            self.rotateF()
            self.rotateLP()
            self.rotateFP()
            self.rotateL()
        else:
            self.moves = "D D F' D F L' F L F'"
            self.secondLayerSolve += "DDF'DFL'FLF'"
            self.rotateD()
            self.rotateD()
            self.rotateFP()
            self.rotateD()
            self.rotateF()
            self.rotateLP()
            self.rotateF()
            self.rotateL()
            self.rotateFP()
        self.feLeft = True
            
def fixBERPosition(self):
    if self.beRightPosition == 7:
        if self.app.backFace[2][1] == 'blue':
            self.moves = "D R D' R' B R' B' R"
            self.secondLayerSolve += "DRD'R'BR'B'R"
            self.rotateD()
            self.rotateR()
            self.rotateDP()
            self.rotateRP()
            self.rotateB()
            self.rotateRP()
            self.rotateBP()
            self.rotateR()
        else:
            self.moves =  "D D B' D B R' B R B'"
            self.secondLayerSolve += "DDB'DBR'BRB'"
            self.rotateD()
            self.rotateD()
            self.rotateBP()
            self.rotateD()
            self.rotateB()
            self.rotateRP()
            self.rotateB()
            self.rotateR()
            self.rotateBP()
        self.beRight = True

def fixBELPosition(self):
    if self.beLeftPosition == 7:
        if self.app.backFace[2][1] == 'blue':
            self.moves = "D' L' D L B' L B L'"
            self.secondLayerSolve += "D'L'DLB'LBL'"
            self.rotateDP()
            self.rotateLP()
            self.rotateD()
            self.rotateL()
            self.rotateBP()
            self.rotateL()
            self.rotateB()
            self.rotateLP()
        else:
            self.moves = "D D B D' B' L B' L' B"
            self.secondLayerSolve += "DDBD'B'LB'L'B"
            self.rotateD()
            self.rotateD()
            self.rotateB()
            self.rotateDP()
            self.rotateBP()
            self.rotateL()
            self.rotateBP()
            self.rotateLP()
            self.rotateB()
        self.beLeft = True

def findEdgePosition(self):
    edgeColor = [ ['green', 'red'], ['green', 'orange'], 
                  ['blue', 'red'], ['blue', 'orange'], 
                  [] ]

    i = 4
    if self.feRight == False: i = 0
    elif self.feLeft == False: i = 1
    elif self.beRight == False: i = 2
    elif self.beLeft == False: i = 3

    if ((self.app.frontFace[1][2] in edgeColor[i]) and
         self.app.rightFace[1][0] in edgeColor[i]):
         edgePosition = 1
    if ((self.app.frontFace[1][0] in edgeColor[i]) and
         self.app.leftFace[1][2] in edgeColor[i]):
         edgePosition = 2
    if ((self.app.backFace[1][0] in edgeColor[i]) and
         self.app.rightFace[1][2] in edgeColor[i]):
         edgePosition = 3
    if ((self.app.backFace[1][2] in edgeColor[i]) and
         self.app.leftFace[1][0] in edgeColor[i]):
         edgePosition = 4
    if ((self.app.frontFace[2][1] in edgeColor[i]) and
         self.app.bottomFace[0][1] in edgeColor[i]):
         edgePosition = 5
    if ((self.app.rightFace[2][1] in edgeColor[i]) and
         self.app.bottomFace[1][2] in edgeColor[i]):
         edgePosition = 6
    if ((self.app.backFace[2][1] in edgeColor[i]) and
         self.app.bottomFace[2][1] in edgeColor[i]):
         edgePosition = 7
    if ((self.app.leftFace[2][1] in edgeColor[i]) and
         self.app.bottomFace[1][0] in edgeColor[i]):
         edgePosition = 8

    if self.feRight == False: 
        self.feRightPosition = edgePosition
    elif self.feLeft == False: 
        self.feRightPosition = 0
        self.feLeftPosition = edgePosition 
    elif self.beRight == False: 
        self.feLeftPosition = 0
        self.beRightPosition = edgePosition
    elif self.beLeft == False: 
        self.beRightPosition = 0
        self.beLeftPosition = edgePosition
    else:
        self.beLeftPosition = 0

def adjustEdgePosition(self):
    positionMap = [self.feRightPosition, self.feLeftPosition,
                   self.beRightPosition, self.beLeftPosition]

    positionPlace = [5, 5, 7, 7]

    if self.ferNotAdjusted: i = 0
    elif self.felNotAdjusted: i = 1
    elif self.berNotAdjusted: i = 2
    elif self.belNotAdjusted: i = 3
    positionToCheck = positionMap[i]

    if positionToCheck == positionPlace[i]:
        if i == 0: self.ferNotAdjusted = False
        elif i == 1: self.felNotAdjusted = False
        elif i == 2: self.berNotAdjusted = False
        elif i == 3: self.belNotAdjusted = False

    elif positionToCheck > 4:
        self.moves += 'D'
        self.secondLayerSolve += 'D'
        self.rotateD()
    elif positionToCheck == 1:
        self.moves += "R' D R F' R F R'"
        self.secondLayerSolve += "R'DRF'RFR'"
        self.rotateRP()
        self.rotateD()
        self.rotateR()
        self.rotateFP()
        self.rotateR()
        self.rotateF()
        self.rotateRP()
    elif positionToCheck == 2:
        self.moves += "L D' L' F L' F' L"
        self.secondLayerSolve += "LD'L'FL'F'L"
        self.rotateL()
        self.rotateDP()
        self.rotateLP()
        self.rotateF()
        self.rotateLP()
        self.rotateFP()
        self.rotateL()
    elif positionToCheck == 3:
        self.moves += "R D' R' B R' B' R"
        self.secondLayerSolve += "RD'R'BR'B'R"
        self.rotateR()
        self.rotateDP()
        self.rotateRP()
        self.rotateB()
        self.rotateRP()
        self.rotateBP()
        self.rotateR()
    elif positionToCheck == 4:
        self.moves += "L' D L B' L B L'"
        self.secondLayerSolve += "L'DLB'LBL'"
        self.rotateLP()
        self.rotateD()
        self.rotateL()
        self.rotateBP()
        self.rotateL()
        self.rotateB()
        self.rotateLP()

def solveYellowCross(self): 
    if self.yellowLNotSolved:
        solveYellowL(self)
    elif ((self.app.bottomFace[0][1] == 'yellow') and 
          (self.app.bottomFace[1][0] == 'yellow') and
          (self.app.bottomFace[1][1] == 'yellow') and
          (self.app.bottomFace[1][2] == 'yellow') and
          (self.app.bottomFace[2][1] == 'yellow')):
          self.yellowCrossNotSolved = False
    elif self.yellowCrossNotSolved:
        self.moves = "F D L D' L' F'"
        self.yellowCrossSolve += "FDLD'L'F'"
        self.rotateF()
        self.rotateD()
        self.rotateL()
        self.rotateDP()
        self.rotateLP()
        self.rotateFP()

def solveYellowL(self):
    for _ in range(4):
        if checkYellowL(self):
            self.yellowLNotSolved = False
            break
        else:
            self.moves = 'D'
            self.yellowCrossSolve += 'D'
            self.rotateD()
    if self.yellowLNotSolved:
        self.moves = "F L D L' D' F'"
        self.yellowCrossSolve += "FLDL'D'F'"
        self.rotateF()
        self.rotateL()
        self.rotateD()
        self.rotateLP()
        self.rotateDP()
        self.rotateFP() 
       
def checkYellowL(self):
    if ((self.app.bottomFace[2][1] == 'yellow') and 
        (self.app.bottomFace[1][2] == 'yellow') and
        (self.app.bottomFace[1][1] == 'yellow')):
        return True

def solveYellowFace(self):
    if self.yellowFaceNotSolved:
        yellowCount = getYellowCount(self)
        if yellowCount == 6:
            if self.app.bottomFace[0][2] != 'yellow':
                self.moves = 'D'
                self.yellowFaceSolve += 'D'
                self.rotateD()
            elif self.app.frontFace[2][0] == 'yellow':
                doSune(self)
            else:
                self.moves = 'D'
                self.yellowFaceSolve += 'D'
                self.rotateD()
                doAntiSune(self)
        elif yellowCount == 7:
            if self.app.frontFace[2][0] != 'yellow':
                self.moves = 'D'
                self.yellowFaceSolve += 'D'
                self.rotateD()
            doSune(self)
        elif yellowCount == 5:
            if self.app.leftFace[2][2] != 'yellow':
                self.moves = 'D'
                self.yellowFaceSolve += 'D'
                self.rotateD()
            doSune(self)
        elif yellowCount == 9:
            self.yellowFaceNotSolved = False

def getYellowCount(self):
    yellowCount = 0
    for row in range(self.faceRows):
        for col in range(self.faceCols):
            if self.app.bottomFace[row][col] == 'yellow':
                yellowCount += 1
    return yellowCount

def doSune(self):
    self.moves = "L D L' D L D D L'"
    self.yellowFaceSolve += "LDL'DLDDL'"
    self.rotateL()
    self.rotateD()
    self.rotateLP()
    self.rotateD()
    self.rotateL()
    self.rotateD()
    self.rotateD()
    self.rotateLP()

def doAntiSune(self):
    self.moves = "L' D' L D' L' D D L"
    self.yellowFaceSolve += "L'D'LD'L'DDL"
    self.rotateLP()
    self.rotateDP()
    self.rotateL()
    self.rotateDP()
    self.rotateLP()
    self.rotateD()
    self.rotateD()
    self.rotateL()

def permuteLastLayer(self):
    if self.matchingCornersNotSolved:
        solveMatchingCorners(self)
    elif self.matchingEdgesNotSolved:
        solveMatchingEdges(self)
    elif self.app.frontFace[2][0] != self.app.frontFace[1][1]:
        self.moves = 'D'
        self.permutationSolve += 'D'
        self.rotateD()
    else:
        self.cubeNotSolved = False

def solveMatchingCorners(self):
    if self.app.backFace[2][0] == self.app.backFace[2][2]:
        print('c1')
        doAPerm(self)
    elif self.app.rightFace[2][0] == self.app.rightFace[2][2]:
        print('c2')
        self.moves = 'D'
        self.permutationSolve += 'D'
        self.rotateD()
        doAPerm(self)
    elif self.app.frontFace[2][0] == self.app.frontFace[2][2]:
        print('c3')
        self.moves = 'D2'
        self.permutationSolve += 'DD'
        self.rotateD()
        self.rotateD()
        doAPerm(self)
    elif self.app.leftFace[2][0] == self.app.leftFace[2][2]:
        print('c4')
        self.moves = "D'"
        self.permutationSolve += "D'"
        self.rotateDP()
        doAPerm(self)
    else:
        print('c5')
        doAPerm(self)
    checkMatchingCorners(self)

def checkMatchingCorners(self):
    if ((self.app.backFace[2][0] == self.app.backFace[2][2]) and
        (self.app.rightFace[2][0] == self.app.rightFace[2][2]) and
        (self.app.frontFace[2][0] == self.app.frontFace[2][2]) and
        (self.app.leftFace[2][0] == self.app.leftFace[2][2])):
        self.matchingCornersNotSolved = False

def solveMatchingEdges(self):
    if self.app.backFace[2][0] == self.app.backFace[2][1] == self.app.backFace[2][2]:
        executeUPerm(self)
    elif self.app.rightFace[2][0] == self.app.rightFace[2][1] == self.app.rightFace[2][2]:
        self.permutationSolve += 'D'
        self.moves = 'D'
        self.rotateD()
        executeUPerm(self)    
    elif self.app.frontFace[2][0] == self.app.frontFace[2][1] == self.app.frontFace[2][2]:
        self.permutationSolve += 'DD'
        self.moves = 'D2'
        self.rotateD()
        self.rotateD()
        executeUPerm(self)       
    elif self.app.leftFace[2][0] == self.app.leftFace[2][1] == self.app.leftFace[2][2]:
        self.permutationSolve += "D'"
        self.moves = "D'"
        self.rotateDP()
        executeUPerm(self)
    elif self.app.frontFace[2][1] == self.app.rightFace[2][2]: 
        self.moves = 'D'
        self.permutationSolve += 'D'
        self.rotateD()
        doZPerm(self) 
    elif self.app.frontFace[2][1] == self.app.leftFace[2][2]:
        doZPerm(self)
    elif self.app.frontFace[2][0] == self.app.backFace[2][1]:
        doHPerm(self)
    checkMatchingEdges(self)

def checkMatchingEdges(self):
    if ((self.app.backFace[2][0] == self.app.backFace[2][1] == self.app.backFace[2][2]) and
        (self.app.rightFace[2][0] == self.app.rightFace[2][1] == self.app.rightFace[2][2]) and
        (self.app.frontFace[2][0] == self.app.frontFace[2][1] == self.app.frontFace[2][2]) and
        (self.app.leftFace[2][0] == self.app.leftFace[2][1] == self.app.leftFace[2][2])):
        self.matchingEdgesNotSolved = False

def executeUPerm(self):
    if self.app.frontFace[2][1] == self.app.rightFace[2][0]:
        doUPermA(self)
    else:
        doUPermB(self)

def doZPerm(self):
    self.moves = "M2 D M2 D M D2 M2 D2 M D2"
    self.permutationSolve += "MMDMMDMDDMMDDMDD"
    self.rotateM()
    self.rotateM()
    self.rotateD()
    self.rotateM()
    self.rotateM()
    self.rotateD()
    self.rotateM()
    self.rotateD()
    self.rotateD()
    self.rotateM()
    self.rotateM()
    self.rotateD()
    self.rotateD()
    self.rotateM()
    self.rotateD()
    self.rotateD()

def doHPerm(self):
    self.moves = 'M2 D M2 D2 M2 D M2'
    self.permutationSolve += 'MMDMMDDMMDMM'
    self.rotateM()
    self.rotateM()
    self.rotateD()
    self.rotateM()
    self.rotateM()
    self.rotateD()
    self.rotateD()
    self.rotateM()
    self.rotateM()
    self.rotateD()
    self.rotateM()
    self.rotateM()

def doAPerm(self):
    self.moves = "L' F L' B2 L F' L' B2 L2"
    self.permutationSolve += "L'FL'BBLF'L'BBLL"
    self.rotateLP()
    self.rotateF()
    self.rotateLP()
    self.rotateB()
    self.rotateB()
    self.rotateL()
    self.rotateFP()
    self.rotateLP()
    self.rotateB()
    self.rotateB()
    self.rotateL()
    self.rotateL()

def doUPermA(self):
    self.moves = "L2 D L D L' D' L' D' L' D L'"
    self.permutationSolve += "LLDLDL'D'L'D'L'DL'"
    self.rotateL()
    self.rotateL()
    self.rotateD()
    self.rotateL()
    self.rotateD()
    self.rotateLP()
    self.rotateDP()
    self.rotateLP()
    self.rotateDP()
    self.rotateLP()
    self.rotateD()
    self.rotateLP()

def doUPermB(self):
    self.moves = "L D' L D L D L D' L' D' L2"
    self.permutationSolve += "LD'LDLDLD'L'D'LL"
    self.rotateL()
    self.rotateDP()
    self.rotateL()
    self.rotateD()
    self.rotateL()
    self.rotateD()
    self.rotateL()
    self.rotateDP()
    self.rotateLP()
    self.rotateDP()
    self.rotateL()
    self.rotateL()