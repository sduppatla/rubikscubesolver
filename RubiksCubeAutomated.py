from RubiksCubeSolver import *

def solveCube(self):
    if self.cubeNotSolved:
        if self.whiteCrossIsNotSolved:
            self.solvePart = 'White Cross'
            solveWhiteCrossOnYellow(self)
        elif self.whiteCrossNotFlipped:
            self.solvePart = 'White Cross'
            flipWhiteCross(self)
        elif self.whiteFaceIsNotSolved:
            self.solvePart = 'White Face'
            solveWhiteCorner(self)
        elif self.secondLayerNotSolved:
            self.solvePart = 'Second Layer'
            solveSecondLayer(self)
        elif self.yellowCrossNotSolved:
            self.solvePart = 'Yellow Cross'
            solveYellowCross(self)
        elif self.yellowFaceNotSolved:
            self.solvePart = 'Yellow Face'
            solveYellowFace(self)
        else:
            self.solvePart = 'Last Layer'
            permuteLastLayer(self)
    else:
        self.solvePart = 'Solved!'