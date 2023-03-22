from __future__ import division
from __future__ import print_function

import os
import psychopy.hardware.keyboard
import pylink
import platform
import random
import time
import sys
import pandas as pd
from EyeLinkCoreGraphicsPsychoPy import EyeLinkCoreGraphicsPsychoPy
from psychopy import visual, core, event, monitors, gui, logging, hardware, data
from PIL import Image  # for preparing the Host backdrop image
from string import ascii_letters, digits

# Switch to the script folder
script_path = os.path.dirname(sys.argv[0])
if len(script_path) != 0:
    os.chdir(script_path)

logging.console.setLevel(logging.CRITICAL)

# Set up PsychoPy Reading Stimuli:
stims = pd.read_csv('All_Stim2.csv')

pci = stims['Pci'].dropna()
pci2 = stims['PCi2'].dropna()
sci = stims['Sci'].dropna()
sci2 = stims['SCi2'].dropna()
trp = stims['trP'].dropna()
lfp = stims['lfP'].dropna()

# Window
win = visual.Window([1920, 1080], fullscr=False, units='pix')
# Keyboard
kb = psychopy.hardware.keyboard.Keyboard()

# Experiment  Instruction Texts

welcome_text = '''
Hello! Thank you for participating in our experiment! 

In this experiment, your task is to read a text and answer some questions about its contents in a memory test later on in Qualtrics. 
As you read, we will record your eye movements with the eye tracker you see just in front of you. 

The researcher will now set you up for experiment. Please let them know if you have any questions and/or concerns.

Press "Space bar" to continue. 
'''

# Condition Assignment

# Use the machine time as a seed to generate a random number from (allows for closer to "truly random" numbers)
random.seed(int(time.process_time()))
# set variable myRand to a random number (either 1 or 2); myRandP (EITHER 3 OR 4)
randCondition = random.randint(1, 2)  # random number for choosing experimental condition order
randPage = random.randint(3, 4)  # random number for choosing reading pages order

# set new variable 'currCondition' depending on what random number we generated
if randCondition == 1:
    # 50% chance of being in the PC condition
    currCondition = "PC"
elif randCondition == 2:
    # 50% chance of being in the SC condition
    currCondition = "SC"

# CREATE A VARIABLE CALLED currConditionP and set it depending on randPage
if randPage == 3:
    # 50% chance of being Tropo pages
    currConditionP = "Tropo"
elif randPage == 4:
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
    # stimFile2 = trp
    stimFile = stims['lfP'].dropna()

elif currConditionP == "Tropo":
    # if we're in the Tropo condition then show TropoPages first run and LifePages second run
    stimFile = stims['trP'].dropna()

# store some useful info about this experiment
info = {'participant': '', 'gender': ['m', 'f', 'n/a'], 'consent given': False, 'dateStr': data.getDateStr()}
# present dialog to participant
dlg = gui.DlgFromDict(info, fixed=['dateStr'])
# if dlg.OK == False or not info['consent given']:
#     core.quit()

filename = "data/%s_%s" % (info['participant'], info['dateStr'])

# create our experiment object to save data
thisExp = data.ExperimentHandler(name='MW_Eyelink', version='1.0',  # not needed, just handy
                                 extraInfo=info,  # the info we created earlier
                                 dataFileName=filename)  # using our string with data/name_date

# Set this variable to True to run the script in "Dummy Mode"
dummy_mode = True

# Set up EDF data file name and local data folder
#
# The EDF data filename should not exceed 8 alphanumeric characters
# use ONLY number 0-9, letters, & _ (underscore) in the filename
edf_fname = info['participant']

# Prompt user to specify an EDF data filename
# before we open a fullscreen window
dlg_title = 'Enter EDF File Name'
dlg_prompt = 'Please enter a file name with 8 or fewer characters\n' + \
             '[letters, numbers, and underscore].'

