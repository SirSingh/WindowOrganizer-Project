# WindowOrganizer-Project
Program to open and move multiple windows in specified monitor arrangement.

Currently the program is non-functional

The issue that remains to be resolved in optaining window handle (HWND) in order to move the window via win32gui.
Current issue seems to be enumeration of windows does not cover all possible options. Currently looking to use enimchildwindows
or other options that will take less time.

Current road map is to complete command-line application, then building gui where greater customization will be availble for window organization.

Program is run through main.py
Each application is set into a window class as defined in window.py, which include methods to manipulate the applications
Screensize.py manages the measurement for application height, width and starting co-ordinate
