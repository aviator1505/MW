# ##########################################################     Imports     ######################################
from __future__ import division

import pandas as pd
from psychopy import visual
from psychopy.hardware import keyboard
# from EyeLinkCoreGraphicsPsychoPy import EyeLinkCoreGraphicsPsychoPy
from psychopy.visual import ImageStim

stims = pd.read_csv('All_Stim2.csv')
pci = stims['Pci'].dropna()
pci2 = stims['PCi2'].dropna()
sci = stims['Sci'].dropna()
sci2 = stims['SCi2'].dropna()
trp = stims['trP'].dropna()
lfp = stims['lfP'].dropna()
win = visual.Window([1920, 1080], fullscr=False, units='pix')
kb = keyboard.Keyboard()
pc_img = ImageStim(win, image='PC_v2.PNG')
sc_img = ImageStim(win, image='SC_v2.PNG')

for idx, val in trp.items():
    # create an image stimulus
    page = ImageStim(win, val, opacity=1)
    sc_img = ImageStim(win, image='SC_v2.PNG')
    page.draw()
    win.flip()

    kb.waitKeys(keyList=('space', '1')) == 'space' or '1':


        while not kb.waitKeys(keyList=['i', 'u']) == 'i' or 'u':
            sc_img.draw()
            win.flip()
