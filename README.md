# Estudy Surfing

This is an app for helping you study. Also E.S. is short for Estudy Surfing. 
______________________________________________________________________________
There are two version the cmd version and the regular version(which is the version that uses pygame)
______________________________________________________________________________
# Compiling instructions for both version
------------------------------------------------------------------------------

1.Run 

    cd nextdirectory

 (Change "nextdirectory" to the next folder name) to the root directory in the terminal
______________________________________________________________________________
2.Install python (If you don't have it): https://www.python.org/downloads/
______________________________________________________________________________
3.Run in terminal 

    python -m venv .venv
______________________________________________________________________________
4.Activate the virtual enviorment

Windows:

Note: You may need to run

    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

to allow the activation of the virtual enviorment

If using powershell as terminal then run 
    
    .venv/Scripts/Activate.ps1

but if your using cmd or command promt run 

    activate.bat

Note: There is no need to specify were the bat file is. (Belive me, I tried to.)
Mac or Linux:

In these OSes there are at least 6 terminals that you can use.
Which in term means that there are 4 other commands specific to those terminals
Note: You only need to use one by the terminal your using

bash/zsh:

    source .venv/bin/activate

fish:

    source .venv/bin/activate.fish

csh/tcsh:

    source .venv/bin/activate.csh


pwsh: 

    .venv/bin/Activate.ps1

______________________________________________________________________________
5.Run 

    pip install pyinstaller
______________________________________________________________________________
6.Run 

    pip install pygame

Note: This instruction is only for the regular version
______________________________________________________________________________
7.Run 

    python exe


Note: This will compile the project
______________________________________________________________________________
8.Find the app in the dist folder
______________________________________________________________________________
9.Run the app

Note: The operating system in wich you compile the app is important.
        For example: If you compile the app in windows the app will only run with windows
        no other OS may run the app.

------------------------------------------------------------------------------
# Credits:

Owner:
Crafty5020

Proggramer:
Crafty5020

Art design:
Juli

Sound design:
No one
