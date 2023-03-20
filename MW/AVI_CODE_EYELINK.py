# ######################################################################    Code Organization Notes
# #######################################################################
#
# The experiment is split into a series of routines that run sequentially (i.e one by one). Within each routine,
# all the components that need to be shown and all condition assignments that dictate the experiment flow are
# constructed. They only are presented on screen if they are *explicitly* summoned.
#
# The script is organized such that all the components are systematically defined according to the routine they
# belong to in one large section. They are then summoned to be presented on-screen in the next section.

# ##########################################################     Imports     ######################################
from __future__ import division
from typing import Union
import psychopy, pylink
import os, time, random, csv
from psychopy import visual, core, event, gui, data
from PIL import Image
import pandas as pd
from psychopy.hardware import keyboard
from EyeLinkCoreGraphicsPsychoPy import EyeLinkCoreGraphicsPsychoPy

# Set up EyeLink connection
eyelink = pylink.EyeLink('100.1.1.1')  # Replace with EyeLink IP address
eyelink.sendCommand("screen_pixel_coords = 0 0 1919 1079")
eyelink.sendCommand("select_parser_configuration 0")
eyelink.sendCommand("file_event_filter = LEFT,RIGHT,FIXATION,SACCADE,BLINK,MESSAGE,BUTTON")
eyelink.sendCommand("file_sample_data = LEFT,RIGHT,GAZE,AREA,GAZERES,STATUS,HTARGET")
eyelink.sendCommand("link_event_filter = LEFT,RIGHT,FIXATION,SACCADE,BLINK,BUTTON")
eyelink.sendCommand("link_sample_data = LEFT,RIGHT,GAZE,AREA,GAZERES,STATUS,HTARGET")
pylink.openGraphics()
eyelink.doTrackerSetup()


stims = pd.read_csv('All_Stim2.csv')

pci: Union[Series, DataFrame] = stims['Pci'].dropna()
pci2 = stims['PCi2'].dropna()
sci = stims['Sci'].dropna()
sci2 = stims['SCi2'].dropna()
trp = stims['trP'].dropna()
lfp = stims['lfP'].dropna()

####################### INITIALIZE Components ########################################.
# Window
win = visual.Window([1920, 1080], fullscr=False, units='pix')
# Keyboard
kb = keyboard.Keyboard()
#######################################################################     Experiment  Instruction Texts                     #######################################################################

welcome_text = '''
Hello! Thank you for participating in our experiment! 

In this experiment, your task is to read a text and answer some questions about its contents in a memory test later on in Qualtrics. 
As you read, we will record your eye movements with the eye tracker you see just in front of you. 

The researcher will now set you up for experiment. Please let them know if you have any questions and/or concerns.

Press "Space bar" to continue. 
'''

##
######################################################################       Condition Assignment                             ##############################################

# Use the machine time as a seed to generate a random number from (allows for closer to "truly random" numbers)
random.seed(int(time.process_time()))
# set variable myRand to a random number (either 1 or 2); myRandP (EITHER 3 OR 4)
rand = random.randint(1, 2)  # random number for choosing experimental condition order
randP = random.randint(3, 4)  # random number for choosing reading pages order

# set new variable 'currCondition' depending on what random number we generated
if rand == 1:
    # 50% chance of being in the PC condition
    currCondition = "PC"
elif rand == 2:
    # 50% chance of being in the SC condition
    currCondition = "SC"

# CREATE A VARIABLE CALLED currConditionP and set it depending on randPage
if randP == 3:
    # 50% chance of being Tropo pages
    currConditionP = "Tropo"
elif randP == 4:
    # 50% chance of being Life pages
    currConditionP = "Life"

# For testing purposes we can set our condition and pages here.
# Just comment out the two lines below to run the experiment randomly.
currCondition = 'SC'
currConditionP = 'Tropo'

