import math, copy, random
# CMU Graphics from: https://www.cs.cmu.edu/~112/notes/notes-animations-part2.html
from cmu_112_graphics import *
from tkinter import *
from RubiksCubeSolver import *
from RubiksCubeAutomated import *
from RubiksCubeExtras import *
from PIL import Image

def runRubiksCube():
    MyModalApp(width = 850, height = 650)

class RubiksCubeMode(Mode):
    def appStarted(self):
        self.margin = 25
        self.cellSize = (self.width - (2 * self.margin)) / 4 / 3
        self.cellLength = 80
        self.faceRows = 3
        self.faceCols = 3
        self.moveCount = 0
        self.timerDelay = 500
        self.createFace()
        self.setBooleans()
        self.scrambleKey = 'Manual Input'
        self.solveStrings()
        
    # Keeps track of which part of the cube needs to be solved
    def setBooleans(self):
        self.whiteCrossBooleans()
        self.whiteCornerBooleans()
        self.secondLayerBooleans()
        self.yellowFaceBooleans()
        self.permutationBooleans()
        self.cubeNotSolved = True

    def solveStrings(self):
        self.solve = ''
        self.whiteCrossSolve = ''
        self.whiteFaceSolve = ''
        self.secondLayerSolve = ''
        self.yellowCrossSolve = ''
        self.yellowFaceSolve = ''
        self.permutationSolve = ''


    def whiteCrossBooleans(self):
        self.whiteCrossIsNotSolved = True
        self.whiteCrossNotFlipped = True
        self.wcFront = False
        self.wcRight = False
        self.wcLeft = False
        self.wcBack = False

    def whiteCornerBooleans(self):
        self.whiteFaceIsNotSolved = True
        #fc, front corner, bc, back corner
        self.fcRight = False
        self.fcLeft = False
        self.bcRight = False
        self.bcLeft = False
        self.fcRightPosition = 0
        self.fcLeftPosition = 0
        self.bcRightPosition = 0
        self.bcLeftPosition = 0
        self.fcrNotAdjusted = True
        self.fclNotAdjusted = True
        self.bcrNotAdjusted = True
        self.bclNotAdjusted = True

    def secondLayerBooleans(self):
        self.secondLayerNotSolved = True
        #fe, front edge, be, back edge
        self.feRight = False
        self.feLeft = False
        self.beRight = False
        self.beLeft = False
        self.feRightPosition = 0
        self.feLeftPosition = 0
        self.beRightPosition = 0
        self.beLeftPosition = 0
        self.ferNotAdjusted = True
        self.felNotAdjusted = True
        self.berNotAdjusted = True
        self.belNotAdjusted = True

    def yellowFaceBooleans(self):
        self.yellowLNotSolved = True
        self.yellowCrossNotSolved = True
        self.yellowFaceNotSolved = True
    
    def permutationBooleans(self):
        self.matchingCornersNotSolved = True
        self.matchingEdgesNotSolved = True

    def createFace(self):
        self.faceList = [self.app.frontFace, self.app.upperFace, self.app.bottomFace, 
                         self.app.rightFace, self.app.backFace, self.app.leftFace]
        self.frontFaceStart = (self.margin + 3 * self.cellSize, 
                            self.margin + 3 * self.cellSize)
        self.upperFaceStart = (self.margin + 3 * self.cellSize, self.margin)
        self.bottomFaceStart = (self.margin + 3 * self.cellSize, 
                            self.margin + 6 * self.cellSize)
        self.rightFaceStart = (self.margin + 6 * self.cellSize, 
                            self.margin + 3 * self.cellSize)
        self.backFaceStart = (self.margin + 9 * self.cellSize, 
                            self.margin + 3 * self.cellSize)
        self.leftFaceStart = (self.margin, self.margin + 3 * self.cellSize)
        self.faceStartList = [self.frontFaceStart, self.upperFaceStart, 
                            self.bottomFaceStart, self.rightFaceStart, 
                            self.backFaceStart, self.leftFaceStart]

    def rotateR(self):
        self.solve += 'R'
        self.rotateFace(3)
        self.tempSide1 = copy.deepcopy([self.app.frontFace[row][2] for row in range(self.faceRows)]) 
        self.tempSide2 = copy.deepcopy([self.app.upperFace[row][2] for row in range(self.faceRows)]) 
        self.tempSide3 = copy.deepcopy([self.app.bottomFace[row][2] for row in range(self.faceRows)])
        self.tempSide4 = copy.deepcopy([self.app.backFace[row][0] for row in range(self.faceRows)])
        for row in range(self.faceRows):
            self.app.upperFace[row][2] = self.tempSide1[row]
            self.app.frontFace[row][2] = self.tempSide3[row]
            self.app.bottomFace[2 - row][2] = self.tempSide4[row]
            self.app.backFace[2 - row][0] = self.tempSide2[row]

    def rotateL(self):
        self.solve += 'L'
        self.rotateFace(5)
        self.tempSide1 = copy.deepcopy([self.app.frontFace[row][0] for row in range(self.faceRows)])
        self.tempSide2 = copy.deepcopy([self.app.upperFace[row][0] for row in range(self.faceRows)])
        self.tempSide3 = copy.deepcopy([self.app.bottomFace[row][0] for row in range(self.faceRows)])
        self.tempSide4 = copy.deepcopy([self.app.backFace[row][2] for row in range(self.faceRows)])
        for row in range(self.faceRows):
            self.app.upperFace[2 - row][0] = self.tempSide4[row]
            self.app.frontFace[row][0] = self.tempSide2[row]
            self.app.bottomFace[row][0] = self.tempSide1[row]
            self.app.backFace[2 - row][2] = self.tempSide3[row]

    def rotateM(self):
        self.solve += 'M'
        self.tempSide1 = copy.deepcopy([self.app.frontFace[row][1] for row in range(self.faceRows)])
        self.tempSide2 = copy.deepcopy([self.app.upperFace[row][1] for row in range(self.faceRows)])
        self.tempSide3 = copy.deepcopy([self.app.bottomFace[row][1] for row in range(self.faceRows)])
        self.tempSide4 = copy.deepcopy([self.app.backFace[row][1] for row in range(self.faceRows)])
        for row in range(self.faceRows):
            self.app.upperFace[row][1] = self.tempSide1[row]
            self.app.frontFace[2 - row][1] = self.tempSide3[row]
            self.app.bottomFace[row][1] = self.tempSide4[row]
            self.app.backFace[2 - row][1] = self.tempSide2[row]

    def rotateU(self):
        self.solve += 'U'
        self.rotateFace(1)
        self.tempSide1 = copy.deepcopy([self.app.frontFace[0][col] for col in range(self.faceCols)])
        self.tempSide2 = copy.deepcopy([self.app.leftFace[0][col] for col in range(self.faceCols)])
        self.tempSide3 = copy.deepcopy([self.app.rightFace[0][col] for col in range(self.faceCols)])
        self.tempSide4 = copy.deepcopy([self.app.backFace[0][col] for col in range(self.faceCols)])
        for col in range(self.faceCols):
            self.app.leftFace[0][col] = self.tempSide1[col]
            self.app.backFace[0][col] = self.tempSide2[col]
            self.app.frontFace[0][col] = self.tempSide3[col]
            self.app.rightFace[0][col] = self.tempSide4[col]

    def rotateD(self):
        self.solve += 'D'
        self.rotateFace(2)
        self.tempSide1 = copy.deepcopy([self.app.frontFace[2][col] for col in range(self.faceCols)])
        self.tempSide2 = copy.deepcopy([self.app.leftFace[2][col] for col in range(self.faceCols)])
        self.tempSide3 = copy.deepcopy([self.app.rightFace[2][col] for col in range(self.faceCols)])
        self.tempSide4 = copy.deepcopy([self.app.backFace[2][col] for col in range(self.faceCols)])
        for col in range(self.faceCols):
            self.app.leftFace[2][col] = self.tempSide4[col]
            self.app.backFace[2][col] = self.tempSide3[col]
            self.app.frontFace[2][col] = self.tempSide2[col]
            self.app.rightFace[2][col] = self.tempSide1[col]

    def rotateF(self):
        self.solve += 'F'
        self.rotateFace(0)
        self.tempUpperSide = copy.deepcopy([self.app.upperFace[2][col] for col in range(self.faceCols)])
        self.tempRightSide = copy.deepcopy([self.app.rightFace[row][0] for row in range(self.faceRows)])
        self.tempBottomSide = copy.deepcopy([self.app.bottomFace[0][col] for col in range(self.faceCols)])
        self.tempLeftSide = copy.deepcopy([self.app.leftFace[row][2] for row in range(self.faceRows)])
        for col in range(self.faceCols):
            self.app.bottomFace[0][2 - col] = self.tempRightSide[col]
            self.app.upperFace[2][2 - col] = self.tempLeftSide[col]
        for row in range(self.faceRows):
            self.app.rightFace[row][0] = self.tempUpperSide[row]
            self.app.leftFace[row][2] = self.tempBottomSide[row]

    def rotateB(self):
        self.solve += 'B'
        self.rotateFace(4)
        self.tempUpperSide = copy.deepcopy([self.app.upperFace[0][col] for col in range(self.faceCols)])
        self.tempRightSide = copy.deepcopy([self.app.rightFace[row][2] for row in range(self.faceRows)])
        self.tempBottomSide = copy.deepcopy([self.app.bottomFace[2][col] for col in range(self.faceCols)])
        self.tempLeftSide = copy.deepcopy([self.app.leftFace[row][0] for row in range(self.faceRows)])
        for col in range(self.faceCols):
            self.app.bottomFace[2][col] = self.tempLeftSide[col]
            self.app.upperFace[0][col] = self.tempRightSide[col]
        for row in range(self.faceRows):
            self.app.rightFace[2 - row][2] = self.tempBottomSide[row]
            self.app.leftFace[2 -row][0] = self.tempUpperSide[row]

    def rotateRP(self):
        for _ in range(3):
            self.rotateR()

    def rotateLP(self):
        for _ in range(3):
            self.rotateL()

    def rotateUP(self):
        for _ in range(3):
            self.rotateU()

    def rotateDP(self):
        for _ in range(3):
            self.rotateD()

    def rotateFP(self):
        for _ in range(3):
            self.rotateF()

    def rotateBP(self):
        for _ in range(3):
            self.rotateB()

    def rotateMP(self):
        for _ in range(3):
            self.rotateM()

    def rotateFace(self, index):
        face = copy.deepcopy(self.faceList[index])
        for row in range(len(face)):
            for col in range(len(face[0])):
                newRow = len(face) - 1 - col
                newCol = row
                self.faceList[index][row][col] = face[newRow][newCol]

    def scramble(self):
        self.scrambleKey = ''
        self.cubeNotSolved = True
        faces = 6
        moveNames = ['F', 'B', 'U', 'D', 'R', 'L']
        for scrambleMove in range(15):
            i = random.randint(0, faces - 1)
            self.scrambleKey += moveNames[i]
            if i == 0: self.rotateF()
            elif i == 1: self.rotateB()
            elif i == 2: self.rotateU()
            elif i == 3: self.rotateD()
            elif i == 4: self.rotateR()
            elif i == 5: self.rotateL()

    def drawCubeSchematic(self, canvas):
        self.drawFace(canvas)

    def drawFace(self, canvas):
        for i in range(len(self.faceList)):
            xStart, yStart = self.faceStartList[i]
            for row in range(self.faceRows):
                for col in range(self.faceCols):
                    x1 = xStart + col * self.cellSize
                    x2 = x1 + self.cellSize
                    y1 = yStart + row * self.cellSize
                    y2 = y1 + self.cellSize
                    color = self.faceList[i][row][col]
                    canvas.create_rectangle(x1, y1, x2, y2, fill = color)
    
    def printInput(self):
        print(f"White Cross = {self.whiteCrossSolve}")
        print(f"White Face = {self.whiteFaceSolve}")
        print(f"Second Layer = {self.secondLayerSolve}")
        print(f"Yellow Cross = {self.yellowCrossSolve}")
        print(f"Yellow Face = {self.yellowFaceSolve}")
        print(f"Last Layer = {self.permutationSolve}")

    def rescramble(self):
        for c in self.solve:
            if c == 'R':
                self.rotateR()
            elif c == 'L':
                self.rotateL()
            elif c == 'B':
                self.rotateB()
            elif c == 'F':
                self.rotateF()
            elif c == 'D':
                self.rotateD()
            elif c == 'U':
                self.rotateU()
            elif c == 'M':
                self.rotateM()

    def keyPressed(self, event):
        if event.key == '1':
            self.app.setActiveMode(self.app.splashScreenMode)
        elif event.key == '2':
            self.app.setActiveMode(self.app.gameMode)
        elif event.key == '3':
            self.app.setActiveMode(self.app.gameMode3D)
        elif event.key == '4':
            self.app.setActiveMode(self.app.manualInputMode)
        elif event.key == 'h':
            self.app.setActiveMode(self.app.helpMode)
        if event.key == 't':
            self.rescramble()
        if event.key == 'q':
            self.printInput()
        if event.key == 'Space':
            solveCube(self)
        if event.key == 'k':
            print('Long Solve: ' + self.solve)
            fixSolveString(self)
            print('Solve: ' + self.solve)
            print('Scramble: ' + self.scrambleKey)
        if event.key == 'a':
            self.appStarted()
        if event.key == 's':
            self.setBooleans()
            self.scramble()
            self.solve = ''
        self.moveKeys(event)

    # Moves to rotate around the cube!
    def moveKeys(self, event):
        if event.key == 'r':
            self.rotateR()
        if event.key == 'R':
            self.rotateRP()
        if event.key == 'l':
            self.rotateL()
        if event.key == 'L':
            self.rotateLP()
        if event.key == 'm':
            self.rotateM()
        if event.key == 'M':
            self.rotateM()
        if event.key == 'u':
            self.rotateU()
        if event.key == 'U':
            self.rotateUP()
        if event.key == 'd':
            self.rotateD()
        if event.key == 'D':
            self.rotateDP()
        if event.key == 'f':
            self.rotateF()
        if event.key == 'F':
            self.rotateFP()
        if event.key == 'b':
            self.rotateB()
        if event.key == 'B':
            self.rotateBP()

    def redrawAll(self, canvas):
        self.drawCubeSchematic(canvas)
        canvas.create_text(5, self.height // 20 - 10, font = 'Arial 15 bold', 
                        text = "Navigation: ", anchor = 'w')
        canvas.create_text(5, self.height // 20 + 10, 
                        text = '1: Loading Screen', anchor = 'w')
        canvas.create_text(5, self.height // 20 + 20,
                        text = '2: 2D Solve Screen', anchor = 'w')
        canvas.create_text(5, self.height // 20 + 30,
                        text = '3: 3D Solve Screen', anchor = 'w')
        canvas.create_text(5, self.height // 20 + 40, 
                        text = '4: Input Screen', anchor = 'w')
        canvas.create_text(5, self.height // 20 + 50,
                        text = 'h: Help Screen', anchor = 'w')
        canvas.create_text(10, self.height - 10, text="Solve so far: " + self.solve, anchor = 'w')