# loop until we get a valid filename
while True:
    dlg = gui.Dlg(dlg_title)
    dlg.addText(dlg_prompt)
    dlg.addField('File Name:', edf_fname)
    # show dialog and wait for OK or Cancel
    ok_data = dlg.show()
    if dlg.OK:  # if ok_data is not None
        print('EDF data filename: {}'.format(ok_data[0]))
    else:
        print('user cancelled')
        core.quit()
        sys.exit()

    # get the string entered by the experimenter
    tmp_str = dlg.data[0]
    # strip trailing characters, ignore the ".edf" extension
    edf_fname = tmp_str.rstrip().split('.')[0]

    # check if the filename is valid (length <= 8 & no special char)
    allowed_char = ascii_letters + digits + '_'
    if not all([c in allowed_char for c in edf_fname]):
        print('ERROR: Invalid EDF filename')
    elif len(edf_fname) > 8:
        print('ERROR: EDF filename should not exceed 8 characters')
    else:
        break

# Set up a folder to store the EDF data files and the associated resources
# e.g., files defining the interest areas used in each trial
results_folder = 'results'
if not os.path.exists(results_folder):
    os.makedirs(results_folder)

# We download EDF data file from the EyeLink Host PC to the local hard
# drive at the end of each testing session, here we rename the EDF to
# include session start date/time
time_str = time.strftime("_%Y_%m_%d_%H_%M", time.localtime())
session_identifier = edf_fname + time_str

# create a folder for the current testing session in the "results" folder
session_folder = os.path.join(results_folder, session_identifier)
if not os.path.exists(session_folder):
    os.makedirs(session_folder)

# Step 1: Connect to the EyeLink Host PC
if dummy_mode:
    el_tracker = pylink.EyeLink(None)
else:
    try:
        el_tracker = pylink.EyeLink("100.1.1.1")
    except RuntimeError as error:
        print('ERROR:', error)
        core.quit()
        sys.exit()

# Step 2: Open an EDF data file on the Host PC
edf_file = edf_fname + ".EDF"
try:
    el_tracker.openDataFile(edf_file)
except RuntimeError as err:
    print('ERROR:', err)
    # close the link if we have one open
    if el_tracker.isConnected():
        el_tracker.close()
    core.quit()
    sys.exit()

# Add a header text to the EDF file to identify the current experiment name
preamble_text = 'RECORDED BY %s' % os.path.basename(__file__)
el_tracker.sendCommand("add_file_preamble_text '%s'" % preamble_text)

pylink.flushGetkeyQueue()

# Step 3: Configure the tracker
#
# Put the tracker in offline mode before we change tracking parameters
el_tracker.setOfflineMode()

# Get the software version:  1-EyeLink I, 2-EyeLink II, 3/4-EyeLink 1000,
# 5-EyeLink 1000 Plus, 6-Portable DUO
eyelink_ver = 0  # set version to 0, in case running in Dummy mode
if not dummy_mode:
    vstr = el_tracker.getTrackerVersionString()
    eyelink_ver = int(vstr.split()[-1].split('.')[0])
    # print out some version info in the shell
    print('Running experiment on %s, version %d' % (vstr, eyelink_ver))

# File and Link data control
# what eye events to save in the EDF file, include everything by default
file_event_flags = 'LEFT,RIGHT,FIXATION,SACCADE,BLINK,MESSAGE,BUTTON,INPUT,HTARGET'
# what eye events to make available over the link, include everything by default
link_event_flags = 'LEFT,RIGHT,FIXATION,SACCADE,BLINK,BUTTON,FIXUPDATE,INPUT,HTARGET'
# what sample data to save in the EDF data file and to make available
# over the link, include the 'HTARGET' flag to save head target sticker
# data for supported eye trackers
if eyelink_ver > 3:
    file_sample_flags = 'LEFT,RIGHT,GAZE,HREF,RAW,AREA,HTARGET,GAZERES,BUTTON,STATUS,INPUT'
    link_sample_flags = 'LEFT,RIGHT,GAZE,GAZERES,AREA,HTARGET,STATUS,INPUT'
