import time

import psychopy
import pandas as pd
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, iohub, hardware
from psychopy.visual import Window, TextStim, ImageStim
import os, sys
from psychopy.hardware import keyboard
# First, we read put all the relevant stim image file names into a dataframe.

dat = pd.read_csv('All_Stim.csv')

#######################################################################     Experiment  Instruction Texts                     #######################################################################

welcome_text = '''
Hello! Thank you for participating in our experiment! 

In this experiment, your task is to read a text and answer some questions about its contents in a memory test later on in Qualtrics. 
As you read, we will record your eye movements with the eye tracker you see just in front of you. 

The researcher will now set you up for experiment. Please let them know if you have any questions and/or concerns.

Press "Space bar" to continue. 
'''



#######################################################################     Common Components                                 ######################################################################
win = visual.Window([1920, 1080], fullscr=False, units='pix')
kb = keyboard.Keyboard()
clock = core.Clock()

welcome = psychopy.visual.TextStim(win, text=welcome_text)
welcome.draw()
welcome.flip()
time.sleep(5)
core.quit()