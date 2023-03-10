import pandas as pd
import psychopy
from psychopy import visual, core, event, monitors, gui, data
from psychopy.hardware import keyboard
from psychopy.visual import ImageStim
win = visual.Window([1920, 1080], fullscr=False, units='pix')
# Keyboard
kb = keyboard.Keyboard()

stims = pd.read_csv('All_Stim2.csv')

# create a series out of each column
pci = stims['Pci'].dropna()
pci2 = stims['PCi2'].dropna()
sci = stims['Sci'].dropna()
sci2 = stims['SCi2'].dropna()
trp = stims['trP'].dropna()
lfp = stims['lfP'].dropna()
print(pci)
#
# # Loop to display images:
# for idx, val in pci.items():
#     #extract each file name and store it for 1 run of the loop in a variable.
#     pic2show = val
#
#     #create an image stimulus
#     img = ImageStim(win, val)
#     img.draw()
#     win.flip()
#
#     #pause till p presses space.
#     event.waitKeys(keyList= ['space'])
# core.quit()

###### INSTRUCTION LOOP####
for idx, val in trp.items():
    # create an image stimulus
    img = ImageStim(win, val, opacity = 1)
    img.draw()
    win.flip()
    core.wait(2)
    img = ImageStim(win, val, opacity = 0.5)
    img.draw()
    win.flip()
    # pause till p presses space.
    event.waitKeys(keyList=['space'])