else:
    file_sample_flags = 'LEFT,RIGHT,GAZE,HREF,RAW,AREA,GAZERES,BUTTON,STATUS,INPUT'
    link_sample_flags = 'LEFT,RIGHT,GAZE,GAZERES,AREA,STATUS,INPUT'
el_tracker.sendCommand("file_event_filter = %s" % file_event_flags)
el_tracker.sendCommand("file_sample_data = %s" % file_sample_flags)
el_tracker.sendCommand("link_event_filter = %s" % link_event_flags)
el_tracker.sendCommand("link_sample_data = %s" % link_sample_flags)

# Choose a calibration type, H3, HV3, HV5, HV13 (HV = horizontal/vertical),
el_tracker.sendCommand("calibration_type = HV9")

# Step 4: set up a graphics environment for calibration
#
# Open a window, be sure to specify monitor parameters
mon = monitors.Monitor('myMonitor', width=53.0, distance=70.0)
win = visual.Window(fullscr=True,
                    monitor=mon,
                    winType='pyglet',
                    units='pix')

# get the native screen resolution used by PsychoPy
scn_width, scn_height = win.size

# Pass the display pixel coordinates (left, top, right, bottom) to the tracker
# see the EyeLink Installation Guide, "Customizing Screen Settings"
el_coords = "screen_pixel_coords = 0 0 %d %d" % (scn_width - 1, scn_height - 1)
el_tracker.sendCommand(el_coords)

# Write a DISPLAY_COORDS message to the EDF file
# Data Viewer needs this piece of info for proper visualization
dv_coords = "DISPLAY_COORDS  0 0 %d %d" % (scn_width - 1, scn_height - 1)
el_tracker.sendMessage(dv_coords)

# Configure a graphics environment (genv) for tracker calibration
genv = EyeLinkCoreGraphicsPsychoPy(el_tracker, win)
print(genv)  # print out the version number of the CoreGraphics library

# Set background and foreground colors for the calibration target
# in PsychoPy, (-1, -1, -1)=black, (1, 1, 1)=white, (0, 0, 0)=mid-gray
foreground_color = (0, 0, 0)
background_color = win.color
genv.setCalibrationColors(foreground_color, background_color)

genv.setTargetType(type='circle')
genv.setTargetSize(24)
# genv.setCalibrationSounds('', '', '')

# Request Pylink to use the PsychoPy window we opened above for calibration
pylink.openGraphicsEx(genv)


# define a few helper functions for trial handling

def clear_screen(win):
    """ clear up the PsychoPy window"""

    win.fillColor = genv.getBackgroundColor()
    win.flip()


def show_msg(win, text, wait_for_keypress=True):
    """ Show task instructions on screen"""

    msg = visual.TextStim(win, text,
                          color=genv.getForegroundColor(),
                          wrapWidth=scn_width / 2)
    clear_screen(win)
    msg.draw()
    win.flip()

    # wait indefinitely, terminates upon any key press
    if wait_for_keypress:
        kb.waitKeys()
        clear_screen(win)


def terminate_task():
    """ Terminate the task gracefully and retrieve the EDF data file

    file_to_retrieve: The EDF on the Host that we would like to download
    win: the current window used by the experimental script
    """

    el_tracker = pylink.getEYELINK()

    if el_tracker.isConnected():
        # Terminate the current trial first if the task terminated prematurely
        error = el_tracker.isRecording()
        if error == pylink.TRIAL_OK:
            abort_trial()

        # Put tracker in Offline mode
        el_tracker.setOfflineMode()

        # Clear the Host PC screen and wait for 500 ms
        el_tracker.sendCommand('clear_screen 0')
        pylink.msecDelay(500)

        # Close the edf data file on the Host
        el_tracker.closeDataFile()

        # Show a file transfer message on the screen
        msg = 'EDF data is transferring from EyeLink Host PC...'
        show_msg(win, msg, wait_for_keypress=False)

        # Download the EDF data file from the Host PC to a local data folder
        # parameters: source_file_on_the_host, destination_file_on_local_drive
        local_edf = os.path.join(session_folder, session_identifier + '.EDF')
        try:
            el_tracker.receiveDataFile(edf_file, local_edf)
        except RuntimeError as error:
            print('ERROR:', error)

        # Close the link to the tracker.
        el_tracker.close()

    # close the PsychoPy window
    win.close()

    # quit PsychoPy
    core.quit()
    sys.exit()


