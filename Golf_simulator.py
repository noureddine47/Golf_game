import pygame
import random
from random import randint
width=1000
height=600
b_w=width/14
b_h=height/12
pygame.init()
win= pygame.display.set_mode((width,height))
pygame.display.set_caption("Nounou Golf")
# colors
black=(0,0,0)

# load and rescale the images and display the grass and the Gap
grass=pygame.image.load("green-grass-summer-gazon-fon-trava-zelenaia.jpg")
grass=pygame.transform.scale(grass,(width,height))

ball_image=pygame.image.load("golf_PNG32.png")
ball_image=pygame.transform.scale(ball_image,(int(b_w),int(b_h)))

c = randint(60, 300)
d = randint(70, 590)

# define the ball class
class Ball:
    r=1
    x=0
    y=0

    def __init__(self):
        self.a=c
        self.b=d
        self.l=0

    def display(self):
        t = self.a - self.x
        n = self.b - self.y
        win.blit(grass, (0, 0))
        pygame.draw.circle(win, black, (940, 80), 40, 0)
        win.blit(ball_image, ((self.a - (b_w / 2), self.b - (b_h / 2))))
        pygame.draw.line(win,(204,153,255),(self.a,self.b),(self.a+t,self.b+n),10)
        pygame.display.update
    def move(self):
        self.s = self.a - self.x
        self.q = self.b - self.y
        for i in range(20):
            if self.a >= 900 and self.a <= 980:
                if self.b >= 50 and self.b <= 100:
                    self.a = self.a
                    self.b = self.b
                    self.l=1
                    break
            if (self.a >= 0 and self.a <= 1020):
                if (self.b >= -5 and self.b <= 600):
                    self.a = self.r * self.s + self.a
                    self.b = self.r * self.q + self.b
                elif (self.b <= -5 or self.b >= 600):
                    self.q = -self.q
                    self.a = self.r * self.s + self.a
                    self.b = self.r * self.q + self.b
            elif (self.a <= 0 or self.a >= 1020):
                self.s = -self.s
                self.a = self.r * self.s + self.a
                self.b = self.r * self.q + self.b
            win.blit(ball_image, (self.a - (b_w / 2), self.b - (b_h / 2)))
            print("a= " + str(self.a) + ", b= " + str(self.b) + " x= " + str(self.x) + ", y= " + str(self.y))

            pygame.display.flip()
        if self.a>1000 or self.a<0 or self.b>600 or self.b<0:
            self.a=c
            self.b=d

    def check(self):
        if self.l==1:
            return True

    def win(self):
     font=pygame.font.SysFont("Comic Sans Ms",60)
     text1=font.render("you win",1,(255,255,102))
     text2=font.render("Retry",1,(255,255,255))
     win.blit(grass, (0, 0))
     pygame.draw.circle(win, black, (940, 80), 40, 0)
     win.blit(text1,(400,300))
     r = pygame.Rect(400, 150, 200, 100)
     pygame.draw.rect(win, (0, 0, 0), r)
     win.blit(text2, (420, 150))
     pygame.display.update()

    def retry(self):
         if self.x>=400 and self.x<=600:
             if self.y>=150 and self.y<=250:
                 self.l=0
                 self.a=c
                 self.b=d


ball1 = Ball()
while True:
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        ball1.x = pos[0]
        ball1.y = pos[1]
        if ball1.check():
            ball1.win()

        else:

            ball1.display()
            pygame.display.update()

        print(str(ball1.a)+" , "+str(ball1.b))

        if event.type==pygame.MOUSEBUTTONDOWN:
            pos1 = pygame.mouse.get_pos()
            ball1.x = pos1[0]
            ball1.y = pos1[1]

            ball1.move()
            ball1.retry()
            ball1.check()
            print(str(ball1.check()))

        if event.type==pygame.QUIT:
            pygame.quit()