# Redraws 2D Cube in 3D
class RubiksCube3DMode(RubiksCubeMode):
    def appStarted(self):
        super().appStarted()
        self.oIndex = 0
        self.oIndexRow = 0
        self.solvePart = 'None'
        self.moves = ''

    # Arrow keys to navigate cube
    def keyPressed(self, event):
        super().keyPressed(event)
        if event.key == 'Right':
            self.rotateOrientationRight()
        elif event.key == 'Left':
            self.rotateOrientationLeft()
        elif event.key == 'Up':
            self.rotateOrientationUp()
        elif event.key == 'Down':
            self.rotateOrientationDown()

    # Allows for tracking the progress of solve
    def setBooleans(self):
        super().setBooleans()

    def rotateOrientationRight(self):
        self.oIndex = (self.oIndex - 1) % 4
    
    def rotateOrientationLeft(self):
        self.oIndex = (self.oIndex + 1) % 4

    def rotateOrientationUp(self):
        self.oIndexRow = (self.oIndexRow + 1) % 2

    def rotateOrientationDown(self):
        self.oIndexRow = (self.oIndexRow - 1) % 2

    def drawTopFace(self, canvas):
        xStart, yStart = self.width / 2 + self.cellLength, 50 - self.cellLength / 2
        for row in range(self.faceRows):
            xStart -= self.cellLength
            yStart += self.cellLength / 2
            self.drawTopFaceHelper(canvas, xStart, yStart, row)

    # Math from: http://clintbellanger.net/articles/isometric_math/
    # Used to calculate isometric coordinates
    def drawTopFaceHelper(self, canvas, xS, yS, row):
        self.faceTopList = [self.app.upperFace, self.app.bottomFace]
        for col in range(self.faceCols):
            x1 = xS + col * self.cellLength
            y1 = yS + col * self.cellLength / 2
            x2 = x1 + self.cellLength
            y2 = y1 + self.cellLength / 2
            x3 = x1
            y3 = y2 + self.cellLength / 2
            x4 = x1 - self.cellLength
            y4 = y2
            color = self.faceTopList[self.oIndexRow][row][col]
            if self.oIndexRow == 0:
                if self.oIndex == 0:
                    color = self.faceTopList[self.oIndexRow][row][col]
                elif self.oIndex == 1:
                    color = self.faceTopList[self.oIndexRow][2 - col][row]
                elif self.oIndex == 2:
                    color = self.faceTopList[self.oIndexRow][2 - row][2 - col]
                elif self.oIndex == 3:
                    color = self.faceTopList[self.oIndexRow][col][2 - row]
            elif self.oIndexRow == 1:
                if self.oIndex == 1:
                    color = self.faceTopList[self.oIndexRow][row][col]
                elif self.oIndex == 2:
                    color = self.faceTopList[self.oIndexRow][2 - col][row]
                elif self.oIndex == 3:
                    color = self.faceTopList[self.oIndexRow][2 - row][2 - col]
                elif self.oIndex == 0:
                    color = self.faceTopList[self.oIndexRow][col][2 - row]
            canvas.create_polygon(x1, y1, x2, y2, x3, y3, x4, y4, 
            fill = color, outline = 'black', width = '1')
    
    def drawRightFace(self, canvas):
        xStart, yStart = self.width / 2, 50 + (2 * self.cellLength)
        for row in range(self.faceRows):
            yStart += self.cellLength
            self.drawRightFaceHelper(canvas, xStart, yStart, row)
    
    def drawRightFaceHelper(self, canvas, xS, yS, row):
        self.faceRightList = [[self.app.rightFace, self.app.backFace,
                               self.app.leftFace, self.app.frontFace],
                              [self.app.backFace, self.app.rightFace, 
                               self.app.frontFace, self.app.leftFace]]
        for col in range(self.faceCols):
            x1 = xS + col * self.cellLength
            y1 = yS - col * self.cellLength / 2
            x2 = x1 + self.cellLength
            y2 = y1 - self.cellLength / 2
            x3 = x2
            y3 = y1 + self.cellLength / 2
            x4 = x1
            y4 = y1 + self.cellLength
            if self.oIndexRow == 0:
                color = self.faceRightList[self.oIndexRow][self.oIndex][row][col]
            elif self.oIndexRow == 1:
                color = self.faceRightList[self.oIndexRow][self.oIndex][2 -row][2 -col]
            canvas.create_polygon(x1, y1, x2, y2, x3, y3, x4, y4, 
            fill = color, outline = 'black', width = '1')
    
    def drawLeftFace(self, canvas):
        xStart = self.width / 2 - 3 * self.cellLength
        yStart = 50 + self.cellLength / 2
        for row in range(self.faceRows):
            yStart += self.cellLength 
            self.drawLeftFaceHelper(canvas, xStart, yStart, row)

    def drawLeftFaceHelper(self, canvas, xS, yS, row):
        self.faceLeftList = [[self.app.frontFace, self.app.rightFace, 
                              self.app.backFace, self.app.leftFace],
                             [self.app.leftFace, self.app.backFace, 
                              self.app.rightFace, self.app.frontFace]]
        for col in range(self.faceCols):
            x1 = xS + col * self.cellLength
            y1 = yS + col * self.cellLength / 2
            x2 = x1 + self.cellLength
            y2 = y1 + self.cellLength / 2
            x3 = x2
            y3 = y1 + (3 / 2) * self.cellLength
            x4 = x1
            y4 = y1 + self.cellLength
            if self.oIndexRow == 0:
                color = self.faceLeftList[self.oIndexRow][self.oIndex][row][col]
            elif self.oIndexRow == 1:
                color = self.faceLeftList[self.oIndexRow][self.oIndex][2 - row][2 - col]
            canvas.create_polygon(x1, y1, x2, y2, x3, y3, x4, y4, 
            fill = color, outline = 'black', width = '1')
    
    def redrawAll(self, canvas):
        canvas.create_text(5, self.height // 20 - 10, font = 'Arial 15 bold', 
                        text = "Navigation: ", anchor = 'w')
        canvas.create_text(5, self.height // 20 + 10, 
                        text = '1: Loading Screen', anchor = 'w')
        canvas.create_text(5, self.height // 20 + 20,
                        text = '2: 2D Solve Screen', anchor = 'w')
        canvas.create_text(5, self.height // 20 + 30,
                        text = '3: 3D Solve Screen', anchor = 'w')
        canvas.create_text(5, self.height // 20 + 40, 
                        text = '4: Input Screen', anchor = 'w')
        canvas.create_text(5, self.height // 20 + 50,
                        text = 'h: Help Screen', anchor = 'w')  
        canvas.create_text(self.width // 2, 25, 
            anchor = 'center', font = 'Arial 15', 
            text = 'Use arrow keys to view different sides of the cube')      
        self.drawTopFace(canvas)
        self.drawRightFace(canvas)
        self.drawLeftFace(canvas)
        canvas.create_text(5, self.height // 3 * 2, text = 'Moves to make:',
            font = 'Arial 15 bold', anchor = 'w')
        canvas.create_text(5, self.height // 3 * 2 + 20, text = f'{self.moves}',
            font = 'Arial 15', anchor = 'w')
        canvas.create_text(self.width // 4 * 3 - 75, 100, font = 'Arial 15 bold', 
            text = f'Current State: {self.solvePart}', anchor = 'w')
        canvas.create_text(self.width // 2, 7, text = 'Make sure to always hold'
        + ' the cube with the green center facing you and the white center on top')
        self.drawButtons(canvas)

    def drawButtons(self, canvas):
        canvas.create_rectangle(100, 500, 150, 550, fill = 'pink')
        canvas.create_rectangle(700, 500, 750, 550, fill = 'pink')
        canvas.create_text(125, 525, text='Left', anchor = 'center')
        canvas.create_text(725, 525, text='Right', anchor = 'center')
        canvas.create_rectangle(250, 550, 600, 640, fill = 'pink')
        canvas.create_text(425, 595, text = 'Solve', anchor = 'center')
        canvas.create_text(425, 605, text = '(Space)', anchor = 'center')
        canvas.create_rectangle(700, self.height/2 - 25, 750, 
                                self.height/2 + 25, fill = 'pink')
        canvas.create_text(725, self.height/2, text = 'Scramble', anchor = 'center')
        canvas.create_rectangle(5, 600, 50, 645, fill = 'pink')
        canvas.create_text(27.5, 622.5, text = 'Reset!')

    def mousePressed(self, event):
        if event.x >= 100 and event.x <= 150 and event.y >= 500 and event.y <= 550:
            self.rotateOrientationLeft()
        elif event.x >= 700 and event.x <= 750 and event.y >= 500 and event.y <= 550:
            self.rotateOrientationRight()
        elif event.x >= 250 and event.x <= 600 and event.y >= 550 and event.y <= 640:
            solveCube(self)
        elif event.x >= 700 and event.x <= 750 and event.y >= self.height/2 - 25 and event.y <= self.height/2 + 25:
            self.setBooleans()
            self.scramble()
            self.solve = ''
        elif event.x >= 5 and event.x <= 50 and event.y >= 600 and event.y <= 645:
            self.setBooleans()

