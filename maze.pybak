# Maze program by Sarah Mitchler
setMediaPath('C:\\Users\\PC7\\Documents\\GitHub\\Maze')
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