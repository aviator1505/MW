#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.5),
    on February 24, 2023, at 18:28
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

import psychopy

psychopy.useVersion('2022.2.5')

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, iohub, hardware
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.5'
expName = 'COPY_Eyetracking_MW_reading6_08_noP_WORKING'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
    'session': '001',
}
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
                                 extraInfo=expInfo, runtimeInfo=None,
                                 originPath='D:\\Lab Research\\BAR Lab\\VR\\Code\\Leilani MW Eyetracking\\ET_MW_DEV.py',
                                 savePickle=True, saveWideText=True,
                                 dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename + '.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[2048, 1152], fullscr=True, screen=0,
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[1.0000, 1.0000, 1.0000], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "Launch" ---
# Run 'Begin Experiment' code from Condition_Assign
# import what we need to generate a random number
import random, xlrd
import time

# Use the machine time as a seed to generate a random number from (allows for closer to "truly random" numbers)
random.seed(time.process_time())
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

# CREATE A VARIABLE CALLED currConditionP and set it depending on randP
if randP == 3:
    # 50% chance of being Tropo pages
    currConditionP = "Tropo"
elif randP == 4:
    # 50% chance of being Life pages
    currConditionP = "Life"

# For testing purposes we can set our condition and pages here.
# Just comment out the two lines below to run the experiment randomly.
# currCondition = "SC"
# currConditionP = "Tropo"


# --- Initialize components for Routine "setFiles" ---
# Run 'Begin Experiment' code from code_8
# SETTING ALL OUR FILE VARIABLES FOR THE EXPERIMENT BASED ON currCondition AND currConditionPs
if currCondition == "PC":
    # if we're in the PC condition then show the PC instructions first run and the SC instructions second run
    InstrFile = "InstrFile/Instr_PC.csv"
    InstrFile2 = "InstrFile/Instr_SC_v2.csv"
    # if we're in the PC condition then show the PC probe message first run and the SC probe message second run
    probeMessage = "Remember, when the probe appears on screen: \n Press 'i' if your MW was intentional (on purpose), or 'u' if it was unintentional (just happened on its own). \n Press '0' if you were not experiencing MW when the probe appeared."
    probeMessage2 = "Remember: Press '1' any time you catch yourself mind wandering (MW). \n When prompted, press 'i' if your MW was intentional (on purpose), or 'u' if it was unintentional (just happened on its own)."
elif currCondition == "SC":
    # if we're in the SC condition then show the SC instructions first run and the PC instructions second run
    InstrFile = "InstrFile/Instr_SC.csv"
    InstrFile2 = "InstrFile/Instr_PC_v2.csv"
    # if we're in the SC condition then show the SC probe message first run and the PC probe message second run
    probeMessage = "Remember: Press '1' any time you catch yourself mind wandering (MW). \n When prompted, press 'i' if your MW was intentional (on purpose), or 'u' if it was unintentional (just happened on its own)."
    probeMessage2 = "Remember, when the probe appears on screen: \n Press 'i' if your MW was intentional (on purpose), or 'u' if it was unintentional (just happened on its own). \n Press '0' if you were not experiencing MW when the probe appeared."

if currConditionP == "Life":
    # if we're in the Life condition then show LifePages first run and TropoPages second run
    stimFile = "LifePages.csv"
    stimFile2 = "TropoPages.csv"
    # if we're in the Life condition then show Life quiz questions first run and Tropo quiz questions second run
    quizFile = "lifeQs.csv"
    quizFile2 = "tropoQs.csv"

elif currConditionP == "Tropo":
    # if we're in the Tropo condition then show TropoPages first run and LifePages second run
    stimFile = "TropoPages.csv"
    stimFile2 = "LifePages.csv"
    # if we're in the Tropo condition then show Tropo quiz questions first run and Life quiz questions second run
    quizFile = "tropoQs.csv"
    quizFile2 = "lifeQs.csv"

# All the above variables will be used in later components as such:
# InstrFile used in MWdefinitions loop as the csv file to pull instruction images from
# InstrFile2 used in MWdefinitions2 loop as the csv file to pull instruction images from
# probeMessage used in IntroExp as display text
# probeMessage2 used in IntroExp2 as display text
# stimFile used in ReadingLoop as the csv file to pull reading page images from
# stimFile2 used in ReadingLoop2 as the csv file to pull reading page images from
# quizFile used in QuizLoop as the csv file to pull quiz question images from
# quizFile2 used in QuizLoop2 as the csv file to pull quiz question images from


