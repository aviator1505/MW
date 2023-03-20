from typing import Union
import psychopy, pylink
import os, time, random, csv
from psychopy import visual, core, event, gui, data
from PIL import Image
import pandas as pd
from psychopy.hardware import keyboard
from EyeLinkCoreGraphicsPsychoPy import EyeLinkCoreGraphicsPsychoPy

# Set up EyeLink connection
eyelink = pylink.EyeLink('100.1.1.1')
eyelink.sendCommand("screen_pixel_coords = 0 0 1919 1079")
eyelink.sendCommand("select_parser_configuration 0")
eyelink.sendCommand("file_event_filter = LEFT,RIGHT,FIXATION,SACCADE,BLINK,MESSAGE,BUTTON")
eyelink.sendCommand("file_sample_data = LEFT,RIGHT,GAZE,AREA,GAZERES,STATUS,HTARGET")
eyelink.sendCommand("link_event_filter = LEFT,RIGHT,FIXATION,SACCADE,BLINK,BUTTON")
eyelink.sendCommand("link_sample_data = LEFT,RIGHT,GAZE,AREA,GAZERES,STATUS,HTARGET")
pylink.openGraphics()
eyelink.doTrackerSetup()

stims = pd.read_csv('All_Stim2.csv')

pci: pd.Series = stims['Pci'].dropna()
pci2 = stims['PCi2'].dropna()
sci = stims['Sci'].dropna()
sci2 = stims['SCi2'].dropna()
trp = stims['trP'].dropna()
lfp = stims['lfP'].dropna()

# Create Data directory
info = {'participant': '', 'gender': ['m', 'f', 'n/a'], 'consent given': False, 'dateStr': data.getDateStr()}
dlg = gui.DlgFromDict(info, fixed=['dateStr'])
if not dlg.OK or not info['consent given']:
    core.quit()

filename = "data/%s_%s" % (info['participant'], info['dateStr'])

# create our experiment object to save data
thisExp = data.ExperimentHandler(name='MW_Eyelink', version='1.0', extraInfo=info, dataFileName=filename)

# Window
win = visual.Window([1920, 1080], fullscr=False, units='pix')
# Keyboard
kb = keyboard.Keyboard()

# Present welcome and instruction screens.
welcome = visual.TextStim(win, text='y')
welcome.draw()
win.flip()

# INSTRUCTION LOOP
instrFile = pci if random.randint(1, 2) == 1 else sci
probeMessage = probeMessage2 = "X"
stimFile = lfp if random.randint(3, 4) == 3 else trp

for idx, val in instrFile.items():
    # create an image stimulus
    img = ImageStim(win, val)
    img.draw()
    win.flip()
    # pause till p presses space.
    event.waitKeys(keyList=['space'])

##ONE TIME INITIALIZATION START

time1 = time2 = resp1 = resp2 = 0
keys = ""
timerStarted2 = False
# start two clocks
mainTimer = core.Clock()
probeTimer = core.Clock()
myCount = 1
looptime = core.Clock()

# ONE TIME INITIALIZATION END

pc_img = ImageStim(win, image='PC_v2.PNG')
sc_img = ImageStim(win, image='SC_v2.PNG')
myCount2 = 1
event.clearEvents()
probe2 = [0, 91, 112, 74,
