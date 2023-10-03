#Maria Girgis, Connor Aalto
#PA 6 intro screen

from graphics import*
from buttonClass import*
from classes import *


def main():

    #define box object
    box = Drawing('Box', [[89,167,37,115],
  [37,115,130,65],
  [130,64,188,115],
  [188,115,90,166],
  [188,115,279,158],
  [279,157,322,103],
  [322,103,228,57],
  [228,57,188,115],
  [279,157,179,216],
  [179,216,90,167],
  [90,167,56,223],
  [56,222,154,279],
  [179,216,155,279],
  [179,216,217,270],
  [217,270,326,200],
  [326,200,279,159],
  [179,216,181,343],
  [181,343,299,276],
  [299,276,298,219],
  [181,343,80,289],
  [80,289,80,236]], [])

    #define arrow object
    arrow = Drawing('Arrow', [[26,215,86,184],
  [86,184,112,186],
  [118,193,112,213],
  [112,213,48,248],
  [48,248,48,223],
  [48,223,24,216],
  [118,193,113,186],
  [113,186,275,93],
  [118,193,278,100],
  [281,104,272,88],
  [281,104,300,87],
  [272,88,291,78],
  [299,78,301,105],
  [299,78,276,72],
  [276,72,343,44],
  [343,44,301,105],
  [299,78,343,44],
  [0,350,400,120],
  [0,163,281, 0]], [])


 
    #define pyramid object
    pyramids = Drawing('Pyramids', [[1,248,93,168],
  [93,168,189,250],
  [189,250,312,133],
  [312,133,400,224],
  [93,169,98,294],
  [98,294,187,250],
  [98,294,2,248],
  [189,250,314,290],
  [314,290,398,223],
  [311,136,315,291],
  [135,199,185,82],
  [185,82,262,179],
  [106,177,185,82],
  [58,206,89,214],
  [59,194,90,195],
  [43,219,89,235],
  [30,228,92,253],
  [21,238,89,271],
  [147,133,159,136],
  [138,145,149,150],
  [123,164,142,168],
  [114,176,134,181],
  [210,236,307,253],
  [228,219,307,222],
  [249,200,305,194],
  [279,171,305,165]], [])
  

    
    win=GraphWin("Intro Screen", 600,600)
    win.setBackground(color_rgb(254,201,212))

    Intro=Text(Point(300,50), "Welcome to Point Drawing! \n Select a picture to draw...")
    Intro.setSize(30)
    Intro.setTextColor("white")
    Intro.setFace("helvetica")
    Intro.setStyle("bold italic")
    Intro.draw(win)


    #creates buttons for each shape and displays the correct image 
    
    arwButton = Button(win, Point(150, 175), 100, 50, "Easy")
    arwButton.activate()

    boxImg=Image(Point(425,180), 'images/box.gif')
    boxImg.draw(win)
    boxButton = Button(win, Point(150, 325), 100, 50, "Medium")
    boxButton.activate()

    arrowImg=Image(Point(425,325), 'images/arrow.gif')
    arrowImg.draw(win)

    pyrButton = Button(win, Point(150, 475), 100, 50, "Hard")
    pyrButton.activate()
    pyramidsImg=Image(Point(425,475), 'images/pyramids.gif')
    pyramidsImg.draw(win)

    #conditionals for when each button is clicked, return that class
    while True:
        pt = win.getMouse()

        if boxButton.clicked(pt) is True:
            win.close()
            return arrow
        if arwButton.clicked(pt) is True:
            win.close()
            return box
        if pyrButton.clicked(pt) is True:
            win.close()
            return pyramids

                