###################################################################### File Assignment #####################################################
# 2. setFiles
# SETTING ALL OUR FILE VARIABLES FOR THE EXPERIMENT BASED ON currCondition AND currConditionPs
if currCondition == "PC":
    # if we're in the PC condition then show the PC instructions first run and the SC instructions second run
    # InstrFile: Tuple[str, str, str, str, str] = stimdict['pci']

    instrFile = pci
    # InstrFile2 = pci2
    # if we're in the PC condition then show the PC probe message first run and the SC probe message second run
    probeMessage = "Remember, when the probe appears on screen: \n Press 'i' if your MW was intentional (on purpose), " \
                   "or 'u' if it was unintentional (just happened on its own). \n Press '0' if you were not " \
                   "experiencing MW when the probe appeared. "
    probeMessage2 = "Remember: Press '1' any time you catch yourself mind wandering (MW). \n When prompted, press 'i' " \
                    "if your MW was intentional (on purpose), or 'u' if it was unintentional (just happened on its " \
                    "own). "

elif currCondition == "SC":
    # if we're in the SC condition then show the SC instructions first run and the PC instructions second run
    instrFile = sci
    # InstrFile2 = sci2
    # if we're in the SC condition then show the SC probe message first run and the PC probe message second run
    probeMessage = 'Remember: Press \'1\' any time you catch yourself mind wandering (MW). \n When prompted, ' \
                   'press \'i\' ' \
                   'if your MW was intentional (on purpose), or \'u\' if it was unintentional (just happened on its ' \
                   'own). '
    probeMessage2 = "Remember, when the probe appears on screen: \n Press 'i' if your MW was intentional (on " \
                    "purpose), or 'u' if it was unintentional (just happened on its own). \n Press '0' if you were " \
                    "not experiencing MW when the probe appeared. "

if currConditionP == "Life":
    # if we're in the Life condition then show LifePages first run and TropoPages second run
    # stimFile: Tuple[str, str, str, str, str] = stimdict['lfp']
    # stimFile2 = trp
    stimFile = stims['lfP'].dropna()

elif currConditionP == "Tropo":
    # if we're in the Tropo condition then show TropoPages first run and LifePages second run
    stimFile = stims['trP'].dropna()
    # stimFile2 = lfp

################## Create Data directory ##########################

# store some useful info about this experiment
info = {'participant': '', 'gender': ['m', 'f', 'n/a'], 'consent given': False, 'dateStr': data.getDateStr()}
# present dialog to participant
dlg = gui.DlgFromDict(info, fixed=['dateStr'])
if dlg.OK == False or not info['consent given']:
    core.quit()

filename = "data/%s_%s" % (info['participant'], info['dateStr'])

# create our experiment object to save data
thisExp = data.ExperimentHandler(name='MW_Eyelink', version='1.0',  # not needed, just handy
                                 extraInfo=info,  # the info we created earlier
                                 dataFileName=filename)  # using our string with data/name_date)

####################### INITIALIZE Components ########################################.
# Window
win = visual.Window([1920, 1080], fullscr=False, units='pix')
# Keyboard
kb = keyboard.Keyboard()

############################### Stimuli ###############################
# Screen 1
welcome = visual.TextStim(win, text= welcome_text)
welcome.draw()
win.flip()




# Mind wandering instructions based on Condition defined above.
##### INSTRUCTION LOOP####
# Screen 2
for idx, val in instrFile.items():
    # create an image stimulus
    img = ImageStim(win, val)
    img.draw()
    win.flip()
    # pause till p presses space.
    event.waitKeys(keyList=['space'])

############################### Stimuli ###############################
##ONE TIME INITIALIZATION START
# opacityImage1 = 0  # PC image opacity (by default our probe and intentionality images are hidden)
# opacityImage2 = 0  # SC image opacity
time1 = 0  # variables for recording response time data
time2 = 0
resp1 = 0  # variables for recording key press data
resp2 = 0
printNow = 0  # used to trigger data writing to output file
keys = ""  # stores keypress values
# these three variables are used to start our timers at the right spot and avoid some edge cases
firstLoop2 = True

