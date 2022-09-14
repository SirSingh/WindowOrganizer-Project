import os
import sys
import pathlib as p
import win32api as win
from window import Window
import screensize as screen

def modifyPath(path):
    text = list(path)
    for i in range(len(text)):
        if text[i] == "\\":
            print(text[i])
            text[i] = "/"
    newPath = ''.join(text)
    #print(newPath)
    #print(path)
    return newPath


class LaunchGroup:
    def __init__(self):

        self.width = win.GetSystemMetrics(0)
        self.height = win.GetSystemMetrics(1)
        # List of applications to be fit; type: class Window
        self.applications = []
        self.focus = 0

    def getApplications(self, inpPath):
        app = Window()
        #direct = input('Please input valid application/file path using / between directories')
        propPath = p.Path(inpPath)
        #propPath = pathlib.Path(inpPath)

        #print(propPath)
        #print(propPath.exists())
        if propPath.exists():
            app.path = propPath
            app.name = app.path.name
            if self.focus == 0:
                print("A focused app takes half the screen. Remaining windows are divided into rest of screen.\n")
                print("Only a single app can be focused on at the moment.\n")
                focBool = input("Focus this a pp? y for yes, n for no.\n")
                if focBool == 'y':
                    self.focus = app
            else:
                self.applications.append(app)
        else:
            print("Please provide valid path")

    def getFit(self):
        if self.focus == 0:
            screen.equalFit(self.applications, self.width, self.height, 0,0)
        else:
            screen.fitHalf(self, self.focus)
            screen.equalFit(self.applications, self.width/2, self.height, self.width/2, 0)

    def moveApplications(self):
        if self.focus != 0:
            self.focus._launchApplication()
            self.focus.findHWND()
            self.focus.resizeWindow()

        for app in self.applications:
            app._launchApplication()
            app.findHWND()
            app.resizeWindow()


    def runLaunchGroup(self):
        while True:
            print("Press q to quit")
            direct = input(r'Please input valid application/file path using \ between directories:')
            if direct.lower() == 'q':
                sys.exit()
            self.getApplications(direct)

            focBool = input("Do you have any other applications to add. Enter y for yes n for no\n")
            if focBool == 'n':
                break
        if len(self.applications) > 0 and self.focus != 0:
            self.getFit()
            self.moveApplications()


if __name__ == '__main__':
    LG = LaunchGroup()
    LG.runLaunchGroup()













