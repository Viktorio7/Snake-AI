# import pyglet
# import random
#
# #===========================================================SnakeBody=========
# class SnakeBody(pyglet.shapes.Rectangle):
#     def __init__(self,x,y):
#         self.X=x
#         self.Y=y
#         super().__init__(x=self.gridToPositionX(self.X),
#                          y=self.gridToPositionY(self.Y),
#                          height=12,width=12)
#         self.color=(255, 255, 255)
#         #self.height=12
#         #self.width=12
#
#     def gridToPositionX(self,gridX):
#         return 901+gridX*15
#
#     def gridToPositionY(self,gridY):
#         return 16+gridY*15
#
#     def setPosX(self, x):
#         self.X=x
#
#     def setPosY(self, y):
#         self.Y=y
#
#     def positionPart(self):
#         self.x=self.gridToPositionX(self.X)
#         self.y=self.gridToPositionY(self.Y)
#
# #===========================================================SnakeHead=========
# class SnakeHead(SnakeBody):
#     def __init__(self,*args,**kwargs):
#         super().__init__(*args,**kwargs)
#         self.color=(255, 0, 0)
#         self.direction=1
#
#     def move(self):
#         if   self.direction == 1: #up
#             self.Y+=1
#         elif self.direction == 2: #right
#             self.X+=1
#         elif self.direction == 3: #down
#             self.Y-=1
#         elif self.direction == 4: #left
#             self.X-=1
#         if self.X>34:
#             self.X=0
#         if self.X<0:
#             self.X=34
#         if self.Y>57:
#             self.Y=0
#         if self.Y<0:
#             self.Y=57
#
#
#
# #===========================================================Apple=============
# class Apple:
#     pass