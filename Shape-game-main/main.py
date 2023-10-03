#Maria Girgis and Connor Aalto
#PA 6 Screen 2

from graphics import*
import time
from intro_screen import *
shape = main()
win=GraphWin("Gameplay",600,600)
win.setBackground("yellow")


playWindow=Rectangle(Point(170,170),Point(570,570))


instructions = Text(Point(300, 100), "Instructions for game here (instructions) Click to continue to game screen")
instructions.draw(win)
introClick = win.getMouse()
instructions.undraw()


playWindow.setFill("light gray")
playWindow.draw(win)


drawingName = Text(Point(350, 75), shape.name)
drawingName.setSize(36)
drawingName.draw(win)

for i in range(9):
    
    cordX = Text(Point(150, 170+i*50), i*50)
    dashY = Line(Point(165, 170+i*50), Point(185, 170+i*50))
    dashX = Line(Point(170+i*50, 555), Point(170+i*50, 575))
    cordY = Text(Point(170+i*50, 590), i*50)

    
    dashX.setWidth(2)
    
    
    dashY.setWidth(2)

    
    cordX.draw(win)
    cordY.draw(win)
    dashX.draw(win)
    dashY.draw(win)

labelY = Text(Point(170, 150), 'Y')
labelY.setSize(20)
labelY.draw(win)


labelX = Text(Point(585, 570), 'X')
labelX.setSize(20)
labelX.draw(win)





cordPos = Text(Point(450, 150), "Move to the game zone")
cordPos.setSize(20)
cordPos.draw(win)



accuracy=Text(Point(75,300),"Accuracy")
accuracyGrd = Text(Point(75, 350), "100%")
accuracyGrd.draw(win)
accuracy.setFace("times roman")
accuracy.setSize(25)
accuracy.setTextColor("black")
accuracy.setStyle("bold")
accuracy.draw(win)
instructions=Text(Point(75,450),"Instructions")
instructionsInfo = Text(Point(75, 476), ("Points for line 1"))
instructionsInfo.draw(win)
instructions.setFace("times roman")
instructions.setSize(25)
instructions.setTextColor("black")
instructions.setStyle("bold")
instructions.draw(win)


timer = Text(Point(80, 100), "5")
timer.setSize(25)

timer.draw(win)

timerLabel = Text(Point(90, 75), "Seconds until cordinates disappear")
timerLabel.setSize(10)
timerLabel.draw(win)


def motion(event):
    
    x, y = event.x, event.y
    if x >=170 and y >=170 and x <=570 and y<=570:
            
        position = ('{}, {}'.format(x-170, y-170))
        cordPos.setText(position)
        
    
    
        

pointList=shape.actualPoints

numlist=len(pointList)

pointLabel=Text(Point(80,525),"")
pointLabel.setSize(15)
pointLabel.draw(win)
win.bind('<Motion>', motion)

def pointTimer():
        
    win.bind('<Motion>', motion)
    
    for i in range(1, 101):

        time.sleep(0.05)
        
        timer.setText((round(5-i/20, 1)))
        

    win.unbind('<Motion>')
    cordPos.setText("Select your points!")


#loop that draws the actual shape to be compared against the one the user created
def drawShape(mode, intro):

    if mode == 'draw':
        
        for i in range(3):

            for j in range(len(pointList)):
                point1X = 170
                point1Y = 170
                point2X = 170
                point2Y = 170
                
               
                point1X = point1X + pointList[j][0]
                point1Y = point1Y + pointList[j][1]

                point2X = point2X + pointList[j][2]
                point2Y = point2Y + pointList[j][3]

                aLine = Line(Point(point1X, point1Y), Point(point2X, point2Y))
                aLine.setFill('red')
                aLine.setWidth(3)
                aLine.draw(win)
                
                if intro == True:
                    
                    aLine.undraw()
            

#sleep to allow user to get ready for game

drawShape(mode = 'draw', intro = True)
introText = Text(Point(400, 400), "Game About to Start... Study the screen for 10 seconds.. \nThe game has started when this message disappears")
introText.draw(win)
time.sleep(10)
introText.undraw()
lineCount = 0
for i in range(numlist):
    pointInfo = ''
    lineCount = lineCount + 1
    
    text = "Points for line " + str(lineCount)
    instructionsInfo.setText(text)
    lenPoint = len(pointList[i])
    for num in range(lenPoint):
        if num == 0:
            pointInfo += 'First Point: (' + str(pointList[i][num]) + ', '
        if num == 1:
            pointInfo += str(pointList[i][num]) + ')'
        if num == 2:
            pointInfo += '\n\nSecond Point: (' + str(pointList[i][num]) + ', '
        if num == 3:
            pointInfo += str(pointList[i][num]) + ')'
            
        
    pointLabel.setText(pointInfo)  
        
    
    
    pointReminder = Text(Point(255, 150), "Plot the First Point")
    pointReminder.setSize(15)
    pointReminder.draw(win)
    pointTimer()
    
    click1 = win.getMouse()
    pointReminder.setText("Plot the Second Point")
    click1X=click1.getX()
    click1Y=click1.getY()
    point1 = Circle(Point(click1X, click1Y), 3)
    point1.setFill('black')
    point1.draw(win)

    
    
    pointTimer()
    



    click2 = win.getMouse()
    click2X=click2.getX()
    click2Y=click2.getY()

    userPtList = [int(click1X), int(click1Y), int(click2X), int(click2Y)]
    shape.userPoints.append(userPtList)
    pointReminder.undraw()
    point2 = Circle(Point(click2X, click2Y), 3)
    point2.setFill('black')
    point2.draw(win)

    
    accuracy = shape.grade()

    accuracyGrd.setText(accuracy)

    if accuracy == '0%':
        pass
        #add a restart button and prompt user to restart

   
    
    
    if click1X>=170 and click1X<=570 and click1Y>=170 and click1Y<=570:
        if click2X>=170 and click2X<=570 and click2Y>=170 and click2Y<=570:


            userLine = Line(Point(click1X, click1Y), Point(click2X, click2Y))
            userLine.setWidth(2)
            userLine.draw(win)


    
#shows the actual shape to be compared to what the user drew
            
drawShape(mode = 'draw', intro = False)

endMessage = "GAME OVER. You scored a " + shape.grade() + " on accuracy"

endMessageTxt = Text(Point(400, 200), endMessage)

endMessageTxt.draw(win)






    
    






    
    




