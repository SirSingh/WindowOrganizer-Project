import os.path
import win32gui
import psutil
import subprocess
import signal
from time import sleep

import win32process


class Window:

    def __init__(self):
        #Name of application
        self.name = ""
        # Path to launch application
        self.path = ""
        #Assigned location sector for application
        self.sector = 0

        # Move to fn. get size and resize
        self.x = 0
        self.y = 0
        self.height = 100
        self.width = 100

        # Running status of application; default False
        self.open = False

    def _getStatusName(self):
        """Determines if an application is running or not"""
        for prog in psutil.process_iter(attrs=['pid','name']):
            if self.name in prog.info['name']:
                self.pid = prog.info['pid']
                return True
            else:
                return False

    def getStatusPID(self):
        if psutil.pid_exists(self.pid):
            return True
        else:
            return False




    def _closeApplication(self):
        applicationName =  self.path.split('/')[-1]
        if not self.getStatusPID():
            print("Application is not currently running")
        else:
            attempts = 3
            while attempts > 0:
                #subprocess.run(["taskkill","/f", "/IM", applicationName])
                os.kill(self.pid, signal.SIGTERM)
                sleep(2)
                if self.getStatusPID():
                    print(f"Failed to close program on attempt {3-attempts}")
                    attempts -= 1
                else:
                    print(f"Successfully closed program {applicationName}")
                    return True

            # Following executes iff application failed to close
            raise ValueError(f'Failed to close {applicationName}')


    def _launchApplication(self, relaunch=False):
        ''' Launches application using path set by user if not already running and
            restart of program not requested.
                relaunch - Setting True forces application to restart even if currently running '''
        if os.path.exists(self.path):
            # replacing the following with subprocess.Popen(self.path) as popen returns a class with pid access


            prog = subprocess.Popen(list(), executable=self.path.resolve())

            self.pid = prog.pid
            if self.getStatusPID():
                print(f"Progam {self.name} succesfully launched")
                process = psutil.Process(self.pid)
                self.name = process.name()
                print(self.name)
                self.pid = [prog.pid]


                return True
            else:
                print (f"Application {self.name} failed to launch")
                return False
        else:
            print("Provided path:" + self.path + " is invalid. Check path.")
            return False


    def findHWND(self):
        result = None
        def callback(hwnd, appPID):
            nonlocal result
            ctid, cpid = win32process.GetWindowThreadProcessId(hwnd)
            print(cpid)
            print(appPID)
            if cpid == appPID:
                result = hwnd
                print(result)
                return False
            return True
        win32gui.EnumWindows(callback, self.pid)
        self.hwnd = result




    # def findHWND(self):
    #     openApps = win32gui.EnumWindows():
    #     for app in openApps:
    #         if self.pid =

    def resizeWindow(self):
        self.hwnd = win32gui.FindWindow(None, self.name)
        win32gui.MoveWindow(self.hwnd,self.x,self.y,self.width, self.height, True)

    # def getPIDviaName(self):
    #     runningProcesses = []
    #     for prog in psutil.process_iter():
    #         try:
    #             if prog.name().lower() in self.name.lower():
    #                 runningProcesses.append(prog.ppid())
    #         except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess) :
    #             pass
    #     self.pid = runningProcesses

    # def findWindowInPids(self):
    #     '''Find correct window if multiple instances of process are open by iterating through'''
    #     if len(self.pid) == 1:
    #         return self.pid[0]
    #
    #     for pid in self.pid:
    #         applicationName = self.path.split('/')[-1]
    #         prog = psutil.Process(pid=pid)
    #         if applicationName == prog.cmdline()[1]:
    #             self.pid = [prog.ppid()]
    #             return True
    #
    #     print("Failed to find application in findWindowInPids")
    #     return False


    # def get_hwnds_for_pid(self):
    #     def callback(hwnd, hwnds):
    #         if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
    #             _, found_pid = win32process.GetWindowThreadProcessId(hwnd)
    #             if found_pid == self.pid:
    #                 hwnds.append(hwnd)
    #         return True
    #
    #     hwnds = []
    #     win32gui.EnumWindows(callback, hwnds)
    #     self.hwnd = hwnds