timerStarted2 = False
# start two clocks
mainTimer = core.Clock()
probeTimer = core.Clock()  # this one stops and restarts every time one of our probe/intentionality images pops up
myCount = 1  # this counts up and tells which value from the probe list we should use
# clear the keyboard buffer just in case they recently pressed a relevant key
looptime = core.Clock()
##ONE TIME INITIALIZATION END

pc_img = ImageStim(win, image='PC_v2.PNG')
sc_img = ImageStim(win, image='SC_v2.PNG')
myCount2 = 1
event.clearEvents()  # clear events just in case they recently pressed a relevant key
# here's a list of the time in seconds between probes change this to adjust the probes for the Reading loop
probe2 = [0, 91, 112, 74, 98, 113, 62, 92, 79, 76, 62]
# first item in probe, 0, never happens because myCount starts at 1
if currCondition == 'SC':
    # make an index to keep track of the iteration of page being displayed.
    current_index = 0

    # Start a loop that will continue until the escape key is pressed
    while current_index != 16:

        # Load the current image
        page = ImageStim(win, image=stimFile.iloc[current_index])

        # Display the current image:
        page.draw()
        win.flip()

        # Wait for key press:
        keys = event.waitKeys()

        if 'space' in keys:
            current_index = (current_index + 1) % len(stimFile)

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
                                TimeAbs)  # log the time that the SC probe appeared (user pressed '1' key)
                thisExp.addData('time_since_last_probe',
                                TimeSinceLast)  # log time since last probe. Should be time since start of experiment if this is the first probe
                thisExp.addData('response_delay', time2)  # log delay from probe appearing to response key being pressed
                thisExp.addData('probe_key_response', resp2)  # log the key response to the probe
                thisExp.addData('condition', currCondition)  # save the current condition
                thisExp.nextEntry()
                probeTimer.reset(0)
                time1 = 0
                time2 = 0
                resp1 = 0
                resp2 = 0
                page.draw()
                win.flip()
        event.clearEvents()

if currCondition == "PC":

    current_index = 0

    # Start a loop that will continue until the escape key is pressed
    while current_index != 16:

        # Load the current image
        page = ImageStim(win, image=stimFile.iloc[current_index])

        # Display the current image:
        page.draw()
        win.flip()

        keys = kb.waitKeys(keyList=['i', 'u', '0', 'space'])

        if 'space' in keys:
            current_index = (current_index + 1) % len(stimFile)

        if (len(probe2) > myCount2) and probeTimer2.getTime() >= probe2[myCount2]:
            pc_img.draw()
            win.flip()
            TimeAbs = mainTimer2.getTime()
            TimeSinceLast = probeTimer2.getTime()

        keys = kb.waitKeys(keyList=['i', 'u', '0'])  # get the time since the last probe popped up

        if '0' in keys or 'i' in keys or 'u' in keys:
            time1 = mainTimer2.getTime() - TimeAbs
            resp1 = keys[0]
            keys = []
            thisExp.addData('probe_appeared', TimeAbs)  # log the time that the PC probe appeared
            thisExp.addData('time_since_last_probe', TimeSinceLast)  # log time since last probe. Should be time since start of experiment if this is the first probe
            thisExp.addData('response_delay', time1)  # log delay from probe appearing to response key being pressed
            thisExp.addData('probe_key_response', resp1)  # log the key response to the probe
            thisExp.addData('condition', currCondition)  # save the current condition
            thisExp.nextEntry()  # if we do not move to the next line in the data file, then any other probes that occur before the end of this routine will overwrite our previous probe data
            probeTimer2.reset(0)
            time1 = 0
            time2 = 0
            resp1 = 0
            resp2 = 0
            myCount2 = myCount2 + 1
