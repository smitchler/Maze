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
    turnLeft(self.t)
   
    
  def colorInFront(self):
    """ returns the color in front of the turtle """
    x = getXPos(self.t)
    y = getYPos(self.t)
    dir = getHeading(self.t)
    if dir == 0.0:
      y = y-11
    if dir == 90.0 or -270.0:
      x = x+11
    if dir == 180.0 or -180.0:
      y = y+11
    if dir == 270.0 or -90.0:
      x = x-11
    c = getColor(getPixelAt(self.image, x, y))
    if distance(c, white) < 160:
      return white
    if distance(c, blue) < 160:
      return blue
    if distance(c, yellow) < 160:
      return yellow
    if distance(c, red) < 160:
      return red
    if distance(c, green) < 160:
      return green 
   
#Tests follow this line
doTests = true
if doTests:
  #Test 1: verify we have a maze
  m=Maze()
  
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
  if m.colorInFront() == blue:
    printNow("Test 9 passed, colorInFront returns blue.")
  else:
    printNow("Test 9 failed, colorInFront does not return blue.")