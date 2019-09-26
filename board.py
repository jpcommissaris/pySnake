import pygame
import random
import time
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
        self.NUMPELLETS = 6
        # set up board
        self.lSize = int(self.LENGTH/self.SIZE)
        self.wSize = int(self.WIDTH/self.SIZE)
        self.board = []  # stores a number that will map tp a color
        self.set()
        # color dictionary
        self.colorDic = {0: BLACK, -1: GREEN, 1: RED} #0 is the board, 1 is the head, -1 is a pellet
        #scores
        self.p1 = 0
        self.p2 = 0

    def set(self):
        self.setBoard(self.lSize, self.wSize)
        for p in range(self.NUMPELLETS):
            self.drawPellet()
        # add snakes
        self.s1 = self.Snake(9, 8, 1)
        self.s2 = self.Snake(9, self.lSize-8, 2)
        self.drawSnake(self.s1, self.s1.size)
        self.drawSnake(self.s2, self.s1.size)

    # --- getters and setters ---
    def getSize(self):
        return self.LENGTH, self.WIDTH

    def setDirection(self):
        keys=pygame.key.get_pressed()

        if keys[pygame.K_s]:
            if self.s1.notAllowed != "DOWN":
                self.s1.direction = "DOWN"
        if keys[pygame.K_w]:
            if self.s1.notAllowed != "UP":
                self.s1.direction = "UP"
        if keys[pygame.K_a]:
            if self.s1.notAllowed != "LEFT":
                self.s1.direction = "LEFT"
        if keys[pygame.K_d]:
            if self.s1.notAllowed != "RIGHT":
                self.s1.direction = "RIGHT"
        if keys[pygame.K_DOWN]:
            if self.s2.notAllowed != "DOWN":
                self.s2.direction = "DOWN"
        if keys[pygame.K_UP]:
            if self.s2.notAllowed != "UP":
                self.s2.direction = "UP"
        if keys[pygame.K_LEFT]:
            if self.s2.notAllowed != "LEFT":
                self.s2.direction = "LEFT"
        if keys[pygame.K_RIGHT]:
            if self.s2.notAllowed != "RIGHT":
                self.s2.direction = "RIGHT"

    def setBoard(self, l, w):
        self.board = []
        for r in range(w):
            self.board.append([])
            for c in range(l):
                self.board[r].append(0)

    def getColor(self, arg):
        return self.colorDic.get(arg, GREY) # default is a body part


    # --- drawing ---
    def drawBoard(self, win):
        self.moveSnake(self.s1)
        self.moveSnake(self.s2)
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                self.moveHelper(r, c)
                color = self.getColor(self.board[r][c])
                pygame.draw.rect(win, color, (c*self.SIZE, r*self.SIZE, self.SIZE, self.SIZE))
        # handles diretions
        self.s1.setAllowed()
        self.s2.setAllowed()
    def drawScores(self, win):
        font = pygame.font.SysFont("Helvetica", 16)
        score1 = font.render('Score = ' + str(self.p1), False, GREEN)
        win.blit(score1, (10, 10))
        score2 = font.render('Score = ' + str(self.p2), False, GREEN)
        win.blit(score2, (800, 10))

    def drawPellet(self):
        l = random.randint(0, self.lSize-1)
        w = random.randint(0, self.wSize-1)
        self.board[w][l] = -1

    def drawSnake(self, snake, size):
        # this makes the bodypart count diff numbers so the sizes can be calculated independently
        if snake.player == 1:
            offset = 1
        else:
            offset = 1.1
        for x in range(size):
            self.board[snake.headR-x][snake.headC] = x+offset

    # --- logic ---
    def gameOver(self, player):
        if player == 1:
            self.p2 += 1
        if player == 2:
            self.p1 += 1
        time.sleep(1)
        self.set()

    def moveSnake(self, snake):
        if snake.direction == "DOWN":
            self.move(snake, 1, 0)
        elif snake.direction == "UP":
            self.move(snake, -1, 0)
        elif snake.direction == "RIGHT":
            self.move(snake, 0, 1)
        elif snake.direction == "LEFT":
            self.move(snake, 0, -1)

    def move(self, snake, r, c):
        if snake.headR >= self.wSize-1 or snake.headR <= 0 or snake.headC >= self.lSize-1 or snake.headC <= 0: # borders
            print("gameover")
            self.gameOver(snake.player)
            return
        else:
            # checks collisions
            if self.board[snake.headR + r][snake.headC + c] == -1: # collides with pellet?
                self.drawPellet()
                if snake.player == 1:
                    self.s1.size += 5
                else:
                    self.s2.size += 5
            if self.board[snake.headR + r][snake.headC + c] > 1:
                self.gameOver(snake.player)
                print("game over") # call a reset
                return
            # moves
            self.board[snake.headR][snake.headC] = 2 # first body part
            snake.headR += r
            snake.headC += c
            self.board[snake.headR][snake.headC] = 1 # head
            self.board[snake.tailR][snake.tailC] = 0 # board
    # goes inside for loop
    def moveHelper(self,r,c):
        if self.board[r][c] == self.s1.size:
            self.board[r][c] = 0
        if self.board[r][c] == self.s2.size:
            self.board[r][c] = 0
        if self.board[r][c] > 1:
            self.board[r][c] += 1

    # Snake Object
    class Snake:

        def __init__(self, r, c, p):
            # pos of head
            self.size = 0
            self.headR = r
            self.headC = c
            self.tailR = r-5
            self.tailC = c
            self.direction = "DOWN"
            self.notAllowed = "UP"
            self.player = p
            self.setSize()
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

        def setSize(self):
            if self.player == 1:
                self.size = 7
            else:
                self.size = 7.1



















