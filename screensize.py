
from main import LaunchGroup
# Screen is made

# Sectors are assigned to each application

def fitHalf(window,launch, side='left'):
    '''Provides coordinates for rectangle to take half the screen on given side
            resH - int - resolution height for maximum size avaible height
            resW - int - resolution width for max availible width
            side - string - either 'right' or 'left' for rectangle to take from larger rectangle'''

    window.width = launch.width/2
    window.height = launch.height/2

    if side == 'left':
        window.x = 0
        window.y = 0
    else:
        window.x = launch.width
        window.height = 0

def equalFit(applications, resW, resH, resX, resY, fitSty= 'horizontal'):
    '''Provides coordinates to fit numR amount of rectangles in rectangle space given by resW, resH starting at resX and resY

    applications - list of Class Window - Applications to be fit into provided space
    resW - int - width of rectangle to fit numR amount of rectangles in
    resH - int - height of rectangle to fit numR amount of rectangles in
    resX - int - x-value of bottom left corner of rectangle to fit remaining rectangles in
    resY - int - y-value of bottom left corner of rectangle to fit remaining rectagnles in
    fitSty - str - either 'horizontal' or 'vertical' depnding on desired fit of rectangles

    Modifies sets value in each window class in the list 'applications'
    '''

    numR = len(applications)
    startX = resX
    startY = resY

    if fitSty == 'horizontal':
        perRw = resW
        perRh = resH/numR

        for app in applications:
            app.height = perRh
            app.width = perRw
            app.x = startX
            app.y = startY

            startY += perRh

    else:
        perRw = resW/numR
        perRh = resH

        for app in applications:
            app.height = perRh
            app.width = perRw
            app.x = startX
            app.y = startY

            startX += perRw












