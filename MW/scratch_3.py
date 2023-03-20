
from typing import Union
import psychopy, pylink
import os, time, random, csv
from psychopy import visual, core, event, gui, data
from PIL import Image
import pandas as pd
from psychopy.hardware import keyboard
from EyeLinkCoreGraphicsPsychoPy import EyeLinkCoreGraphicsPsychoPy

stims = pd.read_csv('All_Stim2.csv')
sci = stims['Sci'].dropna()
trp = stims['trP'].dropna()


# Window
win = visual.Window([1920, 1080], fullscr=False, units='pix')
# Keyboard
kb = keyboard.Keyboard()
# Create Data directory
info = {'participant': '', 'gender': ['m', 'f', 'n/a'], 'consent given': False, 'dateStr': data.getDateStr()}
filename = "data/%s_%s" % (info['participant'], info['dateStr'])

# create our experiment object to save data
thisExp = data.ExperimentHandler(name='MW_Eyelink', version='1.0',
                                 extraInfo=info,
                                 dataFileName=filename)
##ONE TIME INITIALIZATION START

time1 = 0
time2 = 0
resp1 = 0
resp2 = 0
keys = ""
timerStarted2 = False
# start two clocks
mainTimer = core.Clock()
probeTimer = core.Clock()
myCount = 1
looptime = core.Clock()

# ONE TIME INITIALIZATION END
sc_img = ImageStim(win, image='SC_v2.PNG')
myCount2 = 1
event.clearEvents()

# Stimulus Display

current_index = 0

while current_index != 16:

    # Load the current image
    page = ImageStim(win, image=trp.iloc[current_index])

    # Display the current image:
    page.draw()
    win.flip()

    # Wait for key press:
    keys = event.waitKeys()

    if 'space' in keys:
        current_index = (current_index + 1) % len(trp)

    if '1' in keys:
        TimeAbs = mainTimer.getTime()
        TimeSinceLast = probeTimer.getTime()
        sc_img.draw()
        win.flip()

        keys = kb.waitKeys(keyList=['i', 'u'])

        if 'i' in keys or 'u' in keys:
            time2 = mainTimer.getTime() - TimeAbs
            resp2 = keys[-1]
            thisExp.addData('probe_appeared',
                            TimeAbs)
            thisExp.addData('time_since_last_probe',
                            TimeSinceLast)
            thisExp.addData('response_delay', time2)
            thisExp.addData('probe_key_response', resp2)
            thisExp.addData('condition', trp)
            thisExp.nextEntry()
            probeTimer.reset(0)
            time1 = 0
            time2 = 0
            resp1 = 0
            resp2 = 0
            page.draw()
            win.flip()
    event.clearEvents()

