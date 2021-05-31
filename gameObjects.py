import pygame

SCREEN_WIDTH = 480
SCREN_HEIGTH = 800

TYPE_SMALL = 1
TYPE_MIDDLE = 2
TYPE_BIG = 3


class Player (pygame.sprite.Sprite): # Inheritance - Pygame class sprite - pygame.sprite.Sprite
  def __init__(self, plane_img, player_rect, init_pos): # player_rect --> rect (x, y, w, h) --> x pos(left), y pos(top) , width, height
    pygame.sprite.Sprite.__init__(self)
    self.image = [] # Spreadsheet of images - images as a list

    # Everytime we give the coordinates of the player, we fetch the image and add it to the collection self.image[]
    for i in range(len(player_rect)):
      # plane_image is a spreadsheet of images
      # Subsurface method will cut part of the spreadsheet
      # convert_alpha will apply transparency to the image 
      self.image.append(plane_img.subsurface(player_rect[i].convert_alpha()))

    self.rect = player_rect[0]
    self.rect.topleft = init_pos
    self.speed = 8
    self.bullets = pygame.sprite.Group() # It takes multiple objects
    self.img_index = 0
    self.is_hit = False # Boolean

  def moveLeft(self):
    # Check left boundary for the main Player
    if self.rect.left <= 0:
      self.rect.left = 0
    else :
      self.rect.left += self.speed

  def moveRight(self):
    # Check Right boundary for the main Player
    if self.rect.left >= SCREEN_WIDTH - self.rect.width:
      self.rect.left = SCREEN_WIDTH - self.rect.width
    else :
      self.rect.left += self.speed
