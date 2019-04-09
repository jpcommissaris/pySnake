import pygame
import random
BLACK = (0,0,0) # if board[][] = 0
GREEN = (0,255,0)
RED = (255, 0, 0)
GREY = (160,160,160)
WHITE = (255,255,255)

class Board:

    def __init__(self):
        # constants
        self.LENGTH = 900 # width and height must divide nicely into size, quotient must be larger than 10
        self.WIDTH = 705
        self.SIZE = 15
        # set up board
        self.lSize = int(self.LENGTH/self.SIZE)
        self.wSize = int(self.WIDTH/self.SIZE)
        self.board = []  # 0 is empty, 1 is head, 2 is bodypart, 3 is tail
        self.set()
        # color dictionary
        self.colorDic = {"BOARD": BLACK, "PELLET": GREEN, "HEAD": RED, "TAIL": GREY, "BODY": GREY}

    def set(self):
        self.setBoard(self.lSize, self.wSize)
        self.drawPellet()
        self.drawPellet()
        self.drawPellet()
        # add snakes
        self.s1 = self.Snake(9, 8, 1)
        self.s2 = self.Snake(9, self.lSize-8, 2)
        self.drawSnake(self.s1)
        self.drawSnake(self.s2)

    # --- getters and setters ---
    def getSize(self):
        return self.LENGTH, self.WIDTH

    def setDirection(self):
        keys=pygame.key.get_pressed()

        if keys[pygame.K_DOWN]:
            if self.s1.notAllowed != "UP":
                self.s1.direction = "DOWN"
        if keys[pygame.K_UP]:
            if self.s1.notAllowed != "DOWN":
                self.s1.direction = "UP"
        if keys[pygame.K_LEFT]:
            if self.s1.notAllowed != "RIGHT":
                self.s1.direction = "LEFT"
        if keys[pygame.K_RIGHT]:
            if self.s1.notAllowed != "LEFT":
                self.s1.direction = "RIGHT"
        if keys[pygame.K_s]:
            if self.s2.notAllowed != "UP":
                self.s2.direction = "DOWN"
        if keys[pygame.K_w]:
            if self.s2.notAllowed != "DOWN":
                self.s2.direction = "UP"
        if keys[pygame.K_a]:
            if self.s2.notAllowed != "RIGHT":
                self.s2.direction = "LEFT"
        if keys[pygame.K_d]:
            if self.s2.notAllowed != "LEFT":
                self.s2.direction = "RIGHT"



    def setBoard(self, l, w):
        for r in range(w):
            self.board.append([])
            for c in range(l):
                self.board[r].append("BOARD")

    def getColor(self, arg):
        return self.colorDic.get(arg, WHITE) # white is default case, if it shows its an error

    # --- drawing ---
    def drawBoard(self, win):
        self.moveSnake(self.s1)
        #self.moveSnake(self.s2)
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                color = self.getColor(self.board[r][c])
                pygame.draw.rect(win, color, (c*self.SIZE, r*self.SIZE, self.SIZE, self.SIZE))
        # handles diretions
        self.s1.setAllowed()
        self.s2.setAllowed()
        print(self.s1.direction)

    def drawPellet(self):
        l = random.randint(0, self.lSize-1)
        w = random.randint(0, self.wSize-1)
        self.board[w][l] = "PELLET"

    def drawSnake(self, snake):
        self.board[snake.headR][snake.headC] = "HEAD"
        self.board[snake.headR-1][snake.headC] = "BODY"
        self.board[snake.headR-2][snake.headC] = "BODY"
        self.board[snake.headR-3][snake.headC] = "TAIL"
        snake.tailR = snake.headR-3

    # --- logic ---
    def moveSnake(self, snake):
        if snake.direction == "DOWN":
            self.move(snake, 1, 0)
        elif snake.direction == "UP":
            self.move(snake, -1, 0)
        elif snake.direction == "RIGHT":
            self.move(snake, 0, 1)
        elif snake.direction == "LEFT":
            self.move(snake, 0 ,-1)

    def move(self, snake, r, c):
        if snake.headR >= self.wSize-1:
            direction = "NULL" # this player loses
        else:
            # checks collisions
            if self.board[snake.headR + r][snake.headC + c] == "PELLET":
                pass

            # moves
            self.board[snake.headR][snake.headC] = "BODY"
            snake.headR += r
            snake.headC += c
            self.board[snake.headR][snake.headC] = "HEAD"
            self.board[snake.tailR][snake.tailC] = "BOARD"
            self.board[snake.tailR][snake.tailC] = "TAIL"

    def moveDown(self, snake):
        if snake.headR >= self.wSize-1:
            direction = "NULL" # this player loses
        else:
            # checks collisions
            if self.board[snake.headR + 1][snake.headC] == "PELLET":
                pass

            # moves
            self.board[snake.headR][snake.headC] = "BODY"
            snake.headR += 1
            self.board[snake.headR][snake.headC] = "HEAD"
            self.board[snake.tailR][snake.tailC] = "BOARD"
            snake.tailR += 1
            self.board[snake.tailR][snake.tailC] = "TAIL"

    def moveRight(self, snake):
        if snake.headR >= self.wSize - 1:
            direction = "NULL"  # this player loses
        else:
            # checks collisions
            if self.board[snake.headR][snake.headC + 1] == "PELLET":
                pass

            # moves
            self.board[snake.headR][snake.headC] = "BODY"
            snake.headC += 1
            self.board[snake.headR][snake.headC] = "HEAD"
            self.board[snake.tailR][snake.tailC] = "BOARD"
            snake.tailC += 1
            self.board[snake.tailR][snake.tailC] = "TAIL"

    # Snake Object

    class Snake:

        def __init__(self, r, c, p):
            # pos of head
            self.headR = r
            self.headC = c
            self.tailR = r-3
            self.tailC = c
            self.direction = "DOWN"
            self.notAllowed = "UP"
            self.player = p
        # ensures only legal moves are made
        def setAllowed(self):
            if self.direction == "DOWN":
                self.notAllowed = "UP"
            elif self.direction == "UP":
                self.notAllowed = "DOWN"
            elif self.direction == "LEFT":
                self.notAllowed = "RIGHT"
            elif self.direction == "RIGHT":
                self.notAllowed = "LEFT"



















