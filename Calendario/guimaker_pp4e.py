#!/usr/bin/python3
"""
===============================================================================
guimaker_pp4e: Mac menu fixer code, copied from PP4E package's guimaker.py
===============================================================================
"""

import sys
from tkinter import *

# stub out builder class here: this app doesn't use GuiMaker-based windows
class GuiMakerWindowMenu:
    pass


###############################################################################
# For non-GuiMakerWindowMenu clients: customize default menus on Mac OS X
###############################################################################


def fixAppleMenuBar(window,            # a Tk or Toplevel window
                    appname,           # text added to menu labels
                    helpaction=None,   # Help menu callback, no args
                    aboutaction=None,  # About calback, default=Help
                    quitaction=None):  # Quit callback no args, else no-op

    """
    Usage: this should be called on Mac OS for all programs that are not
    GuiMakerWindowMenu clients themselves, but create GuiMakerWindowMenu
    client popup windows: it picks up and saves the app's quit and help to
    apply to popups.  For other programs, this call is optional but useful.

    Details: for Mac/Tk programs that are not GuiMakerWindowMenu clients,
    this function customizes the default Mac menus that always show up at
    top of screen even if the program builds no real menu.  Call this once
    per program, with the main window's app-wide help/quit actions; the
    customized menu with these actions will be inherited by other windows
    in the program that do not build a per-window menu of their own.
    
    Without this, Mac/Tk programs wind up with Tk-propaganda help and
    demos, and a Quit in the app menu or Dock silently closes the entire
    program - changes or not.  On Windows and Linux no menubar appears
    unless one is built explicitly, so calling this is a no-op.

    Note that program-defined menus can vary per window (e.g., "Cut"
    may apply to the current window's text) if a new menu is built for
    new windows (that's why GuiMakerWindowMenu repeats some code here),
    and WM quit can still vary per window.  By contrast, the settings
    made here apply to the entire app/program, not individual windows,
    and remain in force for all windows' menus.  In terms of use cases:
    
    - Programs that mix in GuiMakerWindowMenu for top-toplevel menus:
      do *not* call this, as menus are customized in the superclass.

    - Program that embed GuiMakerFrameMenu windows: call this once
      for the app's main window, not for windows with embedded menus.

    - Programs that build no program-specific menus of their own:
      call this once for the program's main window.

    Subtlety: this call is basically *required* of non-guimaker client
    programs run on Mac that make GuiMakerWindowMenu-client popups.  For
    example, programs that embed PyEdit as a library (e.g., PyMailGUI) may
    create both frame-based menus and standalone popup windows.  For the
    latter, this saves this app's help/quit info, to be applied to menus
    built for later PyEdit popups in GuiMakerWindowMenu.  In this use
    case, the 'first' window is the enclosing app, not a PyEdit Tk; its
    app-wide help and quit will be used in the PyEdit popups' menus too.
    
    Mac's menu paridigm differs from Windows, and requires extra steps.
    Modal dialogs may also disable menu actions, and non-modal dialogs
    can either redraw menus minimally or allow them to remain active.
    """

    # defaults
    helpaction  = helpaction  or (lambda: showinfo(appname, 'No help available'))
    aboutaction = aboutaction or helpaction
    quitaction  = quitaction  or (lambda: None)

    # save this app's info for use in any GuiMaker-based popups it creates
    GuiMakerWindowMenu.__firstWindow = False
    GuiMakerWindowMenu.__appHelp     = helpaction
    GuiMakerWindowMenu.__appAbout    = aboutaction 
    GuiMakerWindowMenu.__appQuit     = quitaction

    if sys.platform.startswith('darwin'):       # for Mac only
        menubar = Menu(window)                  # for this window

        # customize standard app menu on Mac
        menutext = 'About ' + appname
        appmenu = Menu(menubar, name='apple')
        appmenu.add_command(label=menutext, command=aboutaction)
        menubar.add_cascade(menu=appmenu)

        # add automatic windows (dock-ish) menu on Mac
        winmenu = Menu(menubar, name='window')
        menubar.add_cascade(menu=winmenu, label='Window')

        # automatic help menu last=rightmost (no accelerator)
        menutext = appname + ' Help'
        helpmenu = Menu(menubar)  # omit name 
        helpmenu.add_command(label=menutext, command=helpaction)
        menubar.add_cascade(menu=helpmenu, label='Help')

        # attach to window last, so app/etc menus work 
        window.config(menu=menubar)

        # catch std app menu and Dock Quit: this != WM close button
        # registers this once, uses .tk to get to _tkinter from any
        window.tk.createcommand('tk::mac::Quit', quitaction)
