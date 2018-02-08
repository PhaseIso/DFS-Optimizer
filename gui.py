import sys
# For running Python 3.X
if sys.version_info >= (3,0):
    import tkinter as tk
    from tkinter import *
    from tkinter import messagebox
    from tkinter.filedialog import askopenfilename
# For running Python 2.X
else:
    import Tkinter as tk
    from Tkinter import *
    import tkMessageBox
    from tkFileDialog import askopenfilename
import settings
import os
from globalVars import *
import csv
from menu import *

# Starting variables for fixed settings
#lineups, players, maxCost = 0, 0, 0
lineups = StringVar()
players = StringVar()
maxCost = StringVar()
numPos = StringVar()
lineups.set('0')
players.set('0')
maxCost.set('0')
numPos.set('0')

#===========
def enterPressed(event,variable):
    print(variable.get())
    with open('configurations.txt', 'a') as configurations:
        configurations.write('1 ' + str(event.get()+ '\n'))
    variable.set(event.get())
    print(variable.get())
    

#=============
#    Menu
#=============
menu = Menu(settings.app.root)
settings.app.root.config(menu=menu)

#=============
#    FILE
#=============
filemenu = Menu(menu, tearoff=False)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Save Settings", command=Save)
filemenu.add_command(label="Load Settings", command=Load)
filemenu.add_command(label="Options", command=Options)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=settings.app.root.destroy)

#=============
#    CSV
#=============
csvmenu = Menu(menu, tearoff=False)
menu.add_cascade(label="CSV", menu=csvmenu)
csvmenu.add_command(label="Import", command=Import)
csvmenu.add_command(label="Export", command=Export)

#=============
#    HELP
#=============
helpmenu = Menu(menu, tearoff=False)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="GitHub", command=GitHub)
helpmenu.add_command(label="About", command=About)

frame = Frame(settings.app.root, width=settings.app.w, height=settings.app.h, background='white')
frame.pack(fill=BOTH)
frame.pack_propagate(False) # Stop frame from resizing to widgets

#=============
# Top Frame
#=============
top = Frame(frame, width=settings.app.w, height=settings.app.h/2.2, background='white')
top.grid(row=0)
top.grid_propagate(False) # Stop frame from resizing to widgets
for i in range(0,17):
    top.grid_rowconfigure(i, weight=1)
for j in range(0,49):
    top.grid_columnconfigure(j, weight=1)

#================
# Drop Down List
#================
#First Drop
lst = ['Select One']
var = StringVar() 
var.set(lst[0])
drop = OptionMenu(top ,var,*lst)
drop.config(width= 20)
drop.grid(row = 18)

#drop for choosing position
pos = ['Select Position']
vari = StringVar()
vari.set(pos[0])
PosDropDown = OptionMenu(top, vari, *pos)
PosDropDown.config(width = 20)
PosDropDown.grid(row = 4, column = 2)


# Top Widgets
saveSetting = Button(top, text='Save Settings', command=Save)
saveSetting.grid(row=0, column=19)
loadSetting = Button(top, text='Load Settings', command=Load)
loadSetting.grid(row=0, column=20)
addSetting = Button(top, text='Add Setting', command=Add)
addSetting.grid(row=0, column=21)

importBtn = Button(top, text='Import CSV', command=Import)
importBtn.grid(row=16, column=0)
exportBtn = Button(top, text='Export CSV', command=Export)
exportBtn.grid(row=16, column=1)

optimizeBtn = Button(top, text='Optimize', height=2, width=20, command=Optimize)
optimizeBtn.grid(row=15, rowspan=2, column=19, columnspan=3)


setting1 = Label(top, text='Number of Lineups:')
setting1.grid(row=1, sticky=W)
settingLineupsNum = Label(top,textvariable=lineups)
settingLineupsNum.grid(row=1,column = 2, sticky=W)
##user input
lineupNumInput = Entry(top)
lineupNumInput.grid(row=1, column=3, sticky=W)
lineupNumInput.bind('<Return>',(lambda event: enterPressed(lineupNumInput,lineups)))


setting2 = Label(top, text='Number of Players: ')
setting2.grid(row=2, sticky=W)
displayPlayersNum = Label(top,textvariable=players)
displayPlayersNum.grid(row=2,column = 2, sticky=W)

##user input
playerNumInput = Entry(top)
playerNumInput.grid(row=2, column=3,sticky=W)
playerNumInput.bind('<Return>',(lambda event: enterPressed(playerNumInput,players)))


setting3 = Label(top, text='Max Cost: ')
setting3.grid(row=3, sticky=W)
displayCostNum = Label(top,textvariable=maxCost)
displayCostNum.grid(row=3,column = 2, sticky=W)

costNumInput = Entry(top)
costNumInput.grid(row=3, column=3,sticky=W)
costNumInput.bind('<Return>',(lambda event: enterPressed(costNumInput,maxCost)))

setting4 = Label(top, text='Number of players per postion: ')
setting4.grid(row = 4, sticky = W)
#for test purposes can delete later
displayPosAmount = Label(top, textvariable = numPos)
displayPosAmount.grid(row = 4, column = 5, sticky = W)

setting4MaxNum = Label(top, text = 'Max number: ')
setting4MaxNum.grid(row = 4, column = 3, sticky = E)

numOfPosition = Entry(top)
numOfPosition.grid(row = 4, column = 4, sticky = W)
numOfPosition.bind('<Return>',(lambda event: enterPressed(numOfPosition, numPos)))



#=============
# Split Frame
#=============
split = Frame(frame, width=settings.app.w, height=1, background='black')
split.grid(row=18)

#=============
# Bot Frame
#=============
bot = Frame(frame, width=settings.app.w, height=settings.app.h/2, background='white')
bot.grid_propagate(False) # Stop frame from resizing to widgets
for i in range(19,36):
    bot.grid_rowconfigure(i, weight=1)

bottom = Frame(bot, width=settings.app.w, height=settings.app.h/2, background='white')
bottom.pack_propagate(False)

scrollbar = Scrollbar(bottom)

settings.app.root.mainloop()

##writing to text file
##-------------------------------------------------------------------------