class SplashScreenMode(Mode):
    def __init__(mode):
        super().__init__()
    
    def appStarted(mode):
        # Rubik's Cube Image from: 
        # http://icon-park.com/icon/rubiks-cube-mix3-vector-icon/
        mode.image = mode.loadImage('rubiks_cube.png')
        mode.imageBig = mode.scaleImage(mode.image, 1/2)
        mode.imageS = mode.scaleImage(mode.image, 1/15)
        mode.createCubes()

    def createCubes(mode):
        mode.cubeList = []
        for _ in range(20):
            mode.cx = random.randint(0, mode.width)
            mode.cy = random.randint(0, mode.height)
            mode.speed = random.randint(5, 15)
            mode.cubeList.append([mode.cx, mode.cy, mode.speed])

    def redrawAll(mode, canvas):
        for cx, cy, speed in mode.cubeList:
            canvas.create_image(cx, cy, image = ImageTk.PhotoImage(mode.imageS))
        canvas.create_image(mode.width // 2, mode.height // 2 - 75, anchor = 'center',
            image = ImageTk.PhotoImage(mode.imageBig))
        canvas.create_text(mode.width // 2, 50, 
                text = "Rubik's Cube Solver!", font = 'Arial 30 bold')
        canvas.create_text(mode.width // 2, mode.height // 1.5, 
                text = 'Press any key to start!', font = 'Arial 20 bold')
        canvas.create_text(mode.width // 2, mode.height // 1.5 + 30, 
                text = "Press 'h' for help!", font = 'Arial 20 bold')

    def keyPressed(mode, event):
        if event.key == 'h':
            mode.app.setActiveMode(mode.app.helpMode)
        else:
            mode.app.setActiveMode(mode.app.gameMode3D)

    def mousePressed(mode, event):
        mode.app.setActiveMode(mode.app.gameMode3D)
  

    def timerFired(mode):
        tempList = []
        for i in range(len(mode.cubeList)):
            mode.cubeList[i] = (mode.cubeList[i][0], mode.cubeList[i][1] + mode.cubeList[i][2], mode.cubeList[i][2])
            if mode.cubeList[i][1] + mode.cubeList[i][2] >= mode.height:
                continue
            else:
                tempList.append([mode.cubeList[i][0], mode.cubeList[i][1], mode.cubeList[i][2]])
        mode.cubeList = tempList
        while len(mode.cubeList) < 30:
            mode.cx = random.randint(0, mode.width)
            mode.cy = 0
            mode.speed = random.randint(5, 15)
            mode.cubeList.append([mode.cx, mode.cy, mode.speed])


