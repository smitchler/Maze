# Maze program by Sarah Mitchler
setMediaPath('C:\\Users\\Sarah\\Documents\\GitHub')
class Maze(object):
  """ solves a maze """
  def __init__(self):
    """ initialization """
    self.image = makePicture('Maze Image(1).jpg')
    w = getWidth(self.image)
    h = getHeight(self.image)
    self.w = makeWorld(w,h)
    self.w.setPicture(self.image)
    self.t = makeTurtle(self.w)
    penUp(self.t)
    moveTo(self.t, 30, 190)
    self.t.setHeading(90)
    
   
    
  def colorInFront(self):
    """ returns the color in front of the turtle """
    x = getXPos(self.t)
    y = getYPos(self.t)
    dir = getHeading(self.t)
    if dir == 0:
      y = y-11
    if dir == 90 or dir == -270:
      x = x+11
    if dir == 180 or dir == -180:
      y = y+11
    if dir == 270 or dir == -90:
      x = x-11
    c = getColor(getPixelAt(self.image, x, y))
    if distance(c, white) < 160:
      return white
    if distance(c, blue) < 160:
      return blue
    if distance(c, green) < 160:
      return green
    if distance(c, red) < 160:
      return red
    if distance(c, yellow) < 160:
      return yellow
    return blue #assume wall if uncertain
      
  def travel2BranchOrWall(self):
    """moves turtle forward until it hits branch or finds an alternative path"""
    if self.surroundings().count(white) > 1:
      while self.surroundings().count(white) > 1:
        self.forward(1)
    if self.colorInFront() == white:
      while self.colorInFront() == white and self.surroundings().count(white) == 1:
        self.forward(1) 
    if self.surroundings().count(white) > 1:
      self.forward(8)
    
    
  def reset(self):
    """resets maze to original conditions"""
    self.image = makePicture('Maze Image(1).jpg')
    self.w.setPicture(self.image)
    self.t.clearPath()
    penUp(self.t)
    moveTo(self.t, 30, 190)
    turnToFace(self.t, 35, 190)
    penDown(self.t)
    
    
    
  def surroundings(self):
    a = []
    for i in range (4):
      a.append(self.colorInFront())
      turn(self.t)
    return a
    
    
  def forward(self, dist):
    while dist > 0:
      addOvalFilled(self.image, self.t.getXPos()-10, self.t.getYPos()-10, 20, 20, green)
      dist = dist - 1
      forward(self.t, 1)
      
  
  def solve(self):
    pass
 
#Tests follow this line
doTests = true
if doTests:
  #Test 1: verify we have a maze
  m=Maze()
  printNow("Test 1 passed, Maze exists.")
  
  #Test 2:
  if m.image.__class__ == Picture:
    printNow("Test 2 passed, Image exists.")
  else:
    printNow("Test 2 failed, Image doesn't exist.")
      
  #Test 3: verify that we have a world
  try:
    if m.w.__class__ == World:
      printNow("Test 3 passed, World exists.")
  except:
    printNow("Test 3 failed, World doesn't exist.")
    
  #Test 4: check for world image
  try:
    if m.w.getPicture().fileName[-17:] == 'Maze Image(1).jpg':
     printNow("Test 4 passed, world picture is Maze Image(1).jpg")
    else:
     printNow("Test 4 failed, world picture is " + m.w.getPicture().fileName)
  except:
    printNow("Test 4 failed, unable to get file name")
    
  #Test 5: check for Turtle
  try:
    if m.t.__class__ == Turtle:
      printNow("Test 5 passed, Turtle exists.")
    else:
      printNow("Test 5 failed, it is not a turtle.")
  except:
    printNow("Test 5 failed, Turtle doesn't exist.")
    
  #Test 6: check Turtle's location
  try:
    if m.t.getXPos() == 30 and m.t.getYPos() == 190:
      printNow("Test 6 passed, Turtle is in correct starting position.")
    else:
      printNow("Test 6 failed, Turtle is not in correct position.")
  except:
    printNow("Turtle does not exist.")
    
  #Test 7: check colorInFront
  if dir(m).index('colorInFront') > 0:
    printNow("Test 7 passed, colorInFront exists.")
  else:
    printNow("Test 7 failed, colorInFront does not exist.")
    
  #Test 8: check if colorInFront is white
  if m.colorInFront() == white:
    printNow("Test 8 passed, colorInFront returns white.")
  else:
    printNow("Test 8 failed, colorInFront does not return white.")
    
  #Test 9: check if colorInFront is blue
  turnRight(m.t)
  if m.colorInFront() == blue:
    printNow("Test 9 passed, colorInFront returns blue when facing a wall.")
  else:
    printNow("Test 9 failed, colorInFront returned " + str(m.colorInFront()))
    
    
  #Test 10: check travel2BranchOrWall
  if dir(m).index('travel2BranchOrWall') > 0:
    printNow("Test 10 passed, travel2BranchOrWall exists.")
  else:
    printNow("Test 10 failed, travel2BranchOrWall does not exist.")
    
  #Test 11: check reset
  if dir(m).index('reset') > 0:
    printNow("Test 11 passed, reset exists.")
  else:
    printNow("Test 11 failed, reset does not exist.")
    
  #Test 12: check if maze is in initial condition
  m.reset()
  assert getXPos(m.t) == 30, "Test 12 failed, x position is " + str(getXPos(m.t))
  assert getYPos(m.t) == 190, "Test 12 failed, y position is " + str(getYPos(m.t))
  assert getHeading(m.t) == 90, "Test 12 failed, heading is " + str(getHeading(m.t))
  printNow("Test 12 passed, x, y, and heading are correct after reset.")
  
  #Test 13: check that we travel to a wall after travel2BranchOrWall
  m.reset()
  m.travel2BranchOrWall()
  if m.t.getXPos() != 109:
    printNow("Test 13 failed, x position is " + str(m.t.getXPos()))
  elif m.t.getYPos() != 190:
    printNow("Test 13 failed, y position is " + str(m.t.getYPos()))
  else:
    printNow("Test 13 passed, we can travel to wall.")
    
  #Test 14: check travel2BranchOrWall going north
  m.reset()
  turnLeft(m.t)
  m.travel2BranchOrWall()
  if m.t.getXPos() != 30:
    printNow("Test 14 failed, x position is " + str(m.t.getXPos()))
  elif m.t.getYPos() != 110:
    printNow("Test 14 failed, y position is " + str(m.t.getYPos()))
  else: 
    printNow("Test 14 passed, we can travel to branch.")
    
  #Test 15: check for green trail
  m.reset()
  m.forward(30)
  turn(m.t)
  turn(m.t)
  assert m.colorInFront() == green
  printNow("Test 15 passed, leaving green trail.")
    
  #Test 16: check for surroundings
  m.reset()
  m.t.setHeading(0)
  m.forward(80)
  assert m.surroundings() == [white, white, green, blue], str(m.surroundings())
  printNow("Test 16 passed, surroundings at first northern branch are white, white, green, blue.")
  
  #Test 17: solve() returns true when starting at cheese
  m.reset()
  penUp(m.t)
  moveTo(m.t, 390, 155)
  if m.solve():
    printNow("Test 17 passed")
  else:
    printNow("Test 17 failed.")
  
  
  