def abort_trial():
    """Ends recording """

    el_tracker = pylink.getEYELINK()

    # Stop recording
    if el_tracker.isRecording():
        # add 100 ms to catch final trial events
        pylink.pumpDelay(100)
        el_tracker.stopRecording()

    # clear the screen
    clear_screen(win)
    # Send a message to clear the Data Viewer screen
    bgcolor_RGB = (116, 116, 116)
    el_tracker.sendMessage('!V CLEAR %d %d %d' % bgcolor_RGB)

    # send a message to mark trial end
    el_tracker.sendMessage('TRIAL_RESULT %d' % pylink.TRIAL_ERROR)

    return pylink.TRIAL_ERROR


# Step 5: Set up the camera and calibrate the tracker

# Show the task instructions
task_msg = 'In the task, you may press the SPACEBAR to end a trial\n' + \
           '\nPress Ctrl-C to if you need to quit the task early\n'
if dummy_mode:
    task_msg = task_msg + '\nNow, press ENTER to start the task'
else:
    task_msg = task_msg + '\nNow, press ENTER twice to calibrate tracker'
show_msg(win, task_msg)

# skip this step if running the script in Dummy Mode
if not dummy_mode:
    try:
        el_tracker.doTrackerSetup()
    except RuntimeError as err:
        print('ERROR:', err)
        el_tracker.exitCalibration()

time1 = 0  # variables for recording response time data
time2 = 0
resp1 = 0  # variables for recording key press data
resp2 = 0
printNow = 0  # used to trigger data writing to output file
keys = ""  # stores keypress values
# these three variables are used to start our timers at the right spot and avoid some edge cases

timerStarted2 = False
# start two clocks
mainTimer = core.Clock()
probeTimer = core.Clock()  # this one stops and restarts every time one of our probe/intentionality images pops up
myCount = 1  # this counts up and tells which value from the probe list we should use

# clear the keyboard buffer just in case they recently pressed a relevant key