class ManualInputMode(Mode):
    def keyPressed(self, event):
        if event.key == '1':
            self.app.setActiveMode(self.app.splashScreenMode)
        elif event.key == '2':
            self.app.setActiveMode(self.app.gameMode)
        elif event.key == '3':
            self.app.setActiveMode(self.app.gameMode3D)
        elif event.key == '4':
            self.app.setActiveMode(self.app.manualInputMode)
        elif event.key == 'h':
            self.app.setActiveMode(self.app.helpMode)          
        elif event.key == 'w':
            self.submitInput()

    def appStarted(self):
        self.inputColor = 'grey'
        self.face = [['grey'] * 3 for rows in range(3)]
        self.createGreyFace()
        self.isFaceCompleted = [False, False, False, False, False, False]
        self.faceColor = ['white', 'green', 'red', 'yellow', 'blue', 'orange']
        self.faceList = [self.whiteFace, self.greenFace, self.redFace,
                         self.yellowFace, self.blueFace, self.orangeFace]
        self.fillColor = ['grey', 'grey', 'grey', 'grey', 'grey', 'grey']

    def createGreyFace(self):
        self.whiteFace = [['grey'] * 3 for rows in range(3)]
        self.greenFace = [['grey'] * 3 for rows in range(3)]
        self.yellowFace = [['grey'] * 3 for rows in range(3)]
        self.redFace = [['grey'] * 3 for rows in range(3)]
        self.blueFace = [['grey'] * 3 for rows in range(3)]
        self.orangeFace = [['grey'] * 3 for rows in range(3)]

    def checkFace(self):
        for i in range(len(self.faceList)):
            count = 0
            for row in range(3):
                for col in range(3):
                    if self.faceList[i][row][col] == 'grey':
                        count += 1
            if count == 0:
                self.isFaceCompleted[i] = True
            # Checks to see if a face is undone
            else:
                self.fillColor[i] = 'grey'
                self.isFaceCompleted[i] = False
        return False

    # Colors in the checklist if a face is inputted
    def changeFillColor(self):
        for i in range(len(self.faceList)):
            if self.isFaceCompleted[i] == True:
                self.fillColor[i] = self.faceColor[i]
            
    # Ensures that the inputted cube is legal.
    def checkIfLegal(self):
        # w, g, r, y, b, o
        counts = dict()
        for i in range(len(self.faceList)):
            for j in range(len(self.faceColor)):
                for row in range(3):
                    for col in range(3):
                        if self.faceList[i][row][col] == self.faceColor[j]:
                            counts[self.faceColor[j]] = 1 + counts.get(self.faceColor[j], 0)
        colorsCorrect = 0
        for key in counts:
            if counts[key] != 9:
                return False
            else:
                colorsCorrect += 1
        if colorsCorrect == 6:
            return True

    def mousePressed(self, event):
        if event.x >= 5 and event.x <= 55:
            for i in range(len(self.faceList)):
                leftBound = 55 * (i + 1) + 25
                rightBound = leftBound + 50
                if event.y >= leftBound and event.y <= rightBound:
                    self.inputColor = self.faceColor[i]

        # Colors for input face
        if event.x >= 100 and event.x <= 150 and event.y >= 100 and event.y <= 150:
            self.face[0][0] = self.inputColor
        if event.x >= 150 and event.x <= 200 and event.y >= 100 and event.y <= 150:
            self.face[0][1] = self.inputColor
        if event.x >= 200 and event.x <= 250 and event.y >= 100 and event.y <= 150:
            self.face[0][2] = self.inputColor
        if event.x >= 100 and event.x <= 150 and event.y >= 150 and event.y <= 200:
            self.face[1][0] = self.inputColor
        if event.x >= 150 and event.x <= 200 and event.y >= 150 and event.y <= 200:
            self.face[1][1] = self.inputColor
        if event.x >= 200 and event.x <= 250 and event.y >= 150 and event.y <= 200:
            self.face[1][2] = self.inputColor
        if event.x >= 100 and event.x <= 150 and event.y >= 200 and event.y <= 250:
            self.face[2][0] = self.inputColor
        if event.x >= 150 and event.x <= 200 and event.y >= 200 and event.y <= 250:
            self.face[2][1] = self.inputColor
        if event.x >= 200 and event.x <= 250 and event.y >= 200 and event.y <= 250:
            self.face[2][2] = self.inputColor

        if event.x >= 100 and event.x <= 250 and event.y >= 275 and event.y <= 350:
            self.submitFace()

    def submitFace(self):
        color = self.face[1][1]
        for i in range(len(self.faceColor)):
            if color == self.faceColor[i]:
                break
        for row in range(3):
            for col in range(3):
                self.faceList[i][row][col] = self.face[row][col]
        self.face = [['grey'] * 3 for rows in range(3)]        
        
    def redrawAll(self, canvas):
        canvas.create_rectangle(0, 0, self.width, self.height, fill='black')
        self.createKeyMap(canvas)
        # input color rectangle
        canvas.create_rectangle(5, 5, 55, 55, fill = self.inputColor)
        canvas.create_text(30, 20, text = 'Input', anchor = 'center')
        canvas.create_text(30, 40, text = 'Color', anchor = 'center')
        # change color rectangles
        for i in range(len(self.faceList)):
            leftBound = 55 * (i + 1) + 25
            rightBound = leftBound + 50
            canvas.create_rectangle(5, leftBound, 55, rightBound, 
            fill = self.faceColor[i])
        self.drawFace(canvas)
        # submit button
        canvas.create_rectangle(100, 275, 250, 350, fill = 'pink')
        canvas.create_text(175, 312, anchor = 'center', text='SUBMIT FACE')
        # checklist
        canvas.create_text(400, 100, text = 'white', fill = self.fillColor[0])
        canvas.create_text(400, 120, text = 'green', fill = self.fillColor[1])
        canvas.create_text(400, 140, text = 'red', fill = self.fillColor[2])
        canvas.create_text(400, 160, text = 'yellow', fill = self.fillColor[3])
        canvas.create_text(400, 180, text = 'blue', fill = self.fillColor[4])
        canvas.create_text(400, 200, text = 'orange', fill = self.fillColor[5])
        self.createDirections(canvas)

    def createKeyMap(self, canvas):
        canvas.create_text(5, self.height - self.height // 10 - 10, 
                font = 'Arial 10 bold', text = "Navigation: ", 
                fill = 'white', anchor = 'w',)
        canvas.create_text(5, self.height - self.height // 10 + 10, 
                    text = '1: Loading Screen', anchor = 'w', fill = 'white')
        canvas.create_text(5, self.height - self.height // 10 + 20,
                    text = '2: 2D Solve Screen', anchor = 'w', fill = 'white')
        canvas.create_text(5, self.height - self.height // 10 + 30,
                    text = '3: 3D Solve Screen', anchor = 'w', fill = 'white')
        canvas.create_text(5, self.height - self.height // 10 + 40, 
                    text = '4: Input Screen', anchor = 'w', fill = 'white')
        canvas.create_text(5, self.height - self.height // 10 + 50,
                    text = 'h: Help Screen', anchor = 'w', fill = 'white')
    
    def createDirections(self, canvas):
        canvas.create_text(175, 500, fill = 'white', anchor = 'center', 
                text = 'Remember to keep the white center on top at all times ' + 
                'unless entering the yellow face where you should instead have ' + 
                'the green center on top!', width = 200)
        canvas.create_text(400, 80, anchor = 'center', fill = 'white',
                    text = "Successfully Entered:")
        canvas.create_text(175, 75, fill = 'white', anchor = 'center',
                text = 'Click in the colored squares and')
        canvas.create_text(175, 85, fill = 'white', anchor = 'center',
                text = 'then on the face to input your cube')
        canvas.create_text(400, 400, fill = 'white', 
                text = "Press 'w' to load your input to the cube")
        if self.checkIfLegal():
            canvas.create_text(400, 390, fill = 'white',
                text = 'Input is ready for submission!')

    def timerFired(self):
        self.checkFace()
        self.changeFillColor()

    def drawFace(self, canvas):
        xStart = 100
        yStart = 100
        for row in range(3):
            for col in range(3):
                x1 = xStart + col * 50
                x2 = x1 + 50
                y1 = yStart + row * 50
                y2 = y1 + 50
                color = self.face[row][col]
                canvas.create_rectangle(x1, y1, x2, y2, fill = color)

    def loadInput(self):
        for row in range(3):
            for col in range(3):
                self.app.upperFace[row][col] = self.whiteFace[row][col] 
                self.app.frontFace[row][col] = self.greenFace[row][col] 
                self.app.rightFace[row][col] = self.redFace[row][col]
                self.app.bottomFace[row][col] = self.yellowFace[row][col] 
                self.app.backFace[row][col] = self.blueFace[row][col] 
                self.app.leftFace[row][col] = self.orangeFace[row][col]
    
    def submitInput(self):
        if self.checkIfLegal():
            self.loadInput()
    