# --- Initialize components for Routine "MW_def" ---
MWdefInstr = visual.ImageStim(
    win=win,
    name='MWdefInstr',
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1, 0.8),
    color=[1, 1, 1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
MWdefInstr_key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "IntroExp" ---
text = visual.TextStim(win=win, name='text',
                       text=probeMessage,
                       font='Open Sans',
                       pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0,
                       color='white', colorSpace='rgb', opacity=1.0,
                       languageStyle='LTR',
                       depth=0.0);
IntroExp_key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "PageSkipping" ---
NoSkipping = visual.TextStim(win=win, name='NoSkipping',
                             text='Please read at your normal pace and do not skip pages.\n\n\n(press spacebar to continue)',
                             font='Open Sans',
                             pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0,
                             color='white', colorSpace='rgb', opacity=None,
                             languageStyle='LTR',
                             depth=0.0);
key_Skip = keyboard.Keyboard()

# --- Initialize components for Routine "Reading" ---
# Run 'Begin Experiment' code from Probe_Code
##ONE TIME INITIALIZATION START
# setting a bunch of defaults here (we will reset these in every practice or reading loop)
opacityImage1 = 0  # PC image opacity (by default our probe and intentionality images are hidden)
opacityImage2 = 0  # SC image opacity
time1 = 0  # variables for recording response time data
time2 = 0
resp1 = 0  # variables for recording key press data
resp2 = 0
printNow = 0  # used to trigger data writing to output file
keys = ""  # stores keypress values
# these three variables are used to start our timers at the right spot and avoid some edge cases
firstLoop2 = True
firstRoutine2 = True
timerStarted2 = False

# start two clocks
mainTimer2 = core.Clock()  # this one just runs for the whole PracticeTrial loop
probeTimer2 = core.Clock()  # this one stops and restarts every time one of our probe/intentionality images pops up

myCount = 1  # this counts up and tells which value from the probe list we should use

# import some stuff just in case
import random, copy
from random import randint
from decimal import *
import csv
from numpy import *
from psychopy import core, event

event.getKeys()  # clear the keyboard buffer just in case they recently pressed a relevant key
##ONE TIME INITIALIZATION END

# Counter for iterating through our probe2 list
myCount2 = 1

event.clearEvents()  # clear events just in case they recently pressed a relevant key

# here's a list of the time in seconds between probes
# change this to adjust the probes for the Reading loop
probe2 = [0, 91, 112, 74, 98, 113, 62, 92, 79, 76, 62]
# first item in probe, 0, never happens because myCount starts at 1
Reading_key_resp = keyboard.Keyboard()
imagePages = visual.ImageStim(
    win=win,
    name='imagePages',
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.85, 0.85),
    color=[1, 1, 1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
PCProbe = visual.ImageStim(
    win=win,
    name='PCProbe',
    image='images/PC_v2.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1, 0.85),
    color=[1, 1, 1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
SCProbe = visual.ImageStim(
    win=win,
    name='SCProbe',
    image='images/SC_v2.png', mask=None, anchor='center',
    ori=0, pos=(0, 0), size=(1, 0.85),
    color=[1, 1, 1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)

# --- Initialize components for Routine "EndText" ---
EndExpText = visual.TextStim(win=win, name='EndExpText',
                             text="Thank you for participating in this experiment!\n\nPlease let the research assistant know if you would like to be debriefed.\n\nThank you!\n\n(Press 'space' to continue)",
                             font='Open Sans',
                             pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0,
                             color='white', colorSpace='rgb', opacity=None,
                             languageStyle='LTR',
                             depth=0.0);
key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "IntroExp2" ---
probe_message = visual.TextStim(win=win, name='probe_message',
                                text=probeMessage2,
                                font='Open Sans',
                                pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0,
                                color='white', colorSpace='rgb', opacity=None,
                                languageStyle='LTR',
                                depth=0.0);
IntroExp2_key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "PageSkipping" ---
NoSkipping = visual.TextStim(win=win, name='NoSkipping',
                             text='Please read at your normal pace and do not skip pages.\n\n\n(press spacebar to continue)',
                             font='Open Sans',
                             pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0,
                             color='white', colorSpace='rgb', opacity=None,
                             languageStyle='LTR',
                             depth=0.0);
key_Skip = keyboard.Keyboard()

# --- Initialize components for Routine "Reading2" ---
Reading2_key_resp = keyboard.Keyboard()
imagePages2 = visual.ImageStim(
    win=win,
    name='imagePages2',
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.85, 0.85),
    color=[1, 1, 1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
PCProbe2 = visual.ImageStim(
    win=win,
    name='PCProbe2',
    image='images/PC_v2.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1, 0.85),
    color=[1, 1, 1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
SCProbe2 = visual.ImageStim(
    win=win,
    name='SCProbe2',
    image='images/SC_v2.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1, 0.85),
    color=[1, 1, 1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
# Run 'Begin Experiment' code from code_2
# use new true/false variables so that the values from our Practice loop don't affect the functionality of the Reading loop
firstLoop4 = True
firstRoutine4 = True
timerStarted4 = False

# start two new clocks so the values of the previous clocks don't affect this loop
mainTimer4 = core.Clock()
probeTimer4 = core.Clock()

# create a new counter so the value of our old counter doesn't carry over to this loop
myCount4 = 1

event.clearEvents()

# here's a list of the time in seconds between probes
# change this to adjust the probes for the Quiz2 loop
probe4 = [0, 91, 112, 74, 98, 113, 62, 92, 79, 76, 62]
# first item in probe, 0, never happens because myCount starts at 1

# --- Initialize components for Routine "EndText" ---
EndExpText = visual.TextStim(win=win, name='EndExpText',
                             text="Thank you for participating in this experiment!\n\nPlease let the research assistant know if you would like to be debriefed.\n\nThank you!\n\n(Press 'space' to continue)",
                             font='Open Sans',
                             pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0,
                             color='white', colorSpace='rgb', opacity=None,
                             languageStyle='LTR',
                             depth=0.0);
key_resp = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "Launch" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
LaunchComponents = []
for thisComponent in LaunchComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Launch" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in LaunchComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Launch" ---
for thisComponent in LaunchComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Launch" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "setFiles" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
setFilesComponents = []
for thisComponent in setFilesComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "setFiles" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in setFilesComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "setFiles" ---
for thisComponent in setFilesComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "setFiles" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
MWdefinitions = data.TrialHandler(nReps=1.0, method='sequential',
                                  extraInfo=expInfo, originPath=-1,
                                  trialList=data.importConditions(InstrFile),
                                  seed=None, name='MWdefinitions')
thisExp.addLoop(MWdefinitions)  # add the loop to the experiment
thisMWdefinition = MWdefinitions.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisMWdefinition.rgb)
if thisMWdefinition != None:
    for paramName in thisMWdefinition:
        exec('{} = thisMWdefinition[paramName]'.format(paramName))

for thisMWdefinition in MWdefinitions:
    currentLoop = MWdefinitions
    # abbreviate parameter names if possible (e.g. rgb = thisMWdefinition.rgb)
    if thisMWdefinition != None:
        for paramName in thisMWdefinition:
            exec('{} = thisMWdefinition[paramName]'.format(paramName))

    # --- Prepare to start Routine "MW_def" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    MWdefInstr.setImage(chInstrSlide)
    MWdefInstr_key_resp.keys = []
    MWdefInstr_key_resp.rt = []
    _MWdefInstr_key_resp_allKeys = []
    # keep track of which components have finished
    MW_defComponents = [MWdefInstr, MWdefInstr_key_resp]
    for thisComponent in MW_defComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1

    # --- Run Routine "MW_def" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *MWdefInstr* updates
        if MWdefInstr.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            MWdefInstr.frameNStart = frameN  # exact frame index
            MWdefInstr.tStart = t  # local t and not account for scr refresh
            MWdefInstr.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(MWdefInstr, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'MWdefInstr.started')
            MWdefInstr.setAutoDraw(True)

        # *MWdefInstr_key_resp* updates
        if MWdefInstr_key_resp.status == NOT_STARTED and t >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            MWdefInstr_key_resp.frameNStart = frameN  # exact frame index
            MWdefInstr_key_resp.tStart = t  # local t and not account for scr refresh
            MWdefInstr_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(MWdefInstr_key_resp, 'tStartRefresh')  # time at next scr refresh
            MWdefInstr_key_resp.status = STARTED
            # keyboard checking is just starting
            MWdefInstr_key_resp.clock.reset()  # now t=0
        if MWdefInstr_key_resp.status == STARTED:
            theseKeys = MWdefInstr_key_resp.getKeys(keyList=['space', ], waitRelease=False)
            _MWdefInstr_key_resp_allKeys.extend(theseKeys)
            if len(_MWdefInstr_key_resp_allKeys):
                MWdefInstr_key_resp.keys = _MWdefInstr_key_resp_allKeys[-1].name  # just the last key pressed
                MWdefInstr_key_resp.rt = _MWdefInstr_key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in MW_defComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # --- Ending Routine "MW_def" ---
    for thisComponent in MW_defComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "MW_def" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()

# completed 1.0 repeats of 'MWdefinitions'


# --- Prepare to start Routine "IntroExp" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
IntroExp_key_resp.keys = []
IntroExp_key_resp.rt = []
_IntroExp_key_resp_allKeys = []
# keep track of which components have finished
IntroExpComponents = [text, IntroExp_key_resp]
for thisComponent in IntroExpComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "IntroExp" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text.started')
        text.setAutoDraw(True)

    # *IntroExp_key_resp* updates
    if IntroExp_key_resp.status == NOT_STARTED and t >= 0.0 - frameTolerance:
        # keep track of start time/frame for later
        IntroExp_key_resp.frameNStart = frameN  # exact frame index
        IntroExp_key_resp.tStart = t  # local t and not account for scr refresh
        IntroExp_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(IntroExp_key_resp, 'tStartRefresh')  # time at next scr refresh
        IntroExp_key_resp.status = STARTED
        # keyboard checking is just starting
        IntroExp_key_resp.clock.reset()  # now t=0
    if IntroExp_key_resp.status == STARTED:
        theseKeys = IntroExp_key_resp.getKeys(keyList=['space'], waitRelease=False)
        _IntroExp_key_resp_allKeys.extend(theseKeys)
        if len(_IntroExp_key_resp_allKeys):
            IntroExp_key_resp.keys = _IntroExp_key_resp_allKeys[-1].name  # just the last key pressed
            IntroExp_key_resp.rt = _IntroExp_key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False

    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in IntroExpComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "IntroExp" ---
for thisComponent in IntroExpComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "IntroExp" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "PageSkipping" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_Skip.keys = []
key_Skip.rt = []
_key_Skip_allKeys = []
# keep track of which components have finished
PageSkippingComponents = [NoSkipping, key_Skip]
for thisComponent in PageSkippingComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "PageSkipping" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *NoSkipping* updates
    if NoSkipping.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
        # keep track of start time/frame for later
        NoSkipping.frameNStart = frameN  # exact frame index
        NoSkipping.tStart = t  # local t and not account for scr refresh
        NoSkipping.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(NoSkipping, 'tStartRefresh')  # time at next scr refresh
        NoSkipping.setAutoDraw(True)

    # *key_Skip* updates
    if key_Skip.status == NOT_STARTED and t >= 0.0 - frameTolerance:
        # keep track of start time/frame for later
        key_Skip.frameNStart = frameN  # exact frame index
        key_Skip.tStart = t  # local t and not account for scr refresh
        key_Skip.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_Skip, 'tStartRefresh')  # time at next scr refresh
        key_Skip.status = STARTED
        # keyboard checking is just starting
        key_Skip.clock.reset()  # now t=0
        key_Skip.clearEvents(eventType='keyboard')
    if key_Skip.status == STARTED:
        theseKeys = key_Skip.getKeys(keyList=['space'], waitRelease=False)
        _key_Skip_allKeys.extend(theseKeys)
        if len(_key_Skip_allKeys):
            key_Skip.keys = _key_Skip_allKeys[-1].name  # just the last key pressed
            key_Skip.rt = _key_Skip_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False

    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in PageSkippingComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "PageSkipping" ---
for thisComponent in PageSkippingComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "PageSkipping" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
ReadingLoop = data.TrialHandler(nReps=1.0, method='sequential',
                                extraInfo=expInfo, originPath=-1,
                                trialList=data.importConditions(stimFile),
                                seed=None, name='ReadingLoop')
thisExp.addLoop(ReadingLoop)  # add the loop to the experiment
thisReadingLoop = ReadingLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisReadingLoop.rgb)
if thisReadingLoop != None:
    for paramName in thisReadingLoop:
        exec('{} = thisReadingLoop[paramName]'.format(paramName))

for thisReadingLoop in ReadingLoop:
    currentLoop = ReadingLoop
    # abbreviate parameter names if possible (e.g. rgb = thisReadingLoop.rgb)
    if thisReadingLoop != None:
        for paramName in thisReadingLoop:
            exec('{} = thisReadingLoop[paramName]'.format(paramName))

    # --- Prepare to start Routine "Reading" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from Probe_Code
    # Reset a bunch of our defaults at the start of this loop. We only do this once.
    # This stops the values from our previous practice loop from affecting this reading loop.
    if firstRoutine2:
        firstRoutine2 = False
        mainTimer2.reset(0)
        probeTimer2.reset(0)
        timerStarted2 = True
    Reading_key_resp.keys = []
    Reading_key_resp.rt = []
    _Reading_key_resp_allKeys = []
    imagePages.setImage(ChPage)
    # keep track of which components have finished
    ReadingComponents = [Reading_key_resp, imagePages, PCProbe, SCProbe]
    for thisComponent in ReadingComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1

    # --- Run Routine "Reading" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from Probe_Code
        keys = event.getKeys()

        if (mainTimer2.getTime() > 1080) and timerStarted2:
            continueRoutine = False  # quit every routine once the main timer goes over 18 minutes

        if firstLoop2:
            keys = []
            event.clearEvents()

        if currCondition == 'SC':
            if Reading_key_resp.keys == 'space':
                continueRoutine = False

            if '1' in keys:
                opacityImage2 = 1
                TimeAbs = mainTimer2.getTime()
                TimeSinceLast = probeTimer2.getTime()
                keys = []
                event.clearEvents()

            if (opacityImage2 == 1) and ('u' in keys or 'i' in keys):
                opacityImage2 = 0
                time2 = mainTimer2.getTime() - TimeAbs
                resp2 = keys[0]
                keys = []
                event.clearEvents()
                printNow = 1

            if printNow == 1:
                thisExp.addData('probe_appeared',
                                TimeAbs)  # log the time that the SC probe appeared (user pressed '1' key)
                thisExp.addData('time_since_last_probe',
                                TimeSinceLast)  # log time since last probe. Should be time since start of experiment if this is the first probe
                thisExp.addData('response_delay', time2)  # log delay from probe appearing to response key being pressed
                thisExp.addData('probe_key_response', resp2)  # log the key response to the probe
                thisExp.addData('condition', currCondition)  # save the current condition
                thisExp.nextEntry()  # if we do not move to the next line in the data file, then any other probes that occur before the end of this routine will overwrite our previous probe data
                probeTimer2.reset(0)
                time1 = 0
                time2 = 0
                resp1 = 0
                resp2 = 0
                printNow = 0

        if currCondition == 'PC':
            if Reading_key_resp.keys == 'space':
                continueRoutine = False

            if opacityImage1 != 1 and (len(probe2) > myCount2) and probeTimer2.getTime() >= probe2[myCount2]:
                opacityImage1 = 1
                TimeAbs = mainTimer2.getTime()
                TimeSinceLast = probeTimer2.getTime()  # get the time since the last probe popped up

            if opacityImage1 == 1 and ('0' in keys or 'i' in keys or 'u' in keys):
                opacityImage1 = 0
                time1 = mainTimer2.getTime() - TimeAbs
                resp1 = keys[0]
                keys = []
                event.clearEvents()
                printNow = 1

            if printNow == 1:
                printNow = 0
                thisExp.addData('probe_appeared', TimeAbs)  # log the time that the PC probe appeared
                thisExp.addData('time_since_last_probe',
                                TimeSinceLast)  # log time since last probe. Should be time since start of experiment if this is the first probe
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

        firstLoop2 = False

        # *Reading_key_resp* updates
        waitOnFlip = False
        if Reading_key_resp.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            Reading_key_resp.frameNStart = frameN  # exact frame index
            Reading_key_resp.tStart = t  # local t and not account for scr refresh
            Reading_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Reading_key_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Reading_key_resp.started')
            Reading_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Reading_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Reading_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Reading_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = Reading_key_resp.getKeys(keyList=['space', ], waitRelease=False)
            _Reading_key_resp_allKeys.extend(theseKeys)
            if len(_Reading_key_resp_allKeys):
                Reading_key_resp.keys = _Reading_key_resp_allKeys[-1].name  # just the last key pressed
                Reading_key_resp.rt = _Reading_key_resp_allKeys[-1].rt

        # *imagePages* updates
        if imagePages.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            imagePages.frameNStart = frameN  # exact frame index
            imagePages.tStart = t  # local t and not account for scr refresh
            imagePages.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imagePages, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imagePages.started')
            imagePages.setAutoDraw(True)

        # *PCProbe* updates
        if PCProbe.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            PCProbe.frameNStart = frameN  # exact frame index
            PCProbe.tStart = t  # local t and not account for scr refresh
            PCProbe.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(PCProbe, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'PCProbe.started')
            PCProbe.setAutoDraw(True)
        if PCProbe.status == STARTED:  # only update if drawing
            PCProbe.setOpacity(opacityImage1, log=False)

        # *SCProbe* updates
        if SCProbe.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            SCProbe.frameNStart = frameN  # exact frame index
            SCProbe.tStart = t  # local t and not account for scr refresh
            SCProbe.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(SCProbe, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'SCProbe.started')
            SCProbe.setAutoDraw(True)
        if SCProbe.status == STARTED:  # only update if drawing
            SCProbe.setOpacity(opacityImage2, log=False)

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ReadingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # --- Ending Routine "Reading" ---
    for thisComponent in ReadingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if Reading_key_resp.keys in ['', [], None]:  # No response was made
        Reading_key_resp.keys = None
    ReadingLoop.addData('Reading_key_resp.keys', Reading_key_resp.keys)
    if Reading_key_resp.keys != None:  # we had a response
        ReadingLoop.addData('Reading_key_resp.rt', Reading_key_resp.rt)
    # the Routine "Reading" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()

# completed 1.0 repeats of 'ReadingLoop'


# --- Prepare to start Routine "EndText" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
EndTextComponents = [EndExpText, key_resp]
for thisComponent in EndTextComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "EndText" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *EndExpText* updates
    if EndExpText.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
        # keep track of start time/frame for later
        EndExpText.frameNStart = frameN  # exact frame index
        EndExpText.tStart = t  # local t and not account for scr refresh
        EndExpText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(EndExpText, 'tStartRefresh')  # time at next scr refresh
        EndExpText.setAutoDraw(True)
    if EndExpText.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > EndExpText.tStartRefresh + 10 - frameTolerance:
            # keep track of stop time/frame for later
            EndExpText.tStop = t  # not accounting for scr refresh
            EndExpText.frameNStop = frameN  # exact frame index
            EndExpText.setAutoDraw(False)

    # *key_resp* updates
    if key_resp.status == NOT_STARTED and t >= 0.0 - frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        key_resp.clock.reset()  # now t=0
        key_resp.clearEvents(eventType='keyboard')
    if key_resp.status == STARTED:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False

    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndTextComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "EndText" ---
for thisComponent in EndTextComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "EndText" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "IntroExp2" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
IntroExp2_key_resp.keys = []
IntroExp2_key_resp.rt = []
_IntroExp2_key_resp_allKeys = []
# keep track of which components have finished
IntroExp2Components = [probe_message, IntroExp2_key_resp]
for thisComponent in IntroExp2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "IntroExp2" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *probe_message* updates
    if probe_message.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
        # keep track of start time/frame for later
        probe_message.frameNStart = frameN  # exact frame index
        probe_message.tStart = t  # local t and not account for scr refresh
        probe_message.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(probe_message, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'probe_message.started')
        probe_message.setAutoDraw(True)

    # *IntroExp2_key_resp* updates
    waitOnFlip = False
    if IntroExp2_key_resp.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
        # keep track of start time/frame for later
        IntroExp2_key_resp.frameNStart = frameN  # exact frame index
        IntroExp2_key_resp.tStart = t  # local t and not account for scr refresh
        IntroExp2_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(IntroExp2_key_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'IntroExp2_key_resp.started')
        IntroExp2_key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(IntroExp2_key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(IntroExp2_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if IntroExp2_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = IntroExp2_key_resp.getKeys(keyList=['space'], waitRelease=False)
        _IntroExp2_key_resp_allKeys.extend(theseKeys)
        if len(_IntroExp2_key_resp_allKeys):
            IntroExp2_key_resp.keys = _IntroExp2_key_resp_allKeys[-1].name  # just the last key pressed
            IntroExp2_key_resp.rt = _IntroExp2_key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False

    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in IntroExp2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "IntroExp2" ---
for thisComponent in IntroExp2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if IntroExp2_key_resp.keys in ['', [], None]:  # No response was made
    IntroExp2_key_resp.keys = None
thisExp.addData('IntroExp2_key_resp.keys', IntroExp2_key_resp.keys)
if IntroExp2_key_resp.keys != None:  # we had a response
    thisExp.addData('IntroExp2_key_resp.rt', IntroExp2_key_resp.rt)
thisExp.nextEntry()
# the Routine "IntroExp2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "PageSkipping" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_Skip.keys = []
key_Skip.rt = []
_key_Skip_allKeys = []
# keep track of which components have finished
PageSkippingComponents = [NoSkipping, key_Skip]
for thisComponent in PageSkippingComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "PageSkipping" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *NoSkipping* updates
    if NoSkipping.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
        # keep track of start time/frame for later
        NoSkipping.frameNStart = frameN  # exact frame index
        NoSkipping.tStart = t  # local t and not account for scr refresh
        NoSkipping.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(NoSkipping, 'tStartRefresh')  # time at next scr refresh
        NoSkipping.setAutoDraw(True)

    # *key_Skip* updates
    if key_Skip.status == NOT_STARTED and t >= 0.0 - frameTolerance:
        # keep track of start time/frame for later
        key_Skip.frameNStart = frameN  # exact frame index
        key_Skip.tStart = t  # local t and not account for scr refresh
        key_Skip.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_Skip, 'tStartRefresh')  # time at next scr refresh
        key_Skip.status = STARTED
        # keyboard checking is just starting
        key_Skip.clock.reset()  # now t=0
        key_Skip.clearEvents(eventType='keyboard')
    if key_Skip.status == STARTED:
        theseKeys = key_Skip.getKeys(keyList=['space'], waitRelease=False)
        _key_Skip_allKeys.extend(theseKeys)
        if len(_key_Skip_allKeys):
            key_Skip.keys = _key_Skip_allKeys[-1].name  # just the last key pressed
            key_Skip.rt = _key_Skip_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False

    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in PageSkippingComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "PageSkipping" ---
for thisComponent in PageSkippingComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "PageSkipping" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Reading2" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
Reading2_key_resp.keys = []
Reading2_key_resp.rt = []
_Reading2_key_resp_allKeys = []
imagePages2.setImage(ChPage)
# Run 'Begin Routine' code from code_2
if firstRoutine4:
    opacityImage1 = 0
    opacityImage2 = 0
    time1 = 0
    time2 = 0
    resp1 = 0
    resp2 = 0
    printNow = 0
    keys = ""
    firstRoutine4 = False
    mainTimer4.reset(0)
    probeTimer4.reset(0)
    timerStarted4 = True
# keep track of which components have finished
Reading2Components = [Reading2_key_resp, imagePages2, PCProbe2, SCProbe2]
for thisComponent in Reading2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Reading2" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *Reading2_key_resp* updates
    waitOnFlip = False
    if Reading2_key_resp.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
        # keep track of start time/frame for later
        Reading2_key_resp.frameNStart = frameN  # exact frame index
        Reading2_key_resp.tStart = t  # local t and not account for scr refresh
        Reading2_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Reading2_key_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Reading2_key_resp.started')
        Reading2_key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(Reading2_key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(Reading2_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Reading2_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = Reading2_key_resp.getKeys(keyList=['space'], waitRelease=False)
        _Reading2_key_resp_allKeys.extend(theseKeys)
        if len(_Reading2_key_resp_allKeys):
            Reading2_key_resp.keys = _Reading2_key_resp_allKeys[-1].name  # just the last key pressed
            Reading2_key_resp.rt = _Reading2_key_resp_allKeys[-1].rt

    # *imagePages2* updates
    if imagePages2.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
        # keep track of start time/frame for later
        imagePages2.frameNStart = frameN  # exact frame index
        imagePages2.tStart = t  # local t and not account for scr refresh
        imagePages2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(imagePages2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'imagePages2.started')
        imagePages2.setAutoDraw(True)

    # *PCProbe2* updates
    if PCProbe2.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
        # keep track of start time/frame for later
        PCProbe2.frameNStart = frameN  # exact frame index
        PCProbe2.tStart = t  # local t and not account for scr refresh
        PCProbe2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(PCProbe2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'PCProbe2.started')
        PCProbe2.setAutoDraw(True)
    if PCProbe2.status == STARTED:  # only update if drawing
        PCProbe2.setOpacity(opacityImage1, log=False)

    # *SCProbe2* updates
    if SCProbe2.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
        # keep track of start time/frame for later
        SCProbe2.frameNStart = frameN  # exact frame index
        SCProbe2.tStart = t  # local t and not account for scr refresh
        SCProbe2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(SCProbe2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'SCProbe2.started')
        SCProbe2.setAutoDraw(True)
    if SCProbe2.status == STARTED:  # only update if drawing
        SCProbe2.setOpacity(opacityImage2, log=False)
    # Run 'Each Frame' code from code_2
    keys = event.getKeys()

    if (mainTimer4.getTime() > 1080) and timerStarted4:
        continueRoutine = False

    if firstLoop4:
        keys = []
        event.clearEvents()

    # this is the self-caught condition but we check if we're in PC because this is run 2
    if currCondition == 'SC':

        if Reading2_key_resp.keys == 'space':
            continueRoutine = False

        if '1' in keys:
            opacityImage2 = 1
            TimeAbs = mainTimer4.getTime()
            TimeSinceLast = probeTimer4.getTime()
            keys = []
            event.clearEvents()

        if (opacityImage2 == 1) and ('u' in keys or 'i' in keys):
            opacityImage2 = 0
            time2 = mainTimer4.getTime() - TimeAbs
            resp2 = keys[0]
            keys = []
            event.clearEvents()
            printNow = 1

        if printNow == 1:
            thisExp.addData('probe_appeared', TimeAbs)  # log the time that the SC probe appeared (user pressed '1' key)
            thisExp.addData('time_since_last_probe',
                            TimeSinceLast)  # log time since last probe. Should be time since start of experiment if this is the first probe
            thisExp.addData('response_delay', time2)  # log delay from probe appearing to response key being pressed
            thisExp.addData('probe_key_response', resp2)  # log the key response to the probe
            thisExp.addData('condition', currCondition)  # save the current condition
            thisExp.nextEntry()  # if we do not move to the next line in the data file, then any other probes that occur before the end of this routine will overwrite our previous probe data
            probeTimer4.reset(0)
            time1 = 0
            time2 = 0
            resp1 = 0
            resp2 = 0
            printNow = 0

    # this is the probe-caught condition but we check if we're in SC because this is the second run
    if currCondition == 'PC':

        if Reading2_key_resp.keys == 'space':
            continueRoutine = False

        if opacityImage1 != 1 and (len(probe4) > myCount4) and probeTimer4.getTime() >= probe4[myCount4]:
            opacityImage1 = 1
            TimeAbs = mainTimer4.getTime()
            TimeSinceLast = probeTimer4.getTime()  # get the time since the last probe went away

        if opacityImage1 == 1 and ('0' in keys or 'i' in keys or 'u' in keys):
            opacityImage1 = 0
            time1 = mainTimer4.getTime() - TimeAbs
            resp1 = keys[0]
            keys = []
            event.clearEvents()
            printNow = 1

        if printNow == 1:
            thisExp.addData('probe_appeared', TimeAbs)  # log the time that the PC probe appeared
            thisExp.addData('time_since_last_probe',
                            TimeSinceLast)  # log time since last probe. Should be time since start of experiment if this is the first probe
            thisExp.addData('response_delay', time1)  # log delay from probe appearing to response key being pressed
            thisExp.addData('probe_key_response', resp1)  # log the key response to the probe
            thisExp.addData('condition', currCondition)  # save the current condition
            thisExp.nextEntry()  # if we do not move to the next line in the data file, then any other probes that occur before the end of this routine will overwrite our previous probe data
            probeTimer4.reset(0)
            time1 = 0
            time2 = 0
            resp1 = 0
            resp2 = 0
            myCount4 = myCount4 + 1
            printNow = 0

    firstLoop4 = False

    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Reading2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Reading2" ---
for thisComponent in Reading2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if Reading2_key_resp.keys in ['', [], None]:  # No response was made
    Reading2_key_resp.keys = None
thisExp.addData('Reading2_key_resp.keys', Reading2_key_resp.keys)
if Reading2_key_resp.keys != None:  # we had a response
    thisExp.addData('Reading2_key_resp.rt', Reading2_key_resp.rt)
thisExp.nextEntry()
# the Routine "Reading2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "EndText" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
EndTextComponents = [EndExpText, key_resp]
for thisComponent in EndTextComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "EndText" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *EndExpText* updates
    if EndExpText.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
        # keep track of start time/frame for later
        EndExpText.frameNStart = frameN  # exact frame index
        EndExpText.tStart = t  # local t and not account for scr refresh
        EndExpText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(EndExpText, 'tStartRefresh')  # time at next scr refresh
        EndExpText.setAutoDraw(True)
    if EndExpText.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > EndExpText.tStartRefresh + 10 - frameTolerance:
            # keep track of stop time/frame for later
            EndExpText.tStop = t  # not accounting for scr refresh
            EndExpText.frameNStop = frameN  # exact frame index
            EndExpText.setAutoDraw(False)

    # *key_resp* updates
    if key_resp.status == NOT_STARTED and t >= 0.0 - frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        key_resp.clock.reset()  # now t=0
        key_resp.clearEvents(eventType='keyboard')
    if key_resp.status == STARTED:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False

    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndTextComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "EndText" ---
for thisComponent in EndTextComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "EndText" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename + '.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