if currCondition == 'SC':
    # make an index to keep track of the iteration of page being displayed.
    current_index = 0

    # Start a loop that will continue until the escape key is pressed
    while current_index != 16:

        # get a reference to the currently active EyeLink connection
        el_tracker = pylink.getEYELINK()

        # put the tracker in the offline mode first
        el_tracker.setOfflineMode()

        # clear the host screen before we draw the backdrop
        el_tracker.sendCommand('clear_screen 0')

        page = visual.ImageStim(win, image=stimFile.iloc[current_index])

        im = Image.open(stimFile.iloc[current_index])  # read image with PIL
        im = im.resize((scn_width, scn_height))
        img_pixels = im.load()  # access the pixel data of the image
        pixels = [[img_pixels[i, j] for i in range(scn_width)]
                  for j in range(scn_height)]
        el_tracker.bitmapBackdrop(scn_width, scn_height, pixels,
                                  0, 0, scn_width, scn_height,
                                  0, 0, pylink.BX_MAXCONTRAST)

        # OPTIONAL: draw landmarks and texts on the Host screen
        left = int(scn_width / 2.0) - 60
        top = int(scn_height / 2.0) - 60
        right = int(scn_width / 2.0) + 60
        bottom = int(scn_height / 2.0) + 60
        draw_cmd = 'draw_filled_box %d %d %d %d 1' % (left, top, right, bottom)
        el_tracker.sendCommand(draw_cmd)

        # send a "TRIALID" message to mark the start of a trial
        el_tracker.sendMessage("TRIALID %d" % current_index)

        # record_status_message : show some info on the Host PC
        # here we show how many trial has been tested
        status_msg = 'TRIAL number %s' % stimFile.iloc[current_index]
        el_tracker.sendCommand("record_status_message '%s'" % status_msg)

        # drift check
        # we recommend drift-check at the beginning of each trial
        # the doDriftCorrect() function requires target position in integers
        # the last two arguments:
        # draw_target (1-default, 0-draw the target then call doDriftCorrect)
        # allow_setup (1-press ESCAPE to recalibrate, 0-not allowed)
        #
        # Skip drift-check if running the script in Dummy Mode
        while not dummy_mode:
            # terminate the task if no longer connected to the tracker or
            # user pressed Ctrl-C to terminate the task
            if (not el_tracker.isConnected()) or el_tracker.breakPressed():
                terminate_task()

            # drift-check and re-do camera setup if ESCAPE is pressed
            try:
                error = el_tracker.doDriftCorrect(int(scn_width / 2.0),
                                                  int(scn_height / 2.0), 1, 1)
                # break following a success drift-check
                if error is not pylink.ESC_KEY:
                    break
            except:
                pass

        # put tracker in idle/offline mode before recording
        el_tracker.setOfflineMode()

        # Start recording
        # arguments: sample_to_file, events_to_file, sample_over_link,
        # event_over_link (1-yes, 0-no)
        try:
            el_tracker.startRecording(1, 1, 1, 1)
        except RuntimeError as error:
            print("ERROR:", error)
            abort_trial()

        # Allocate some time for the tracker to cache some samples
        pylink.pumpDelay(100)

        # show the image, and log a message to mark the onset of the image
        clear_screen(win)
        page.draw()
        win.flip()
        el_tracker.sendMessage('image_onset')
        img_onset_time = core.getTime()  # record the image onset time

        # Send a message to clear the Data Viewer screen, get it ready for
        # drawing the pictures during visualization
        bgcolor_RGB = (116, 116, 116)
        el_tracker.sendMessage('!V CLEAR %d %d %d' % bgcolor_RGB)

        # send over a message to specify where the image is stored relative
        # to the EDF data file, see Data Viewer User Manual, "Protocol for
        # EyeLink Data to Viewer Integration"
        bg_image = 'D:\LabResearch\BARLab\Development\MW' + stimFile.iloc[current_index]

        imgload_msg = '!V IMGLOAD CENTER %s %d %d %d %d' % (bg_image,
                                                            int(scn_width / 2.0),
                                                            int(scn_height / 2.0),
                                                            int(scn_width),
                                                            int(scn_height))

        el_tracker.sendMessage(imgload_msg)
        # for all supported interest area commands, see the Data Viewer Manual,
        # "Protocol for EyeLink Data to Viewer Integration"
        ia_pars = (1, left, top, right, bottom, 'screen_center')
        el_tracker.sendMessage('!V IAREA RECTANGLE %d %d %d %d %d %s' % ia_pars)

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

        # clear the screen
        clear_screen(win)
        el_tracker.sendMessage('blank_screen')
        # send a message to clear the Data Viewer screen as well
        el_tracker.sendMessage('!V CLEAR 128 128 128')

        # stop recording; add 100 msec to catch final events before stopping
        pylink.pumpDelay(100)
        el_tracker.stopRecording()

        # record trial variables to the EDF data file, for details, see Data
        # Viewer User Manual, "Protocol for EyeLink Data to Viewer Integration"
        el_tracker.sendMessage('!V TRIAL_VAR condition %s' % currCondition)
        el_tracker.sendMessage('!V TRIAL_VAR image %s' % page)
        # el_tracker.sendMessage('!V TRIAL_VAR RT %d' % RT)

        # send a 'TRIAL_RESULT' message to mark the end of trial, see Data
        # Viewer User Manual, "Protocol for EyeLink Data to Viewer Integration"
        el_tracker.sendMessage('TRIAL_RESULT %d' % pylink.TRIAL_OK)