class HelpMode(Mode):
    def redrawAll(mode, canvas):  
        mode.drawKeyMap(canvas)  
        canvas.create_text(mode.width // 2, mode.height // 20, text='Help Screen',
            font = 'Arial 35 bold')
        canvas.create_text(mode.width // 2, mode.height // 2, font = 'Arial 15',
            text = '    Please input your cube on the manual input screen or feel ' + 
            'free to mess around with random scrambles. When inputting your cube ' +
            'make sure to always hold the green center facing you and the white ' +
            'center on top. From this starting position rotate in each direction ' +
            'to enter the other faces while keeping the white center on top. To ' +
            'enter the yellow face, hold the green center on top.', 
            anchor = 'center', width = '700')
        canvas.create_text(mode.width // 2, mode.height // 4 * 3, font = 'Arial 15', 
            text = "Press 's' to get a sample scramble.", anchor = 'center')
        canvas.create_text(mode.width //2, mode.height //4 * 3 + 20, font = 'Arial 15',
            text = "Press 'space' to walk through the solve for the cube!")               
        canvas.create_text(mode.width //2, mode.height // 4 * 3 + 40, font = 'Arial 15',
         text = "if cube is not solving, press the reset button or click 'a'")
        mode.drawTurnMap(canvas)

    def drawTurnMap(mode, canvas):
        canvas.create_text(mode.width // 2, 100, text = 'Turn Map',
            anchor = 'center', font = 'Arial 20 bold')
        canvas.create_text(mode.width // 2, 122, anchor = 'center',
            text = 'F: Rotate Front Face Clockwise')
        canvas.create_text(mode.width // 2, 134, anchor = 'center',
            text = 'U: Rotate Upper Face Clockwise')
        canvas.create_text(mode.width // 2, 146, anchor = 'center',
            text = 'R: Rotate Right Face Clockwise')
        canvas.create_text(mode.width // 2, 158, anchor = 'center',
            text = 'L: Rotate Left Face Clockwise')
        canvas.create_text(mode.width // 2, 170, anchor = 'center',
            text = 'D: Rotate Bottom Face Clockwise')
        canvas.create_text(mode.width // 2, 182, anchor = 'center',
            text = 'B: Rotate Back Face Clockwise')
        canvas.create_text(mode.width // 2, 194, anchor = 'center',
            text = 'M: Rotate Middle Face Clockwise')
        canvas.create_text(mode.width // 2, 206, anchor = 'center',
            text = "'(apostrophe) : rotate counter clockwise")
        canvas.create_text(mode.width // 2, 218, anchor = 'center',
            text = "2: rotate face twice")
    def drawKeyMap(mode, canvas):
        canvas.create_text(5, mode.height // 20 - 10, font = 'Arial 15 bold', 
                        text = "Navigation: ", anchor = 'w')
        canvas.create_text(5, mode.height // 20 + 10, 
                        text = '1: Loading Screen', anchor = 'w')
        canvas.create_text(5, mode.height // 20 + 20,
                        text = '2: 2D Solve Screen', anchor = 'w')
        canvas.create_text(5, mode.height // 20 + 30,
                        text = '3: 3D Solve Screen', anchor = 'w')
        canvas.create_text(5, mode.height // 20 + 40, 
                        text = '4: Input Screen', anchor = 'w')
        canvas.create_text(5, mode.height // 20 + 50,
                        text = 'h: Help Screen', anchor = 'w')    

    def keyPressed(mode, event):
        if event.key == '1':
            mode.app.setActiveMode(mode.app.splashScreenMode)
        elif event.key == '2':
            mode.app.setActiveMode(mode.app.gameMode)
        elif event.key == '3':
            mode.app.setActiveMode(mode.app.gameMode3D)
        elif event.key == '4':
            mode.app.setActiveMode(mode.app.manualInputMode)
        elif event.key == 'h':
            mode.app.setActiveMode(mode.app.helpMode)

class MyModalApp(ModalApp):
    def appStarted(app):
        app.splashScreenMode = SplashScreenMode()
        app.gameMode = RubiksCubeMode()
        app.gameMode3D = RubiksCube3DMode()
        app.manualInputMode = ManualInputMode()
        app.helpMode = HelpMode()
        app.setActiveMode(app.splashScreenMode)
        app.createFace()

    def createFace(app):
        # Creating Standard Faces
        app.frontFace = [['green'] * 3 for _ in range(3)]
        app.upperFace = [['white'] * 3 for _ in range(3)]
        app.bottomFace = [['yellow'] * 3 for _ in range(3)]
        app.rightFace = [['red'] * 3 for _ in range(3)]
        app.backFace = [['blue'] * 3 for _ in range(3)]
        app.leftFace = [['orange'] * 3 for _ in range(3)]
        
runRubiksCube()
